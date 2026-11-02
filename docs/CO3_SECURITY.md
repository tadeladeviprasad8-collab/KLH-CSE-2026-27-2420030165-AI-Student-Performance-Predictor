# CO3 – Security Operations and DevSecOps

This document explains the DevSecOps principles and security tools integrated into the GradeMind project.

## DevSecOps Philosophy
DevSecOps integrates security practices within the DevOps process. Security is no longer treated as a final step before release; instead, it is integrated throughout the development lifecycle (Shift-Left Security).

The lifecycle:
Plan → Code → Build → Test → **Security** → Deploy → Monitor

## Security Tools Used in GradeMind

### 1. Bandit (SAST - Static Application Security Testing)
Bandit is a tool designed to find common security issues in Python code. It analyzes the source code (Static Analysis) without running it.
- **Purpose**: Identify hardcoded passwords, unsafe function calls, or injection vulnerabilities in `app.py` and the `src/` directory.
- **Usage**: `bandit -r src app.py`

### 2. pip-audit (Dependency Scanning)
Modern applications rely heavily on third-party libraries. `pip-audit` scans the Python environment or `requirements.txt` for packages with known security vulnerabilities (CVEs).
- **Purpose**: Ensure `scikit-learn`, `Flask`, etc., do not have known exploits.
- **Usage**: `pip-audit`

### 3. SonarQube (Code Quality and Security)
SonarQube is a platform for continuous inspection of code quality.
- **Purpose**: Identifies Bugs, Code Smells (maintainability issues), and Security Vulnerabilities.
- **Integration**: The project structure is ready for SonarQube analysis, which can be run locally via a Docker container to analyze the Python code.

### 4. OWASP ZAP (DAST - Dynamic Application Security Testing)
ZAP (Zed Attack Proxy) is an open-source tool for finding vulnerabilities in web applications while they are running (Dynamic Analysis).
- **Purpose**: Scans the running Flask application (e.g., `http://localhost:5000`) for issues like cross-site scripting (XSS), security misconfigurations, and missing headers.
- **Action**: Developers run ZAP against the local dev server and fix findings before deployment.

### 5. Trivy (Container Scanning)
Trivy is a comprehensive security scanner for container images.
- **Purpose**: Scans the built `grademind:latest` Docker image for vulnerabilities in the base OS (Debian/Ubuntu in the python slim image) and installed libraries.
- **Usage**: `trivy image grademind:latest`

## Secure Coding Practices Implemented
- **Input Validation**: The `src/predict.py` module strictly validates all form inputs (e.g., ensuring percentages are between 0-100) before passing them to the ML model, preventing unexpected errors or injection attacks.
- **No Hard-coded Secrets**: The Flask secret key is loaded from environment variables (`.env`). The repository only contains a `.env.example` template.
- **Proper Error Handling**: The Flask application catches exceptions and displays generic, user-friendly error messages, ensuring stack traces (which can reveal system details) are never exposed to the end-user.
