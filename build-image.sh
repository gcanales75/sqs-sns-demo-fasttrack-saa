#!/bin/bash
# Variables
export repo=demosqs
# Build docker image
cd website/
docker build -t aws/demosqs .
# Create ECR repo
#aws ecr create-repository --repository-name $repo --region us-east-1
# Environment variables
export AWS_DEFAULT_REGION=us-east-1
export ACCOUNT_NUMBER=`aws sts get-caller-identity --query 'Account' --output text`
export ECR_REPO_URI=`aws ecr describe-repositories --repository-names $repo --query 'repositories[*].repositoryUri' --output text`
# Authenticate to ECR repo
$(aws ecr get-login --registry-ids $ACCOUNT_NUMBER --no-include-email --region us-east-1)
# Tag docker image
docker tag aws/demosqs:latest $ECR_REPO_URI:latest
# Push docker image to repo
docker push $ECR_REPO_URI:latest