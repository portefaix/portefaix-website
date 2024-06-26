---
type: docs
title: "Install on Exoscale"
description: "Running Portefaix on Exoscale"
weight: 50
categories: "HowTo"
tags: ["Exoscale"]
---

<a id="exo"></a>

## Setup

```shell
# AWS
export EXOSCALE_API_KEY="xxxxx"
export EXOSCALE_API_SECRET="xxxxxxxxxxx"
export AWS_ACCESS_KEY_ID="${EXOSCALE_API_KEY}"
export AWS_SECRET_ACCESS_KEY="${EXOSCALE_API_SECRET}"
```

And load environment :

```shell
❯ . ./portefaix.sh exoscale
```

## Storage for Terraform

Create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/exoscale.mk exo-bucket ENV=dev
```

## Terraform

### SKS

```shell
❯ make terraform-apply SERVICE=iac/exoscale/sks ENV=dev
```

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in Exoscale

### Configure Exoscale

```shell
❯ . ./portefaix.sh exoscale
[ Portefaix ]
Setup credentials
Done
```

### Configure kubectl

```shell
❯ make kubernetes-credentials CLOUD=exoscale ENV=dev
```

```shell
❯ kubectl get nodes

```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)