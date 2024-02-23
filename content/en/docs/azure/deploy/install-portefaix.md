+++
title = "Install Portefaix"
description = "Instructions for deploying Portefaix on Azure"
weight = 10
+++

<a id="azure"></a>

## Setup

Export Azure credentials:

```shell
❯ export AZURE_SUBSCRIPTION_ID="xxxxxx"
```

create a service principal:

```shell
❯ make -f hack/build/azure.mk azure-sp
```

The `appId`, `password`, and `tenant` values are used in the next step:

```shell
export ARM_SUBSCRIPTION_ID="<azure_subscription_id>"
export ARM_TENANT_ID="<azure_subscription_tenant_id>"
export ARM_CLIENT_ID="<service_principal_appid>"
export ARM_CLIENT_SECRET="<service_principal_password>"
```

## Storage for Terraform

Create a [Storage Account](https://portal.azure.com/#create/Microsoft.StorageAccount) :

```shell
❯ make -f hack/build/azure.mk azure-storage-account
XXXXXXXXXXX
```

You could see the Key on the output.

Create storage container for Terraform states:

```shell
❯ make -f hack/build/azure.mk azure-storage-container AZ_STORAGE_ACCOUNT_KEY="xxxxxxxxxxxxxxxxx"
```

Set permissions:

```shell
❯ make -f hack/build/azure.mk azure-permissions
```

Enable preview features:

```shell
❯ make -f hack/build/azure.mk azure-wasi
```

## Terraform

[Github Actions](https://github.com/features/actions) with [Terraform Cloud](https://www.terraform.io/cloud) could used to deploy the infrastructure:

<img src="/img/azure/portefaix-azure-deploy.png" alt="Portefaix Azure deployment" class="mt-3 mb-3 rounded">

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)