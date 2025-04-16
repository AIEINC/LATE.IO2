resource "digitalocean_kubernetes_cluster" "agentic" {
  name    = "agentic-cluster"
  region  = "nyc1"
  version = "1.29.0-do.0"
  node_pool {
    name       = "agentic-nodes"
    size       = "s-2vcpu-4gb"
    node_count = 3
  }
}

resource "helm_release" "agentic" {
  name       = "agentic"
  repository = "./charts/agentic"
  chart      = "agentic-deployment"
  namespace  = "agentic"
  depends_on = [digitalocean_kubernetes_cluster.agentic]
}
