# Viva Questions and Answers

This document provides a set of questions and simple answers to help a B.Tech student prepare for a viva examination based on the GradeMind project.

## CO1 - Software Engineering and Agile

**1. What is SDLC?**
SDLC stands for Software Development Life Cycle. It's a framework defining the steps involved in the development of software, including requirements gathering, design, implementation, testing, deployment, and maintenance.

**2. What is Agile?**
Agile is an iterative and incremental approach to software development. It focuses on flexibility, continuous improvement, and delivering working software quickly to respond to changing customer needs.

**3. What is Scrum?**
Scrum is an Agile framework used to manage and organize work. It involves roles (Product Owner, Scrum Master, Development Team), events (Sprints, Daily Scrums), and artifacts (Product Backlog, Sprint Backlog).

**4. What is a sprint?**
A sprint is a time-boxed period (e.g., 2 weeks) in Scrum during which a specific set of work must be completed and made ready for review.

**5. What is a user story?**
A user story is a simple description of a software feature written from the perspective of the end-user. Format: "As a [user], I want to [action], so that [benefit]."

**6. What is a backlog?**
A backlog is an ordered list of tasks, features, or bug fixes needed for a product. The Product Backlog contains everything for the product, while the Sprint Backlog contains tasks selected for the current sprint.

**7. What is velocity?**
Velocity is a metric used in Agile to measure the amount of work (usually in story points) a team can complete in a single sprint. It helps in planning future sprints.

## CO2 - DevOps Fundamentals

**8. What is DevOps?**
DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) to shorten the development lifecycle and continuously deliver high-quality software.

**9. What is CI/CD?**
CI/CD stands for Continuous Integration and Continuous Deployment (or Delivery). It's the automation of the software release process. CI automatically tests code changes, and CD automatically deploys the tested code.

**10. What is Git?**
Git is a distributed version control system used to track changes in source code during software development, allowing multiple developers to collaborate.

**11. What is Docker?**
Docker is a platform that uses containerization to package an application and all its dependencies together, ensuring it runs consistently across different environments.

**12. What is Kubernetes?**
Kubernetes is an open-source container orchestration system for automating the deployment, scaling, and management of containerized applications.

**13. What is Minikube?**
Minikube is a tool that allows you to run a single-node Kubernetes cluster locally on your machine for development and testing purposes.

