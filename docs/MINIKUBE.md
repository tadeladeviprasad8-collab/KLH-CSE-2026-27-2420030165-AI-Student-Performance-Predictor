# Minikube Local Deployment

This guide explains how to deploy the GradeMind application locally using Minikube.
Minikube sets up a local Kubernetes cluster on your machine.

## Prerequisites
1. Docker Desktop (or another container runtime) installed and running.
2. Minikube installed.
3. `kubectl` (Kubernetes command-line tool) installed.

## Steps

### 1. Start Minikube
Start the local Kubernetes cluster:
```bash
minikube start
```
*This provisions and manages the local Kubernetes cluster.*

### 2. Point Docker to Minikube's Environment
To allow Minikube to use the Docker images built locally (instead of trying to pull them from a registry like Docker Hub), configure your shell:
```bash
# On Linux/macOS
eval $(minikube docker-env)

# On Windows (PowerShell)
& minikube -p minikube docker-env | Invoke-Expression
```

### 3. Build the Docker Image
Build the GradeMind image so it's available inside the Minikube environment:
```bash
docker build -t grademind:latest .
```

### 4. Deploy to Kubernetes
Apply the configuration files located in the `k8s/` directory.

The Deployment (`deployment.yaml`) manages the pods running our Flask app.
The Service (`service.yaml`) exposes the application so we can access it.

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 5. Verify the Deployment
Check the status of the pods (the instances of your application):
```bash
kubectl get pods
```
*You should see two pods (as specified in `replicas: 2`) with a status of 'Running'.*

Check the status of the service:
```bash
kubectl get services
```

### 6. Access the Application
Because we used a `NodePort` service, we can ask Minikube to provide the URL to access the application:
```bash
minikube service grademind-service
```
*This command will open the GradeMind application in your default web browser.*

### 7. Stop Minikube
When you are done testing, you can stop the cluster to free up resources:
```bash
minikube stop
```
