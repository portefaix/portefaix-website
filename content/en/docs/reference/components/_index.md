---
type: docs
title: "Components"
linkTitle: "Components"
description: "The components used by Portefaix"
weight: 10
---

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

- [Falco](https://falco.org): The Cloud Native Runtime Security
- [Authentik](https://goauthentik.io): Identity Provider.
- [Trivy](https://aquasecurity.github.io/trivy): Kubernetes and container vulnerability scanner.
- [Tetragon](https://tetragon.io/): eBPF-based security observability and runtime enforcement.

### Observability

- [Grafana](https://grafana.com): Visualization platform.
- [Prometheus](https://prometheus.io): Monitoring system.
- [Loki](https://grafana.com/oss/loki/): Log aggregation system.
- [Tempo](https://grafana.com/oss/tempo/): High-scale distributed tracing backend
- [Mimir](https://grafana.com/oss/mimir/): Horizontally scalable TSDB for long-term storage for Prometheus
- [Alloy](https://grafana.com/oss/alloy/): The OpenTelemetry Distribution from Grafana

### Storage