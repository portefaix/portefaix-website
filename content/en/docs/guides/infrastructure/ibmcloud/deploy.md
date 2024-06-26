---
type: docs
title: "Install on IBMCloud"
description: "Running Portefaix on IBMCloud"
weight: 50
categories: "HowTo"
tags: ["IBMCloud"]
---

<a id="ibmcloud"></a>

## Setup

```shell
# IBMCloud
export IAAS_CLASSIC_USERNAME="xxxxxxxxxxxx"
export IC_API_KEY="xxxxxxxxxxxxxx"
export IAAS_CLASSIC_API_KEY="xxxxxxxxxxxxxxxxx"
# For Terraform Backend S3
# See 

```

And load environment :

```shell
❯ . ./portefaix.sh ibmcloud
```

Authentication:

```shell
❯ make -f hack/build/ibmcloud.mk ibmcloud-init ENV=staging
```

Then, generate the right set of HMAC credentials : [documentation](https://www.ibm.com/cloud/blog/store-terraform-states-cloud-object-storage)

```shell
❯ export AWS_ACCESS_KEY_ID="xxxxxxxxxx"
❯ export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxx"
```

## Storage for Terraform

Create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/ibmcloud.mk ibmcloud-bucket-create ENV=staging
```

## Terraform

### VPC

```shell
❯ make terraform-apply SERVICE=terraform/ibmcloud/vpc ENV=staging
```

### IKS

```shell
❯ make terraform-apply SERVICE=terraform/ibmcloud/iks ENV=staging
```

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in IBMCloud

### Configure IBMCloud CLI

```shell
❯ . ./portefaix.sh ibmcloud
[ Portefaix ]
✔ Configuration file
✔ Flux
✔ PagerDuty
✔ Terraform Cloud
✔ IBMCloud
```

### Configure kubectl

```shell
❯ make -f hack/build/ibmcloud.mk ibmcloud-kube-credentials CLOUD=ibmcloud ENV=staging
```

```shell
❯ kubectl get nodes
NAME            STATUS   ROLES    AGE   VERSION
10.242.0.10     Ready    <none>   13m   v1.22.7+IKS
10.242.0.7      Ready    <none>   29m   v1.22.7+IKS
10.242.128.10   Ready    <none>   12m   v1.22.7+IKS
10.242.128.7    Ready    <none>   29m   v1.22.7+IKS
10.242.64.6     Ready    <none>   29m   v1.22.7+IKS
10.242.64.8     Ready    <none>   13m   v1.22.7+IKS
```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)