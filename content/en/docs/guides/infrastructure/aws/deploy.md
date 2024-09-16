---
type: docs
title: "Install on Amazon Web Services"
description: "Running Portefaix on Amazon Web Services"
weight: 50
categories: "HowTo"
tags: ["AWS"]
---

<a id="aws"></a>

## Setup

Creates an [AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html), and enable Service Control Policies in AWS organizations.

Now that we’ve created an organization, you’ll notice that all the policies are disabled by default.

There you need to enable AWS Service Control Policies in the AWS console by clicking on the button Enable service control policies. Do the same action for the AWS Tag Policies.

Navigate to Personal Health Dashboard service in the console. On the left side panel, expand Organizational view and choose configurations. Then, enable organizational view for AWS Health

Create an [admin user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html), and configure [account alias for IAM Users access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html)

Then [API Keys](https://console.aws.amazon.com/iam/home?#/security_credentials).

Configure Portefaix environment file `${HOME}/.config/portefaix/portefaix.sh`:

```shell
HOME_IP=$(curl -s http://ifconfig.me)
SLACK_WEBHOOK_NOTIFS="https://hooks.slack.com/services/xxx/xxx"

# AWS
function setup_aws() {
    export AWS_ACCESS_KEY_ID="....."
    export AWS_SECRET_ACCESS_KEY="....."
    export AWS_DEFAULT_REGION="..."
    export AWS_REGION="...."
    # For Terraform Cloud
    export TF_VAR_access_key="${AWS_ACCESS_KEY_ID}"
    export TF_VAR_secret_key="${AWS_SECRET_ACCESS_KEY}"
    export TF_VAR_slack_webhook_url="${SLACK_WEBHOOK_NOTIFS}"
    export TF_VAR_org_email="xxxxxx"    # for Root Account
    export TF_VAR_org_email_domain="gmail.com"
    export TF_VAR_org_admin_username="xxxxxx"
    export TF_VAR_admin_ipv4="[\"${HOME_IP}/32\"]" # for WAF
}
```

Load environment :

```shell
❯ . ./portefaix.sh aws
```

## Storage for Terraform

Create a S3 bucket for Terraform states:

```shell
❯ make -f hack/build/aws.mk aws-s3-bucket ENV=staging
```

Create a DynamoDB table :

```shell
❯ make -f hack/build/aws.mk aws-dynamodb-create-table ENV=staging
```

## AWS Organization Units and Accounts

Configure the AWS Organization:

```shell
❯ make terraform-apply SERVICE=terraform/aws/root ENV=main
```

<img src="/img/aws/aws_organization.png" alt="
Portefaix AWS organization" class="mt-3 mb-3 rounded">

<a id="aws-terraform-cloud"></a>

## Terraform Cloud / Github Actions

* [Terraform Cloud](https://terraform.cloud) is used as the remote backend.
* [Github Actions](https://github.com/features/actions) perform tasks to deploy or undeploy the AWS infrastructure.

```shell
❯ make terraform-apply SERVICE=terraform/aws/terraform-cloud ENV=main
```

<img src="/img/aws/portefaix-aws-deploy.png" alt="Portefaix AWS deployment" class="mt-3 mb-3 rounded">

<img src="/img/aws/portefaix-aws-undeploy.png" alt="Portefaix Azure deletion" class="mt-3 mb-3 rounded">

<a id="aws-gitops"></a>

## Authentication

### Kubernetes

Configure the AWS provider

```shell
❯ . ./portefaix.sh aws
[ Portefaix ]
Setup credentials
Done
```

Perform an AWS authentication:

```shell
❯ make -f hack/build/aws.mk ENV=staging aws-admin
source ./hack/scripts/aws-auth.sh xxxxxx Administrator portefaix-staging-eks eu-west-1

❯ source ./hack/scripts/aws-auth.sh xxxxxxx Administrator portefaix-staging-eks eu-west-1
```

Update Kubernetes configuration file:

```shell
❯ make -f hack/build/aws.mk ENV=staging aws-kube-credentials

❯ kubectl get nodes
NAME                                        STATUS   ROLES    AGE   VERSION
ip-10-0-13-85.eu-west-1.compute.internal    Ready    <none>   81m   v1.23.9-eks-ba74326
ip-10-0-29-115.eu-west-1.compute.internal   Ready    <none>   81m   v1.23.9-eks-ba74326
ip-10-0-60-137.eu-west-1.compute.internal   Ready    <none>   81m   v1.23.9-eks-ba74326
ip-10-0-70-76.eu-west-1.compute.internal    Ready    <none>   81m   v1.23.9-eks-ba74326
```

### Bastion

You would use the [AWS System Manager plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) to connect to EC2 and EKS instances:

```shell
❯ aws ec2 describe-instances --output table
-------------------
|DescribeInstances|
+-----------------+

❯ aws ssm start-session --target i-019042b3847f5c81f
Starting session with SessionId: portefaix-admin-031b2ba6d981142b0
```

## Gitops for Kubernetes

Next: [Gitops](/docs/gitops)

## Inspec

[Inspec](http://inspec.io/) is used to check infrastructure.

Check:

```shell
❯ make -f hack/build/aws.mk inspec-debug
Test infrastructure

 ────────────────────────────── Platform Details ──────────────────────────────

Name:      aws
Families:  cloud, api
Release:   train-aws: v0.1.15, aws-sdk-core: v3.94.0
```

Execute tests:

```shell
❯ make -f hack/build/aws.mk inspec-test SERVICE=iac/aws/<SERVICE> ENV=staging
```

You could upload JSON results file to [Heimdall Lite](https://heimdall-lite.mitre.org/) to display ressults

### CIS AWS Foundations Benchmark

You could perform tests according to the [CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-cis.html):

```shell
❯ make -f hack/build/aws.mk inspec-aws-cis ENV=staging
```

### CIS Kubernetes Benchmark

```shell
❯ make -f hack/build/aws.mk inspec-aws-kubernetes ENV=staging
```

### VPC

```shell
❯ make -f hack/build/aws.mk inspec-test SERVICE=iac/aws/vpc ENV=staging
```

<img src="/img/aws/inspec-aws-vpc.png"
 alt="VPC"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `vpc-1` | Ensure that VPC exist and tags correcly set |
| `vpc-2` | Ensure that VPC have an Internet Gateway |
| `vpc-3` | Check AWS Security Groups does not have undesirable rules |
| `vpc-4` | Ensure that VPC Subnets exists |

### EKS

```shell
❯ make -f hack/build/aws.mk inspec-test SERVICE=iac/aws/eks ENV=staging
```

<img src="/img/aws/inspec-aws-eks.png"
 alt="EKS"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `eks-1` | Ensure the AWS EKS Cluster is running a minimal version |
| `eks-2` | Ensure the AWS EKS Cluster control plane has audit logs enabled |
| `eks-3` | Ensure the AWS EKS Cluster is not public |
| `eks-4` | Ensure the AWS EKS Cluster has application secrets encryption enabled |
| `eks-5` | Ensure AWS EKS Cluster Subnets are specific |
| `eks-6` | Ensure AWS EKS Cluster Nodegroups do not allow remote access from all IPs

### Observability

```shell
❯ make -f hack/build/aws.mk inspec-test SERVICE=iac/aws/observability ENV=staging
```

<img src="/img/aws/inspec-aws-observability.png"
 alt="Observability"
 class="mt-3 mb-3 border border-info rounded">

| Code | Description|
|---|---|
| `grafana-1` | Ensure IAM roles and policies exists |
| `prometheus-1` | Ensure IAM roles and policies exists |
| `thanos-1` | Ensure that S3 bucket exist and tags correcly set |
| `thanos-2` | Ensure that S3 log bucket exist and tags correcly set |
| `thanos-3` | Ensure that Kms key exist |
| `thanos-4` | Ensure IAM roles and policies exists |
| `loki-1` | Ensure that S3 bucket exist and tags correcly set |
| `loki-2` | Ensure that S3 log bucket exist and tags correcly set |
| `loki-3` | Ensure that Kms key exist |
| `loki-4` | Ensure IAM roles and policies exists |
| `tempo-1` | Ensure that S3 bucket exist and tags correcly set |
| `tempo-2` | Ensure that S3 log bucket exist and tags correcly set |
| `tempo-3` | Ensure that Kms key exist |
| `tempo-4` | Ensure IAM roles and policies exists |

