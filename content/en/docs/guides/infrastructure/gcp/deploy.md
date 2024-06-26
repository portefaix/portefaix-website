---
type: docs
title: "Install on Google Cloud Platform"
description: "Running Portefaix on Google Cloud Platform"
weight: 50
categories: "HowTo"
tags: ["GCP"]
---

<a id="gcloud"/></a>

## Organization

Create a Google Cloud Organization using **Google Workspace** or **Cloud Identity**

See: https://cloud.google.com/resource-manager/docs/creating-managing-organization?hl=fr

## Bootstrap

Authenticate on the Google Cloud Platform:

```shell
❯ gcloud auth login
xxxxxxxxxx

❯ gcloud organizations list
DISPLAY_NAME             ID  DIRECTORY_CUSTOMER_ID
xxxxxxx              xxxxxx               xxxxxxxx
```

You could find the `GCP_USER`:

```shell
❯ gcloud auth list
            Credentialed Accounts
ACTIVE  ACCOUNT
*       xxxxxxxxxxxx@portefaix.xyz
```

Create the Service Account on bootstrap project:

```shell
❯ make -f hack/build/gcp.mk gcp-bootstrap-sa
❯ make -f hack/build/gcp.mk gcp-bootstrap-credentials
❯ make -f hack/build/gcp.mk gcp-bootstrap-iam GCP_ORG_ID=xxxx
```

Enable APIs on Bootstrap project:

```shell
❯ make -f hack/build/gcp.mk gcp-bootstrap-apis
```









Bootstrap the organization:

```shell
❯ make -f hack/build/gcp.mk gcp-organization-bootstrap GCP_ORG_ID=xxxxxxxxxxx GCP_USER=xxxxxxxxxxxxxxxxx
```

Then go to https://console.cloud.google.com/cloud-setup/organization to creates groups and create the billing account.

Then create the bootstrap project:

```shell
❯ make -f hack/build/gcp.mk gcp-organization-project GCP_ORG_NAME=xxxx GCP_ORG_ID=xxxxxxxxxxx
```

Associate this project to the Billing Account (on GCP console or using gcloud):

```shell
gcloud alpha billing accounts projects link my-project --billing-account=xxxxxxx
```

Then create the bucket for boostraping the organization:

```shell
❯ make -f hack/build/gcp.mk gcp-bucket GCP_ORG_NAME=xxxxxxx
```

Bootstrap:

```shell
❯ make terraform-apply SERVICE=terraform/gcp/root ENV=main
```

<a id="gcp-terraform-cloud"></a>

## Terraform Cloud / Github Actions

