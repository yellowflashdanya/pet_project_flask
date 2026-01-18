# Flask counter with Redis & HealthChecks & Infrastructure as Code (Terraform) 🚀

[![CI to Docker Hub](https://github.com/yellowflashdanya/pet_project_flask/actions/workflows/main.yml/badge.svg)](https://github.com/yellowflashdanya/pet_project_flask/actions)

Educational DevOps project demonstrating a production-ready approach to containerization and infrastructure management.

## Stack:
* **Language:** Python 3.9 (Flask)
* **Database:** Redis (Alpine)
* **Infrastructure:** Terraform (IaC), Docker Compose
* **CI/CD:** GitHub Actions
* **Monitoring:** In process...

## Key features:

* **Infrastructure as Code (IaC):** Full environment setup using **Terraform**, including isolated network and container lifecycle.
* **Resilience:** Configured **Healthchecks** to ensure the web app only starts when Redis is ready.
* **Persistence:** Docker Volumes are used to prevent data loss after container restarts.
* **Automated CI:** Every push to `main` branch triggers an automated build and push to DockerHub.

## 🚀 How to Run:

### Option A: Using Terraform (IaC Demo):

1. Clone the repo & Initialize Terraform:
  ```bash
  git clone [https://github.com/yellowflashdanya/pet_project_flask.git](https://github.com/yellowflashdanya/pet_project_flask.git)
  cd pet_project_flask
  terraform init
  ```

2. Apply infrastructure:
  ```bash
  terraform apply
  ```

### Option B: Using Docker Compose:

1. docker-compose up --build

## Architecture Details:

* **Network:** Isolated bridge network for secure inter-container communication;
* **Port mapping:** `localhost:5001` (Docker Compose) / `localhost:5003` (Terraform)
* **Registry:** Images are stored at [hub.docker.com/r/danyakube/counter-app](https://hub.docker.com/r/danyakube/counter-app)
* **Command to download the image**:
```bash
docker pull danyakube/counter-app:latest
```

