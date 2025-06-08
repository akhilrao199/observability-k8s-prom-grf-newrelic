Observability - Kubernetes - Prometheus - New Relic

Observability plays a key role in how we build, operate, and trust modern systems.
 It’s not just about collecting data — it’s about making systems understandable when things break, scale, or behave unexpectedly.
 
Goal: To explore this end-to-end, I recently set up a complete monitoring solution for a local Kubernetes cluster using Prometheus, Grafana, and New Relic. The goal? Go beyond just spinning up dashboards — and focus on how each tool contributes to real observability.

Tools I used: Minikube, kubernetes, helm, prometheus, grafana, Newrelic, python

What I focused on:
Complete observability stack for a local Kubernetes cluster — integrating Prometheus, Grafana, and New Relic.
- making sense of the cluster state, setting up alerting on pod events, and pulling in custom metrics.
- Setting up Prometheus & Grafana via Helm with NodePort exposure
- Exploring pre-built dashboards in Grafana(3662)
- Exposing kube-state-metrics for in-depth cluster health
- Integrating the same cluster with New Relic, setting up and validating pod restart alerts with live scenario
- Exploring what different monitoring tools offers to software lifecycle


-📄 I’ve documented everything step-by-step in a PDF (attached) — including commands, configs, and key takeaways.
- If you’re diving into Kubernetes monitoring and want a hands-on guide that skips the fluff, you might find it helpful.


go through the pdf in the repository for end-to-end step-by-step setup
