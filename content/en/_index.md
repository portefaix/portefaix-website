---
title: Portefaix
description: >-
  bla bla bla
show_banner: true
---

{{< blocks/cover title="Welcome to Portefaix" image_anchor="top" height="full" >}}

<!-- prettier-ignore -->
<!-- ![OpenTelemetry](/img/logos/opentelemetry-horizontal-color.svg)
{.otel-logo} -->

<a class="btn btn-lg btn-primary me-3 mb-4" href="/docs/">
  Learn More <i class="fas fa-arrow-alt-circle-right ms-2"></i>
</a>
<a class="btn btn-lg btn-primary me-3 mb-4" href="/docs/about/contributing/">
  Contribute <i class="fas fa-pencil ms-2"></i>
</a>
<a class="btn btn-lg btn-secondary me-3 mb-4" href="https://github.com/portefaix">
  Github project <i class="fab fa-github ms-2 "></i>
</a>
<p class="lead mt-5">A Kubernetes experience!</p>

{{< blocks/link-down color="info" >}}
{{< /blocks/cover >}}


{{% blocks/lead color="white" %}}
<strong>What is Portefaix?</strong>

An Open Source project to deploy applications from the Kubernetes ecosystem in different Cloud Providers.
{{% /blocks/lead %}}


{{% blocks/section color="dark" type="row" %}}
{{% blocks/feature icon="fas fa-wrench" title="Infrastructure As Code" url="./docs/started/getting-started/#installing-portefaix-on-a-public-cloud" %}}
Manage the infrastructure using Cloud Native tools: Terraform, Kustomize, Helm, ...
{{% /blocks/feature %}}


{{% blocks/feature icon="fas fa-file-code" title="Gitops" url="fa-file-code" %}}
A Git repository that always contains declarative descriptions of the infrastructure, and an
automated process to make the environment match the described state in the repository.
{{% /blocks/feature %}}


{{% blocks/feature icon="fas fa-chart-area" title="Observability" url="./docs/kubernetes/monitoring" %}}
Open Source components for monitoring, logging and tracing.
{{% /blocks/feature %}}


{{% /blocks/section %}}


{{% blocks/section color="white" %}}
{.h1 .text-center}
<div class="col">
	<h2 class="text-center pb-3">Cloud Providers</h2>
	<p class="text-center showcase">
		<a href="https://cloud.google.com/"><img alt="Google Cloud" width="100" src="google-cloud.svg" /></a>
		<a href="https://aws.amazon.com/"><img alt="AWS" width="100" src="aws.svg" /></a>
		<a href="https://azure.microsoft.com/"><img alt="Azure" width="100" src="azure-icon.svg" /></a>
		<a href="https://www.scaleway.com/"><img alt="altavr" width="100" src="scaleway-icon.svg" /></a>
		<a href="https://www.digitalocean.com/"><img alt="Embark Studios" width="100" src="digitalocean-icon.svg" /></a>
		<a href="https://www.alibabacloud.com/"><img alt="accelbyte" width="100" src="alibabacloud-icon.svg" /></a>
	</p>
</div>
{{% /blocks/section %}}


<!-- {{% blocks/section color="white" type="row" %}}

{{% blocks/feature icon="fab fa-app-store-ios" title="Download **from AppStore**" %}}
Get the Goldydocs app!
{{% /blocks/feature %}}

{{% blocks/feature icon="fab fa-github" title="Contributions welcome!"
    url="[https://github.com/portefaix/portefaix](https://github.com/portefaix/portefaix-website)" %}}
We do a [Pull Request](https://github.com/portefaix/portefaix-website/pulls)
contributions workflow on **GitHub**. New users are always welcome!
{{% /blocks/feature %}}

{{% blocks/feature icon="fab fa-twitter" title="Follow us on Twitter!"
    url="https://twitter.com/GoHugoIO" %}}
For announcement of latest features etc.
{{% /blocks/feature %}}

{{% /blocks/section %}} -->

<!-- 
{{% blocks/section %}}
This is the another section
{.h1 .text-center}
{{% /blocks/section %}} -->