[Terraform Cloud](https://terraform.cloud) is used as the remote backend. [Github Actions](https://github.com/features/actions) perform tasks to deploy and undeploy the GCP infrastructure.

Configure Terraform Cloud workspaces:

```shell
❯ make terraform-apply SERVICE=terraform/gcp/terraform-cloud ENV=main
```

<img src="/img/gcp/portefaix-gcp-deploy.png" alt="Portefaix GCP deployment" class="mt-3 mb-3 rounded">

<img src="/img/gcp/portefaix-gcp-undeploy.png" alt="Portefaix GCP deletion" class="mt-3 mb-3 rounded">

## Authentication and authorization

This section shows the how to setup Portefaix with authentication and authorization support in
Google Cloud Platform (GCP).

### Cloud IAP

To enable Cloud IAP, you need first to configure the OAuth consent screen. If you still haven't configured the OAuth
consent screen, you can do so with an email address and product name.
See https://support.google.com/cloud/answer/6158849?hl=en#zippy=%2Cuser-consent

Then creates the [Oauth credentials](https://console.cloud.google.com/apis/credentials).
Select the `OAuth client ID` from the Create credentials drop-down list and then select `web application` from the
application type. Next, add a name for your OAuth client ID and click `create`.

### Gcloud

```shell
❯ . ./portefaix.sh gcp
[ Portefaix ]
Setup credentials
Done
```

### Kubernetes

```shell
❯ make -f hack/build/azure.mk gck-kube-credentials CLOUD=gcp ENV=dev
```

```shell
❯ kubectl get nodes
NAME                                                  STATUS   ROLES    AGE     VERSION
gke-xxxxxxxxxx-cluster-g-core-5d5d62be-tf15   Ready    <none>   7h37m   v1.18.10-gke.601
```


<a id="gcp-gitops"></a>

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)

## Inspec

[inspec](http://inspec.io/) is used to check infrastructure:

```shell
❯ make -f hack/build/gcp.mk inspec-debug
Test infrastructure

 ────────────────────────────── Platform Details ──────────────────────────────

Name:      gcp
Families:  cloud, api
Release:   google-api-client-v0.34.1
```

Execute tests:

```shell
❯ make -f hack/build/gcp.mk inspec-test SERVICE=iac/gcp/<SERVICE> ENV=dev
```

You could upload JSON results file to [Heimdall Lite](https://heimdall-lite.mitre.org/) to display ressults

## CIS Kubernetes Benchmark

```shell
❯ make -f hack/build/gcp.mk inspec-gcp-kubernetes ENV=dev
```

## GCP CIS

You could perform tests accoring the [GCP CIS](https://opensource.googleblog.com/2020/08/assess-security-of-cloud-deployments.html):

```shell
❯ make -f hack/build/gcp.mk inspec-cis ENV=dev
```

## VPC

```shell
❯ make -f hack/build/gcp.mk inspec-test SERVICE=iac/gcp/vpc ENV=dev
```

<img src="/img/gcp/inspec-gcp-vpc.png"
 alt="VPC"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `vpc-1` | Ensure default network is deleted |
| `vpc-2` | Ensure network is correctly configure |

## GKE

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/gke ENV=dev
```

<img src="/img/gcp/inspec-gcp-gke.png"
 alt="GKE"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `gke-1` | Stackdriver Logging and Monitoring is configured |
| `gke-2` | Basic Authentication is disabled |
| `gke-3` | Ensure GKE Nodes are not public |
| `gke-4` | Ensure the GKE Control Plane is not public |
| `gke-5` | Ensure the Network Policy managed addon is enabled |
| `gke-6` | Ensure OAuth Access Scopes and dedicated Service Accounts for node pools |
| `gke-7` | Ensure GKE Node Pools should use the COS or COS_CONTAINERD Operating System |
| `gke-8` | GKE Workload Identity should be enabled on all node pools |
| `gke-9` | GKE Shielded Nodes should be enabled on all NodePools |
| `gke-10` | Ensure instances have labels |
| `gke-11` | Ensure instances have tags |

## Sops

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/sops ENV=dev
```

<img src="/img/gcp/inspec-gcp-sops.png"
 alt="Sops"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `sops-1` | Ensure service account and IAM binding exists |
| `sops-2` | Ensure that Kms key exist |

## Observability

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/observability ENV=dev
```

<img src="/img/gcp/inspec-gcp-observability.png"
 alt="Observability"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `grafana-1` | Ensure service account and IAM binding exists |
| `prometheus-1` | Ensure service account and IAM binding exists |
| `thanos-1` | Ensure service account and IAM binding exists |
| `thanos-2` | Ensure that bucket exists and labels correcly set |
| `thanos-3` | Ensure that Kms key exist |
| `loki-1` | Ensure service account and IAM binding exists |
| `loki-2` | Ensure that bucket exists and labels correcly set |
| `loki-3` | Ensure that Kms key exist |
| `tempo-1` | Ensure service account and IAM binding exists |
| `tempo-2` | Ensure that bucket exists and labels correcly set |
| `tempo-3` | Ensure that Kms key exist |

## Velero

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/velero ENV=dev
```

<img src="/img/gcp/inspec-gcp-velero.png"
 alt="Velero"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `velero-1` | Ensure service account and IAM binding exists |
| `velero-2` | Ensure that bucket exists and labels correcly set |
| `velero-3` | Ensure that Kms key exist |

## Vector

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/vector ENV=dev
```

<img src="/img/gcp/inspec-gcp-vector.png"
 alt="Vector"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `vector-1` | Ensure service account and IAM binding exists |
| `vector-2` | Ensure that bucket exists and labels correcly set |
| `vector-3` | Ensure that Kms key exist |

## External-DNS

```shell
❯ make -f hack/build/gcp.mk gcp-inspec-test SERVICE=iac/gcp/external-dns ENV=dev
```

<img src="/img/gcp/inspec-gcp-external-dns.png"
 alt="External-DNS"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `external_dns-1` | Ensure service account and IAM binding exists |
