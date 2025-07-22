# Makefile for Docker image build and push

# Variables
ECR_REGISTRY := 626690050115.dkr.ecr.us-east-1.amazonaws.com
DJANGO_APP_NAME := django-app
NGINX_APP_NAME := nginx
TAG := latest

# Targets
.PHONY: all build-django push-django build-nginx push-nginx

all: build-django push-django build-nginx push-nginx

# Django App
build-django:
	docker build -t $(ECR_REGISTRY)/$(DJANGO_APP_NAME):$(TAG) .

push-django:
	docker push $(ECR_REGISTRY)/$(DJANGO_APP_NAME):$(TAG)

# Nginx
build-nginx:
	docker build -f nginx/Dockerfile -t $(ECR_REGISTRY)/$(NGINX_APP_NAME):$(TAG) nginx

push-nginx:
	docker push $(ECR_REGISTRY)/$(NGINX_APP_NAME):$(TAG)