+++
title = "Install Portefaix"
description = "Instructions for deploying Portefaix infrastructure on Homelab"
weight = 10
+++

<a id="os"/></a>

## Secrets

All secrets in this repo are encrypted with SOPS leveraging age.
Generate the public key and age secret:

```shell
❯ age-keygen -o portefaix.homelab.txt
```

SOPS is configured to use the age public key via the .sops.yaml in the root of this repo to encrypt files

## Operating System

Generate the customized Talos Linux image using [Talos Image Factory](https://www.talos.dev/v1.7/learn-more/image-factory), and download them:

```shell
❯ make -f hack/build/talos.mk talos-image
```

Then:
- boot one machine off the ISO to be the control plane node
- boot one or more machines off the same ISO to be the workers

<!-- 
Download the Talos iso files:
```shell
❯ make -f hack/build/talos.mk talos-iso SCHEMATIC_ID=20301c5ab1025be5b64591acd0bbb1a2c1a0a16d9ad084e5cc86c0d7f5793f48 ARCH=amd64
❯ make -f hack/build/talos.mk talos-iso SCHEMATIC_ID=20301c5ab1025be5b64591acd0bbb1a2c1a0a16d9ad084e5cc86c0d7f5793f48 ARCH=arm64
``` -->

To designate the disk where Talos will be installed, update installDisk in `talconfig.yaml`.
Use this command to display disks (where <IP_ADDR> is your node's local IP address):

```shell
❯ talosctl disks -e <IP_ADDR> -n <IP_ADDR> --insecure
```

Generate your own Talos cluster secrets:

```shell
❯ make -f hack/build/talos.mk talos-secrets ENV=homelab
```

Generate the Talos configuration:

```shell
❯ make -f hack/build/talos.mk talos-config ENV=homelab
```

Apply the corresponding configuration for each of your node:

```shell
❯ make -f hack/build/talos.mk talos-apply ENV=homelab NODE_NAME=<NAME> NODE_IP=<IP_ADDR>
```

Save the Talos configuration:

```shell
❯ cp hack/talos/homelab/clusterconfig/talosconfig $HOME/.talos/config
```

Wait for a few minutes for the nodes to reboot, then bootstrap Talos:

```shell
❯ make -f hack/build/talos.mk talos-bootstrap ENV=homelab NODE_IP=<IP_ADDR>
```

Generate kubeconfig:

```shell
❯ make -f hack/build/talos.mk talos-kubeconfig ENV=homelab NODE_IP=<IP_ADDR>
```

```shell
❯ talosctl services
NODE           SERVICE         STATE     HEALTH   LAST CHANGE   LAST EVENT
192.168.0.61   apid            Running   OK       29m57s ago    Health check successful
192.168.0.61   containerd      Running   OK       30m5s ago     Health check successful
192.168.0.61   cri             Running   OK       29m57s ago    Health check successful
192.168.0.61   etcd            Running   OK       9m41s ago     Health check successful
192.168.0.61   ext-tailscale   Waiting   ?        29m57s ago    Waiting for extension service config
192.168.0.61   kubelet         Running   OK       29m48s ago    Health check successful
192.168.0.61   machined        Running   OK       30m10s ago    Health check successful
192.168.0.61   syslogd         Running   OK       30m9s ago     Health check successful
192.168.0.61   trustd          Running   OK       29m57s ago    Health check successful
192.168.0.61   udevd           Running   OK       30m7s ago     Health check successful
```

```shell
❯ kubectl get nodes -o wide
NAME        STATUS     ROLES                  AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE         KERNEL-VERSION   CONTAINER-RUNTIME
portefaix   NotReady   control-plane,master   10m   v1.30.3   192.168.0.61   <none>        Talos (v1.7.6)   6.6.43-talos     containerd://1.7.18
```

## Cilium

The nodes are in a `NotReady` state, due to the Pod Networking CNI plugin is not available.
[Cilium](https://cilium.io/) must be installed:

```shell
❯ make bootstrap-crds ENV=homelab CLOUD=k3s
❯ make bootstrap-cilium ENV=homelab CLOUD=k3s
```

```shell
❯ kubectl get node -o wide

```

and Cilium status:

```shell
❯ cilium status

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

        "talos")
            setup_tailscale
            setup_cloudflare
            ;;
        *)
            echo -e "${KO_COLOR}Invalid cloud provider: $1.${NO_COLOR}"
            usage
            ;;
    esac
}
```

Then creates the bucket for Terraform tfstate:

```shell
❯ make -f hack/build/talos.mk cloudflare-bucket-create ENV=homelab
[portefaix] Create bucket for Terraform states
{
    "Location": "/portefaix-talos-tfstates"
}
```

## Terraform

Configure DNS:

```shell
❯ make terraform-apply SERVICE=terraform/talos/dns ENV=homelab
```

Creates the R2 buckets for Observability components:

```shell
❯ make terraform-apply SERVICE=terraform/talos/observability ENV=homelab
```

## Applications

Next: [Gitops](/docs/gitops)