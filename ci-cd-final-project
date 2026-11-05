# Accounts Service — CI/CD Project

**Project name:** Accounts Service

## Description
Accounts Service is an educational Python microservice used to demonstrate continuous integration, unit testing, container image creation, and an OpenShift/Tekton deployment workflow.

## Project objectives
- Validate source code automatically with GitHub Actions.
- Run flake8 lint checks and nose unit tests.
- Package the sample API in a container image.
- Define Tekton pipeline tasks for cleanup, git clone, linting, testing, image building, and deployment.
- Define persistent storage using an OpenShift PersistentVolumeClaim.

## Technologies
Python, Flask, GitHub Actions, flake8, nose, Docker, Buildah, Kubernetes, Red Hat OpenShift, and Tekton Pipelines.

## GitHub Actions workflow
The `.github/workflows/workflow.yml` file defines checkout, Node.js and Python setup, dependency installation, flake8 lint checks, and nose unit tests. Verify the actual run on the repository's **Actions** tab.

## OpenShift pipeline tasks
The OpenShift Tekton configuration defines these six tasks in sequence:

1. `cleanup`
2. `git-clone`
3. `flake8-lint`
4. `nose-test`
5. `buildah-build`
6. `openshift-deploy`

The `oc-pipelines-pvc.yaml` manifest requests `1Gi` of storage using storage class `skills-network-learner`. This configuration alone does **not** prove that the PVC was provisioned or the pipeline succeeded.

## Application
Run locally with `python app.py` and check `http://localhost:8000/health`. Run tests with `nosetests -v`.

## Required submission evidence
Use real GitHub Actions output and actual OpenShift Console screenshots showing PVC details, the pipeline graph, and a successful PipelineRun. Reference diagrams or example logs do not establish execution success.

## Repository
https://github.com/AveryJan/accounts-service
