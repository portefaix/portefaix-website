---
type: docs
title: "Install on Digital Ocean"
description: "Running Portefaix on Digital Ocean"
weight: 50
categories: "HowTo"
tags: ["Digital Ocean"]
---

<a id="do"></a>

## Setup

```shell
# Digital Ocean
function setup_digitalocean() {
    export DIGITALOCEAN_TOKEN="xxxxxxxxxxxx"
    export SPACES_ENDPOINT_URL="fra1.digitaloceanspaces.com"
    export SPACES_ACCESS_KEY_ID="xxxxxxxxxx"
    export SPACES_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxx"
    export AWS_ACCESS_KEY_ID="${SPACES_ACCESS_KEY_ID}"
    export AWS_SECRET_ACCESS_KEY="${SPACES_SECRET_ACCESS_KEY}"
    export AWS_DEFAULT_REGION="eu-west-3"
    export AWS_REGION="eu-west-3"
}
```

And load environment :

```shell
❯ . ./portefaix.sh digitalocean
```

## Storage for Terraform

Create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/digitalocean.mk exo-bucket ENV=dev
```

## Authentication and Authorization

This section shows the how to setup Portefaix with authentication and authorization support in Digital Ocean

### Configure Digital Ocean

```shell
❯ . ./portefaix.sh digitalocean
[ Portefaix ]
Setup credentials
Done
```

### Configure kubectl

```shell
❯ make kubernetes-credentials CLOUD=digitalocean ENV=dev
```

```shell
❯ kubectl get nodes

```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)
