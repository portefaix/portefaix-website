+++
title = "Install Portefaix"
description = "Instructions for deploying Portefaix infrastructure on Homelab"
weight = 10
+++

<a id="os"/></a>

## Operating System

Generate the customized Talos Linux image using [Talos Image Factory](https://www.talos.dev/v1.7/learn-more/image-factory):

```shell
❯ make -f hack/build/talos.mk talos-image SCHEMATIC=hack/kind/talos-schematic-rpi.yaml
{"id":"xxxxxx"}
❯ make -f hack/build/talos.mk talos-image SCHEMATIC=hack/kind/talos-schematic.yaml
{"id":"xxxxxx"}
```

Then:
- boot one machine off the ISO to be the control plane node
- boot one or more machines off the same ISO to be the workers

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

Configure Talos cluster:



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