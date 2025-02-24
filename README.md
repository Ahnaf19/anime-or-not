# Anime-Or-Not

Anime-Or-Not (AoN) is an API that exposes prediction endpoint of an deep learning leveraged image classifier, detecting if its either anime or cartoon.

## Project Overview

Although Anime and Cartoon both are a form of animation and look almost the same, there are some structural differences between the two that can be exploited to classify them.

**Create an image classification API that leverages a deep learning model to classify images as either anime or cartoon. The API will expose a prediction endpoint to take an image as input and return a classification label.**

> Being developed on: python 3.10.16

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Deliverables

- Trained DL model (`.pth` or `.onnx`).
- FastAPI-based prediction API.
- Fully documented API endpoints (Swagger UI).
- Performance metrics and model evaluation report.
- Deployment-ready containerized application.

## Milestones

- [x] develop ML prediction pipeline 🤖
- [x] Expose the prediction pipeline with api end points 🌐
- [ ] unit testing 🧪
- [ ] write comprehensive readme 📖✨
- [ ] dockerize the repo & add resources 🐳
- [x] Code Auto-formatting & Linting with Pre-commit (check-yaml, end-of-file-fixer, trailing-whitespace, black, isort, mypy) 🎨
- [ ] add GitHub Action for format checks ✅
- [ ] Study deploy requirement and deploy! 🚀
