# AWS SageMaker and Cloud MLOps

This document explains how the GradeMind project can be transitioned from a local deployment to a cloud-based MLOps architecture using Amazon Web Services (AWS).

## Cloud Architecture Concept

Moving to the cloud provides scalability, managed services, and easier integration with CI/CD pipelines.

A typical cloud architecture for GradeMind would look like this:

Student → Cloud Web Application (EC2 / ECS / App Runner)
   ↓
ML Prediction API (API Gateway + AWS Lambda)
   ↓
Trained Model (Served via SageMaker Endpoint)
   ↓
Cloud Storage (Amazon S3)

## Cloud Storage (Amazon S3)
Currently, data and models are stored locally. In the cloud:
- **Dataset Storage**: The `data/students.csv` file would be uploaded to an S3 bucket (e.g., `s3://grademind-data/raw/`).
- **Model Storage**: The trained `model.joblib` file would be saved to S3 (e.g., `s3://grademind-models/prod/`).
- **Security**: AWS IAM (Identity and Access Management) roles would be used to securely grant the Flask application permission to read the model from S3, avoiding hardcoded credentials.

## AWS SageMaker MLOps Process
Amazon SageMaker is a fully managed service that provides developers and data scientists with the ability to build, train, and deploy ML models quickly.

1. **Dataset**: Training data is pulled directly from Amazon S3.
2. **SageMaker Training**: We would create a SageMaker Training Job, providing our `src/train.py` script. SageMaker provisions the necessary compute instances, runs the training script, and automatically tracks metrics (similar to local MLflow).
3. **Model Artifact**: After training, SageMaker saves the model artifact back to S3.
4. **SageMaker Endpoint**: We deploy the trained model to a SageMaker Endpoint. This creates a highly available, scalable REST API for our model.
5. **Prediction**: The Flask application (running on EC2 or ECS) sends user input to the SageMaker Endpoint to get predictions, instead of loading the model locally.
6. **Monitoring**: SageMaker Model Monitor continuously tracks the predictions and input data for data drift and anomalies.

## Cloud CI/CD for ML
The GitHub Actions pipeline (`.github/workflows/ci.yml`) can be extended to deploy to the cloud:
- After successful tests, the pipeline can trigger a SageMaker Training Job.
- If the new model performs better than the old one, the pipeline can automatically update the SageMaker Endpoint.
- The Docker image built in the pipeline can be pushed to Amazon ECR (Elastic Container Registry) and deployed to Amazon ECS (Elastic Container Service).
