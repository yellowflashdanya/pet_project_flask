# Flask counter with Redis & K8s Resilience & IaC 🚀

[![CI to Docker Hub](https://github.com/yellowflashdanya/pet_project_flask/actions/workflows/main.yml/badge.svg)](https://github.com/yellowflashdanya/pet_project_flask/actions)

Educational DevOps project demonstrating the evolution from simple containerization to a production-ready **Kubernetes** orchestration with self-healing capabilities.

## Stack:
* **Language:** Python 3.9 (Flask)
* **Database:** Redis (Alpine)
* **Orchestration:** **Kubernetes (Minikube)**
* **Infrastructure:** Terraform (IaC), Docker Compose
* **CI/CD:** GitHub Actions
* **Monitoring:** In process... (Prometheus & Grafana)

## Key features:

* **Kubernetes Orchestration:** Migrated from Compose to K8s with **Deployments** and **Service**.
* **Self-healing & Resilience:** Configured to automatically restore pods upon failure.
* **Infrastructure as Code:** Environment managed via **Terraform**.
* **Resilience:** Configured **Healthchecks** to ensure the web app only starts when Redis is ready.
* **Automated CI:** Every push to `main` branch triggers an automated build and push to DockerHub.

## 🚀 How to Run:

### Option A: Running on Kubernetes (Recommended):
1. Start your local cluster:
   ```bash
   minikube start
   ```

2. Apply all manifests:
   ```bash
   kubectl apply -f k8s/
   ```

3. Open the app in your browser:
   ```bash
   minikube service flask-service
   ```

### Option B: Using Terraform (IaC Demo):

1. Clone the repo & Initialize Terraform:
  ```bash
  git clone https://github.com/yellowflashdanya/pet_project_flask.gitpet_project_flask.git
  cd pet_project_flask
  terraform init
  ```

2. Apply infrastructure:
  ```bash
  terraform apply
  ```

### Option C: Simple Docker Compose:

1. ```bash
   docker-compose up --build
   ```

## Architecture Details:

* **K8s Networking:** Uses internal DNS `redis-service` for inter-pod communication
* **Port mapping:**
* `localhost:5001` - **Docker Compose**
* `localhost:5003` - **Terraform**
* `localhost:30001` - **Kubernetes (NodePort)**
* **Registry:** Images are stored at [hub.docker.com/r/danyakube/counter-app](https://hub.docker.com/r/danyakube/counter-app)
* **Command to download the image**:
```bash
docker pull danyakube/counter-app:latest
```

