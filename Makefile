# Helper tasks for development and CI/CD

.PHONY: test_backend test_frontend build_backend build_frontend push_backend push_frontend all_tests

# Run backend unit and integration tests
test_backend:
	cd backend && python manage.py test

# Run frontend tests
test_frontend:
	cd frontend && npm test -- --watchAll=false

# Run both backend and frontend tests
all_tests: test_backend test_frontend

# Build Docker images for backend and frontend
build_backend:
	docker build -t $(DOCKER_USERNAME)/backend:latest ./backend

build_frontend:
	docker build -t $(DOCKER_USERNAME)/frontend:latest ./frontend

# Push Docker images to Docker Hub
push_backend:
	docker push $(DOCKER_USERNAME)/backend:latest
push_frontend:
	docker push $(DOCKER_USERNAME)/frontend:latest
