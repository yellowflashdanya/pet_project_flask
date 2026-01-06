# Flask counter with Redis & CI pipeline 🚀

[![CI to Docker Hub](https://github.com/yellowflashdanya/devops_practice/actions/workflows/main.yml/badge.svg)](https://github.com/yellowflashdanya/devops_practice/actions)

This is an educational project that demonstrates the Python app in action with Redis database, automatic with Docker-Compose & CI pipeline

## Stack:
* **Language:** Python 3.9 (Flask)
* **Database:** Redis (Alpine version)
* **Conteinerization:** Docker + Docker Compose
* **CI:** GitHub Actions (Automated CI)

## Project Architecture and Features:

* **web**: Flask-app, which processes HTTP-requests and interacts with Redis;
* **redis**: Storage that contains data with type key-value and for saving the counter of visiting;
* **containerization**: The app is totally containerized with Docker-containers;
* **automated ci pipeline**: Configured pipeline, which automatically logs in Docker Hub, build image and push it after every branch update `main`.

## 🚀 How to run locally:

To run this project locally, two things you need to be installed - **Docker** and **Docker Compose**.

1. Clone the repo:
  ```bash
  git clone https://github.com/yellowflashdanya/devops_practice.git
  cd devops_practice
  ```

2. Run project by 1 command:
  ```bash
  docker-compose up --build
  ```

3. Open in browser:
  http://localhost:5001

## 📦 Docker Registry
My builded image automatically publish at Docker Hub. You can find it via link or download using ONE command:

* **Link for the repository**: [hub.docker.com/r/danyakube/counter-app](https://hub.docker.com/r/danyakube/counter-app)
* **Command to download the image**:
```bash
docker pull danyakube/counter-app:latest
```