**14. What is YAML?**
YAML (YAML Ain't Markup Language) is a human-readable data serialization language often used for configuration files (like in Kubernetes or GitHub Actions).

**15. What is Prometheus?**
Prometheus is an open-source systems monitoring and alerting toolkit. It collects metrics from applications and stores them as time-series data.

**16. What is Grafana?**
Grafana is an open-source analytics and visualization web application. It connects to data sources like Prometheus to create interactive dashboards and charts.

## CO3 - Security Operations (SecOps), DevSecOps and MLOps

**17. What is DevSecOps?**
DevSecOps is the integration of security practices into the DevOps process. It emphasizes that security is a shared responsibility from the start (Shift-Left), rather than a final check before release.

**18. What is SAST?**
SAST stands for Static Application Security Testing. It's a method of analyzing source code without executing it to find security vulnerabilities (e.g., using Bandit in Python).

**19. What is DAST?**
DAST stands for Dynamic Application Security Testing. It analyzes a running web application from the outside to find vulnerabilities like XSS or SQL injection (e.g., using OWASP ZAP).

**20. What is SonarQube?**
SonarQube is a tool for continuous inspection of code quality. It performs automatic reviews to detect bugs, code smells, and security vulnerabilities.

**21. What is OWASP ZAP?**
OWASP ZAP (Zed Attack Proxy) is an open-source DAST tool used to find security vulnerabilities in running web applications.

**22. What is Trivy?**
Trivy is a comprehensive vulnerability scanner for container images, file systems, and Git repositories.

**23. What is OWASP Top 10?**
The OWASP Top 10 is a standard awareness document that lists the ten most critical security risks to web applications (like Injection, Broken Access Control).

**24. What is GDPR?**
GDPR (General Data Protection Regulation) is a European regulation on data protection and privacy, emphasizing principles like data minimization, consent, and the right to be forgotten.

**25. What is DVC?**
DVC (Data Version Control) is a version control system for machine learning projects, used to track changes in large datasets and models, similar to how Git tracks code.

**26. What is MLflow?**
MLflow is an open-source platform to manage the machine learning lifecycle, including tracking experiments, packaging code, and sharing models.

**27. What is MLOps?**
MLOps (Machine Learning Operations) is a set of practices that aims to reliably and efficiently deploy and maintain machine learning models in production.

**28. What is model bias?**
Model bias occurs when an ML model produces systematically prejudiced results, often because the training data was unrepresentative or contained historical human biases.

## CO4 - Cloud MLOps and Cloud Deployment

**29. What is cloud MLOps?**
Cloud MLOps applies MLOps practices using cloud provider services (like AWS, GCP) to handle data storage, scalable training, and robust model deployment.

**30. What is AWS SageMaker?**
AWS SageMaker is a fully managed cloud service that provides developers and data scientists the ability to build, train, and deploy machine learning models quickly.

**31. What is S3?**
Amazon S3 (Simple Storage Service) is a highly scalable object storage service used to store and retrieve large amounts of data, such as datasets or trained ML models.

**32. How can ML models be deployed in the cloud?**
ML models can be deployed by wrapping them in an API (like Flask or FastAPI) and hosting them on cloud servers (like EC2), container services (like ECS), or serverless functions (like AWS Lambda). They can also be deployed using managed endpoints like SageMaker Endpoints.

**33. What is an ML CI/CD pipeline?**
An ML CI/CD pipeline automates the process of testing code changes, triggering model retraining if data changes, validating the new model, and deploying it to production.

## GradeMind Project Specifics

**34. Why Random Forest?**
Random Forest was chosen because it is an ensemble learning method that handles non-linear relationships well, is less prone to overfitting than a single decision tree, and is easy to interpret using feature importance.

**35. What is the target variable?**
The target variable is `final_grade_category`, which can be one of three values: Pass, Merit, or Distinction.

**36. What are the input features?**
The input features are: Attendance Percentage, Internal Marks, Assignment Score, Study Hours Per Week, and Previous GPA.

**37. How is the dataset generated?**
The dataset is synthetic, generated using a Python script (`generate_dataset.py`). It uses normal distributions and a hidden "talent" factor to create logically correlated features (e.g., higher attendance correlates with higher marks).

**38. How is the model evaluated?**
The model is evaluated using standard classification metrics: Accuracy, Precision, Recall, and F1-score, which are calculated on a testing split (20%) of the dataset.

**39. How does Flask communicate with the ML model?**
The Flask application loads the trained model from a `.joblib` file using the `joblib` library. When a user submits the form, Flask passes the input data to the model's `predict()` function and returns the result.

**40. How does Docker help GradeMind?**
Docker packages the GradeMind application (Flask app, ML model, dependencies) into a single container image. This ensures that the application runs exactly the same way on any machine, eliminating "it works on my machine" problems.

**41. How does Kubernetes help GradeMind?**
Kubernetes allows us to run multiple copies (replicas) of the GradeMind Docker container. It automatically restarts containers if they fail, balances traffic between them, and makes scaling the application easier.

**42. How can the application be monitored?**
The Flask application is instrumented to expose metrics at a `/metrics` endpoint. Prometheus scrapes this endpoint to track data like the number of predictions made and the time taken for each prediction.

**43. How can the model be improved?**
The model could be improved by using real student data instead of synthetic data, tuning hyperparameters (like tree depth), or testing other algorithms (like Gradient Boosting or Neural Networks).
