terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_network" "app_network" {
  name = "my_app_network"
}

resource "docker_image" "redis_image" {
  name = "redis:alpine"
}

resource "docker_image" "flask_image" {
  name = "danyakube/counter-app:latest"
}


resource "docker_container" "redis_container" {
  image = docker_image.redis_image.image_id
  name  = "my_redis_from_terraform"

  networks_advanced {
    name = docker_network.app_network.name
  }
}

resource "docker_container" "flask_app" {
  name  = "flask-app-tf"
  image = docker_image.flask_image.image_id

  ports {
    internal = 5000
    external = 5003
  }

  env = [
    "REDIS_HOST=my_redis_from_terraform"
  ]

  networks_advanced {
    name = docker_network.app_network.name
  }
}