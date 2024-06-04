+++
title = "Getting Started"
description = "Getting started"
weight = 20

+++

## Installation

<a id="installation-guides"></a>
## Installing Portefaix

There are various ways to install Portefaix. Choose one of the following options
to suit your environment (public cloud, existing Kubernetes cluster, or
a single-node cluster which you can use on a desktop or server or in the cloud).

<a id="cloud"></a>
### Installing Portefaix on a public cloud

Choose the Portefaix deployment guide for your chosen cloud:

* To use Portefaix on Google Kubernetes Engine (GKE), follow the [GKE deployment guide](/docs/gcp/deploy/).
* To use Portefaix on Amazon Elastic Kubernetes Service (EKS), follow the [EKS deployment guide](/docs/aws/deploy/).
* To use Portefaix on Microsoft Azure Kubernetes Service (AKS), follow the [AKS deployment guide](/docs/azure/deploy/).
* To use Portefaix on AlibabaCloud Container Service for Kubernetes (ACK), follow the [ACK deployment guide](/docs/alicloud/deploy).
* To use Portefaix as your Homelab, follow the [Raspberry PI Homelab](/docs/homelab/deploy).

<!-- * To use Portefaix on IBM Cloud (IKS),
    follow the [IKS deployment guide](/docs/ibm/). -->

## Components

### Infrastructure management

- [Terraform](https://github.com/hashicorp/terraform): Bootstraps and manages the cloud provider infrastructure.
- [Crossplane](https://crossplane.io): Kubernetes-native infrastructure management.

### Cluster management

- [Argo CD](https://github.com/argoproj/argo-cd): Reconciles kubernetes clusters with this repository.
- [Kyverno](https://kyverno.io): Policy engine supporting validate, mutate, generate, and cleanup rules.
- [Renovate](https://github.com/renovatebot/renovate): Automatic updates for applications via pull requests.

### Secrets

- [External Secrets](https://external-secrets.io): Synchronizes secrets from Doppler into Kubernetes.
- [AKeyless](https://console.akeyless.io): A secrets management platform.

### Networking

- [Cilium](https://cilium.io): eBPF-based CNI & service mesh.
- [Cert Manager](https://cert-manager.io): Automatic Let's Encrypt certificates.

### Security

- [Authentik](https://goauthentik.io): Identity Provider.
- [Tetragon](https://tetragon.io/): eBPF-based security observability and runtime enforcement.
- [Trivy](https://aquasecurity.github.io/trivy): Kubernetes and container vulnerability scanner.

### Observability

- [Grafana](https://grafana.com): Visualization platform.
- [Prometheus](https://prometheus.io): Monitoring system.
- [Loki](https://grafana.com/oss/loki/): Log aggregation system.
- [Tempo](https://grafana.com/oss/tempo/): High-scale distributed tracing backend
- [Mimir](https://grafana.com/oss/mimir/): Horizontally scalable TSDB for long-term storage for Prometheus
- [Alloy](https://grafana.com/oss/alloy/): The OpenTelemetry Distribution from Grafana

### Storage

*TODO*

## Troubleshooting

See the [Portefaix troubleshooting guide](/docs/other-guides/troubleshooting/).
