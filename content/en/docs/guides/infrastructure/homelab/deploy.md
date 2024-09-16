+++
title = "Install Portefaix"
description = "Instructions for deploying Portefaix infrastructure on Homelab"
weight = 10
+++

<a id="os"/></a>

## Operating System

Setup operating system for Raspberry PI.

See: https://www.raspberrypi.org/software/

Or:

```shell
❯ sudo dd if=/dev/zero of=/dev/mmcblk0 conv=noerror status=progress
❯ sudo./hack/scripts/sdcard.sh <hostname> /dev/mmcblk0
```

Enable SSH :

```shell
❯ make -f hack/build/k3s.mk sdcard-mount ENV=homelab
❯ sudo touch /mnt/portefaix/boot/ssh
❯ echo portefaix-xxx | sudo tee /mnt/portefaix/root/etc/hostname
❯ make -f hack/build/k3s.mk sdcard-unmount ENV=homelab
```

Copy keys to each node:

```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@x.x.x.x
```

## Ansible

```shell
❯ make ansible-deps SERVICE=ansible/k3s/machines CLOUD=k3s ENV=homelab
❯ make ansible-run SERVICE=ansible/k3s/machines CLOUD=k3s ENV=homelab
```

## K3Sup

Create the master :

```shell
❯ make -f hack/build/k3s.mk  k3s-create ENV=homelab SERVER_IP=x.x.x.x EXTERNAL_IP=x.x.x.x
```

For each node, add it to the cluster, then add a label:

```shell
❯ make -f hack/build/k3s.mk k3s-join ENV=homelab SERVER_IP=x.x.x.x AGENT_IP=x.x.x.x EXTERNAL_IP=x.x.x.x
```

Authentication and authorization

```shell
❯ make kubernetes-credentials CLOUD=k3s ENV=homelab
```

Set labels:

```shell
❯ kubectl label node <NODE_NAME> node-role.kubernetes.io/worker=true
```

We add also these labels:

| Label                                | Description                       |
| ------------------------------------ | --------------------------------- |
| node-role.kubernetes.io/infra=true   | For core components               |
| node-role.kubernetes.io/lowcost=true | For pocs, small applications, ... |

The nodes are in a `NotReady` state, due to the Pod Networking CNI plugin is not available.
[Cilium](https://cilium.io/) must be installed:

```shell
❯ make bootstrap-crds ENV=homelab CLOUD=k3s
❯ make bootstrap-cilium ENV=homelab CLOUD=k3s
```

Then check nodes:

```shell
❯ kubectl get node -o wide
NAME          STATUS     ROLES                       AGE     VERSION        INTERNAL-IP     EXTERNAL-IP      OS-IMAGE           KERNEL-VERSION     CONTAINER-RUNTIME
portefaix     Ready      control-plane,etcd,master   3h37m   v1.30.2+k3s1   192.168.0.61    100.79.205.64    Ubuntu 24.04 LTS   6.8.0-36-generic   containerd://1.7.17-k3s1
portefaix-1   NotReady   lowcost,worker              155m    v1.30.2+k3s1   192.168.0.208   100.115.34.57    Ubuntu 24.04 LTS   6.8.0-1005-raspi   containerd://1.7.17-k3s1
portefaix-2   Ready      lowcost,worker              154m    v1.30.2+k3s1   192.168.0.116   100.126.100.42   Ubuntu 24.04 LTS   6.8.0-1005-raspi   containerd://1.7.17-k3s1
portefaix-6   Ready      infra,worker                3h21m   v1.30.2+k3s1   192.168.0.233   100.111.218.32   Ubuntu 24.04 LTS   6.8.0-36-generic   containerd://1.7.17-k3s1
portefaix-7   Ready      infra,worker                3h18m   v1.30.2+k3s1   192.168.0.250   100.86.220.99    Ubuntu 24.04 LTS   6.8.0-36-generic   containerd://1.7.17-k3s1
```

and Cilium status:

```shell
❯ cilium status
    /¯¯\
 /¯¯\__/¯¯\    Cilium:         OK
 \__/¯¯\__/    Operator:       OK
 /¯¯\__/¯¯\    Hubble:         OK
 \__/¯¯\__/    ClusterMesh:    disabled
    \__/

Deployment        cilium-operator    Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet         cilium             Desired: 4, Ready: 4/4, Available: 4/4
Deployment        hubble-relay       Desired: 1, Ready: 1/1, Available: 1/1
Deployment        hubble-ui          Desired: 1, Ready: 1/1, Available: 1/1
Containers:       cilium             Running: 4
                  cilium-operator    Running: 1
                  hubble-relay       Running: 1
                  hubble-ui          Running: 1
Cluster Pods:     4/4 managed by Cilium
```

## Cloudflare

[R2](https://www.cloudflare.com/products/r2/) is used to store the Terraform states and for S3 buckets

Setup your Cloudflare Account ID, and your AWS credentials

```shell
function setup_cloudflare() {
    echo_info "Cloudflare"
    export CLOUDFLARE_ACCOUNT_ID="xxxxxxxx"
    export AWS_ACCESS_KEY_ID="xxxxxxxxxxx"
    export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxx"
}

function setup_cloud_provider {
    case $1 in
    
        ...

        "k3s")
            setup_tailscale
            setup_freebox
            setup_cloudflare
            ;;
        *)
            echo -e "${KO_COLOR}Invalid cloud provider: $1.${NO_COLOR}"
            usage
            ;;
    esac
}
```

The creates the bucket for Terraform:

```shell
❯ make -f hack/build/k3s.mk cloudflare-bucket-create ENV=homelab
[portefaix] Create bucket for Terraform states
{
    "Location": "/portefaix-homelab-tfstates"
}
```

## Terraform

Configure DNS:

```shell
❯ make terraform-apply SERVICE=terraform/k3s/dns ENV=homelab
```

Creates the R2 buckets for Observability components:

```shell
❯ make terraform-apply SERVICE=terraform/k3s/observability ENV=homelab
```

## Applications

Next: [Gitops](/docs/gitops)