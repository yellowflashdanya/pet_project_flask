# Flask counter with Redis 🚀

This is an educational project that shows, which demonstrates the Python-app in action with Redis database, automatic with Docker-Compose

## Stack:
* **Language:** Python 3.9 (Flask)
* **Database:** Redis (Alpine version)
* **Conteinerization:** Docker + Docker Compose
* **CI/CD:** GitHub Actions (in process...)

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

## Project Architecture:

* **web**: Flask-app, which processes HTTP-requests and interacts with Redis
* **redis**: Storage that contains data with type key-value and for saving the counter of visiting