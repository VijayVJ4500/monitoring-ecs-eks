# Project A - Scalable Microservice on AWS (ECS + EKS + Monitoring)

This project demonstrates a production-ready DevOps pipeline with:
- Flask microservice containerized with Docker
- Deployment on AWS ECS Fargate and EKS (Kubernetes)
- Infrastructure-as-Code with Terraform
- CI/CD pipeline with GitHub Actions
- Monitoring with Prometheus & Grafana

## Setup Instructions

1. Clone repo & install dependencies
   ```bash
   git clone <your-repo>
   cd <your-repo>
   ```

2. Add GitHub Secrets:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION
   - AWS_ACCOUNT_ID
   - TF_VAR_DB_PASSWORD

3. Push code to `main` branch → CI/CD will build & deploy.

4. Access application:
   ```
   http://<ALB_DNS>/
   http://<ALB_DNS>/metrics
   ```

5. Access Grafana (via port-forward or LoadBalancer from EKS).

---

## Resume Bullets
- Built and deployed a scalable Flask microservice on AWS ECS Fargate and EKS using Terraform and GitHub Actions.
- Automated CI/CD pipelines with Docker image builds, ECR integration, and Terraform-managed infrastructure deployments.
- Implemented monitoring with Prometheus and Grafana for observability of microservices.
