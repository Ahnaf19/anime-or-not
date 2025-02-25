# Anime-Or-Not

Anime-Or-Not (AoN) is an API that exposes prediction endpoint of an deep learning leveraged image classifier, detecting if its either anime or cartoon.

## Project Overview

Although Anime and Cartoon both are a form of animation and look almost the same, there are some structural differences between the two that can be exploited to classify them.

**Created an image classification API that leverages a deep learning model to classify images as either anime or cartoon. The API exposes a prediction endpoint to take an image as input and return a classification label with prediction probability.**

> Developed on: python 3.10.16

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Docker Build & Run

To build and run the application using Docker, follow these steps:

### Prerequisites

Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

#### Build Docker Image

> [!IMPORTANT]
> `Docker Daemon` or `Docker Desktop` must be running while building Docker Image.

Navigate to the root directory of the repo where the `Dockerfile` is located and run the following command to build the Docker image:

```sh
docker build -t aon:latest .
```

#### Run Docker Container

After building the Docker image, you can run it using the following command:

```sh
docker run -dp 8000:8000 aon:latest
```

This will start the application in a Docker container. The application can be accessed at `http://localhost:8000` e.g. `127.0.0.1:8000`

> [!NOTE]
> `-dp` (`-d` & `-p`) tag runs the container in detached mode (in the background, terminal is available to use right away) and container port `8000` is mapped to local port `8000`.

Go to `http://localhost:8000/docs` and try the end points. `/model/predict` takes in an image and returns prediction.

#### Stopping the Container

To stop the running container, first find the container ID using:

```sh
docker ps
```

Then stop the container using:

```sh
docker stop <container_id>
```

## Run locally with Uvicorn

- [optional but recommended] create a venv and activate it
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- start Uvicorn server:
  ```sh
  uvicorn app.main:app --reload
  ```
- `cntrl+c` to break the server.

## Milestones

- [x] develop ML prediction pipeline 🤖
- [x] Expose the prediction pipeline with api end points 🌐
- [ ] unit testing 🧪
- [ ] write comprehensive readme 📖✨
- [ ] write readme-dev 📖
- [x] dockerize the repo 🐳
- [x] Code Auto-formatting & Linting with Pre-commit (check-yaml, end-of-file-fixer, trailing-whitespace, black, isort, mypy) 🎨
- [ ] add GitHub Action for format checks ✅
- [ ] Study deploy requirement and deploy! 🚀
