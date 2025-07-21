---
name: Docker Optimization and Workflow Improvement
about: This issue tracks the optimization of our Docker setup and the simplification of the build/push workflow.
title: 'feat: Optimize Docker Images and Add Makefile'
labels: enhancement, performance
assignees: ''

---

### Description

This PR addresses the need to optimize our Docker images to reduce their size and improve the developer workflow for building and pushing images to ECR.

The initial image size for the Django application was over 600MB, which is unnecessarily large for a production environment. Additionally, the manual `docker build` and `docker push` commands were long and cumbersome.

### Changes Made

1.  **Optimized Django `Dockerfile`**:
    *   Implemented a multi-stage build to separate the build environment from the final runtime environment. This prevents build-time dependencies (like `gcc`) from being included in the final image.
    *   Added a step to clean up the `apt` cache within the builder stage to keep layers lean.

2.  **Reduced Image Size by Removing Unused Dependencies**:
    *   Investigated the `requirements.txt` file and identified that `pandas` and `openpyxl` were major contributors to the image size.
    *   Confirmed that these libraries are not used by the application at runtime and removed them. This is the most significant change for reducing the image size.

3.  **Added a `Makefile` for Simplified Workflow**:
    *   Created a `Makefile` in the root directory to provide simple commands for building and pushing Docker images.
    *   Developers can now use `make build-django`, `make push-django`, `make build-nginx`, and `make push-nginx`.

### Benefits

*   **Reduced Docker Image Size**: The final Django image size is significantly smaller, leading to faster deployments, lower storage costs, and a reduced attack surface.
*   **Improved Developer Workflow**: The `Makefile` simplifies the process of building and pushing images, reducing the chance of errors and saving time.
*   **Enhanced Security**: Smaller images with fewer packages have a smaller attack surface.
*   **Best Practices**: The new `Dockerfile` setup follows best practices for building production-ready Docker images.