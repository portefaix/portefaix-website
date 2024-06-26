+++
title = "Install Portefaix"
description = "Instructions for deploying Portefaix on Oracle Cloud"
weight = 10
+++

<a id="oci"></a>

## Setup

Configure Oracle CLI. See https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm

Load environment :

```shell
❯ . ./portefaix.sh oci
```

Then authentication:

```shell
❯ make -f hack/build/oci.mk oci-authenticate  ENV=staging
```

## Create a new compartment

```shell
❯ make -f hack/build/oci.mk oci-compartment ENV=staging
```

## Storage for Terraform

Check compartement ID from output of the previous command and create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/oci.mk oci-bucket ENV=staging COMPARTMENT_ID=ocid1.compartment.oc1....
```

Bootstrap:

```shell
❯ make terraform-apply SERVICE=terraform/oci/root ENV=main
❯ make terraform-apply SERVICE=terraform/oci/terraform-cloud ENV=main
```

<a id="oci-terraform-cloud"></a>

## Terraform Cloud / Github Actions

[Terraform Cloud](https://terraform.cloud) is used as the remote backend. [Github Actions](https://github.com/features/actions) perform tasks to deploy the Oracle Cloud Infrastructure.

Configure Terraform Cloud workspaces:

```shell
❯ make terraform-apply SERVICE=terraform/oci/terraform-cloud ENV=main
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

<a id="oci-gitops"></a>

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)