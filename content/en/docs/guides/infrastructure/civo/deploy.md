---
type: docs
title: "Install on Civo"
description: "Running Portefaix on Civo"
weight: 50
categories: "HowTo"
tags: ["Civo"]
---

<a id="civo"></a>

## Setup

```shell
# Civo
export CIVO_TOKEN="xxxxxxxxxxxxxxxx"
```

And load environment :

```shell
❯ . ./portefaix.sh civo
```

## Storage for Terraform

{{% alert title="Work In Progress" color="warning" %}}
{{% /alert %}}

## Terraform

### Network

```shell
❯ make terraform-apply SERVICE=terraform/civo/network ENV=dev
```

### Kubernetes

```shell
❯ make terraform-apply SERVICE=terraform/civo/kubernetes ENV=dev
```

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in Civo

### Configure Civo

```shell
❯ . ./portefaix.sh civo
[ Portefaix ]
 Flux
 Pagerduty
 TerraformCloud
 Civo
✔ Done
```

### Configure kubectl

```shell
❯ make -f hack/build/civo.mk civo-kube-credentials ENV=dev
```

```shell
❯ kubectl get nodes
NAME                                                      STATUS   ROLES    AGE     VERSION
k3s-portefaix-dev-civo-691a-de1391-node-pool-8c2e-859cq   Ready    <none>   6m29s   v1.22.2+k3s1
```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)