### Hexlet tests and linter status:
[![Actions Status](https://github.com/Denwien/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Denwien/python-project-52/actions)

### SonarCloud Quality Gate:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-52)

### Code Coverage:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-52)

# Task Manager

Task Manager is a web application built with Django.
It allows users to create tasks, assign statuses, labels, and executors, as well as filter tasks by different criteria.

The project includes:

* user authentication
* task management (CRUD)
* task filtering
* automated tests
* static code analysis with SonarCloud

## Requirements

* Python >= 3.12
* [uv](https://docs.astral.sh/uv/)
* PostgreSQL (production) / SQLite (development)

## Installation
```bash
git clone https://github.com/Denwien/python-project-52.git
cd python-project-52
uv sync
```

## Usage
```bash
make migrate       # apply database migrations
make build         # collectstatic + migrate
make test          # run tests
make test-coverage # run tests with coverage report
```
