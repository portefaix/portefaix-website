---
type: docs
title: "Install on Scaleway"
description: "Running Portefaix on Scaleway"
weight: 50
categories: "HowTo"
tags: ["Scaleway"]
---

<a id="scaleway"></a>

## Setup

```shell
# Scaleway
function setup_scaleway() {
    export SCW_ACCESS_KEY="xxxxx"
    export SCW_SECRET_KEY="xxxx"
    export SCW_DEFAULT_PROJECT_ID="xxxx"
    export SCW_DEFAULT_ORGANIZATION_ID="${SCW_DEFAULT_PROJECT_ID}"
    export AWS_ACCESS_KEY_ID="${SCW_ACCESS_KEY}"
    export AWS_SECRET_ACCESS_KEY="${SCW_SECRET_KEY}"
    export AWS_DEFAULT_REGION="eu-west-3"
    export AWS_REGION="eu-west-3"
}
```

And load environment :

```shell
❯ . ./portefaix.sh scaleway
```

## Storage for Terraform

Create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/scw.mk scw-bucket ENV=sandbox
```

## Terraform

### SKS

```shell
❯ make terraform-apply SERVICE=iac/scaleway/kapsule ENV=sandbox
```

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in Scaleway

## Configure Scaleway

```shell
❯ . ./portefaix.sh scaleway
[ Portefaix ]
Setup credentials
Done
```

## Configure kubectl

```shell
❯ make kubernetes-credentials CLOUD=scaleway ENV=sandbox
```

```shell
❯ kubectl get nodes

```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)