---
type: docs
title: "Install on Alibaba Cloud"
description: "Running Portefaix on Alibaba Cloud ACK"
weight: 50
categories: "HowTo"
tags: ["Alicloud"]
---

<a id="alicloud"></a>

## Setup

Create an admin user, then API Keys.
And configure Portefaix environment file `${HOME}/.config/portefaix/portefaix.sh`:

```shell
# Alicloud
function setup_alicloud() {
    # Alicloud User: Portefaix Admin
    export ALICLOUD_ACCESS_KEY="xxxxxxxxxx"
    export ALICLOUD_SECRET_KEY="xxxxxxxxxxxxxxxx"
    export ALICLOUD_REGION="eu-central-1"
    # For Terraform Cloud
    export TF_VAR_access_key="${ALICLOUD_ACCESS_KEY}"
    export TF_VAR_secret_key="${ALICLOUD_SECRET_KEY}"
    export TF_VAR_region="${ALICLOUD_REGION}"
}
```

And load environment :

```shell
❯ . ./portefaix.sh alicloud
```

## Storage for Terraform

Create an OSS bucket for Terraform states:

```shell
❯ make -f hack/build/alicloud.mk aliyun-bucket-create ENV=staging
```

Create a TableStore instance:

```shell
❯ make -f hack/build/alicloud.mk aliyun-tablestore-create ENV=staging
```

<a id="alicloud-terraform-cloud"></a>

## Terraform Cloud / Github Actions

[Terraform Cloud](https://terraform.cloud) is used as the remote backend. [Github Actions](https://github.com/features/actions) perform tasks to deploy the Alibaba Cloud infrastructure and undeploy:

<img src="/img/alicloud/portefaix-alicloud-deploy.png" alt="Portefaix Alibaba Cloud deployment" class="mt-3 mb-3 rounded">

<img src="/img/alicloud/portefaix-alicloud-undeploy.png" alt="Portefaix Azure deletion" class="mt-3 mb-3 rounded">

<a id="alicloud-gitops"></a>

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in Alibaba Cloud

### Configure Alibaba Cloud

```shell
❯ . ./portefaix.sh alicloud
[ Portefaix ]
Setup credentials
Done
```

### Bastion

{{% alert title="Work In Progress" color="warning" %}}
{{% /alert %}}

### Configure kubectl

{{% alert title="Work In Progress" color="warning" %}}
{{% /alert %}}

```shell
❯ make kubernetes-credentials CLOUD=alicloud ENV=staging
```

```shell
❯ kubectl get nodes
NAME                                        STATUS   ROLES    AGE    VERSION
```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)

## Inspec for Alicloud

### Setup

[Inspec](http://inspec.io/) is used to check infrastructure.

Check:

```shell
❯ make -f hack/build/alicloud.mk inspec-alicloud-debug
```

Execute tests:

{{% alert title="Work In Progress" color="warning" %}}
{{% /alert %}}


### CIS Kubernetes Benchmark

```shell
❯ make -f hack/build/alicloud.mk inspec-alicloud-kubernetes ENV=staging
```
