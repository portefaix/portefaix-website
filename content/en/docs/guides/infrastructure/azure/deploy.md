---
type: docs
title: "Install on Microsoft Azure"
description: "Running Portefaix on Microsoft Azure"
weight: 50
categories: "HowTo"
tags: ["Azure"]
---

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

[Github Actions](https://github.com/features/actions) with [Terraform Cloud](https://www.terraform.io/cloud)
could used to deploy and undeploy the infrastructure:

<img src="/img/azure/portefaix-azure-deploy.png" alt="Portefaix Azure deployment" class="mt-3 mb-3 rounded">

<img src="/img/azure/portefaix-azure-undeploy.png" alt="Portefaix Azure deletion" class="mt-3 mb-3 rounded">

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in Microsoft Azure (AZURE)

```shell
❯ . ./portefaix.sh azure
[ Portefaix ]
Setup credentials
Done
```

Configure kubectl

```shell
❯ make -f hack/build/azure.mk azure-kube-credentials ENV=dev
```

```shell
❯ kubectl get nodes
NAME                           STATUS   ROLES   AGE   VERSION
aks-core-19506595-vmss000000   Ready    agent   8h    v1.18.10
```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)

## Inspec

### Setup

[inspec](http://inspec.io/) is used to check infrastructure.

Check:

```shell
❯ make -f hack/build/azure.mk inspec-debug
Test infrastructure

 ────────────────────────────── Platform Details ──────────────────────────────

Name:      azure
Families:  cloud, api
Release:   azure_mgmt_resources-v0.17.8
```

Execute tests:

```shell
❯ make -f hack/build/azure.mk inspec-test SERVICE=iac/azure/<SERVICE> ENV=dev
```

You could upload JSON results file to [Heimdall Lite](https://heimdall-lite.mitre.org/) to display ressults

### Microsoft Azure CIS Foundations

You could perform tests accoring the [CIS Microsoft Azure Foundations Security Benchmark](https://azure.microsoft.com/fr-fr/resources/cis-microsoft-azure-foundations-security-benchmark/):

```shell
❯ make -f hack/build/azure.mk inspec-cis ENV=dev
```

### AKS

<img src="/img/azure/inspec-azure-aks.png"
 alt="AKS"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `resourcegroup-1` | Check that resource group exists |
| `aks-1` | Ensure logging to Azure Monitor is configured |
| `aks-2` | Ensure RBAC is enabled |
| `aks-3` | Ensure API Server Authorized IP Ranges are configured |
