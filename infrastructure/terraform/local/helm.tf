resource "helm_release" "frontend" {

  name       = "frontend"
  namespace  = "frontend"

  chart = "../../../helm/frontend"
}

resource "helm_release" "backend" {

  name       = "backend"
  namespace  = "backend"

  chart = "../../../helm/backend"
}