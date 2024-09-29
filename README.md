<h1><center>Blog</center></h1>

---

# Setting Up GitHub Actions for a Python Project

This guide explains how to use GitHub Actions to **automate tasks** such as **testing, linting, formatting**, and **building a Docker container** for your Python project. The example workflow uses a `Makefile` to **streamline** commands.

## Overview of the Workflow
**What?**  
The workflow **automates tasks** triggered by Git events (**push** or **pull request**). It sets up the environment, installs dependencies, performs code quality checks, runs tests, and builds a Docker container.

**Why?**  
- **Continuous Integration (CI)**: Automates the process of testing and building your code to catch issues early.
- **Code Quality Assurance**: Ensures code is linted, formatted, and tested consistently before merging or deploying.
- **Efficient Builds**: Streamlines development by using Docker to create consistent application environments.

**How?**  
The workflow is defined in a YAML file (typically `.github/workflows/ci.yml`).

## GitHub Actions Triggers
**What?**  
The **`on`** section **specifies when the workflow should be triggered**.

**Why?**  
- **Push and Pull Request Events**: The workflow runs when code is pushed to the repository or when a pull request is opened.
- **Path Filtering**: The `paths-ignore` key prevents the workflow from running when only certain files (like lock files, `toml` files, and `README.md`) are changed.

**How?**
```yaml
name: Blog
on:
  push:
    paths-ignore:
      - "**/*.lock"
      - "**/*.toml"
      - "**/README.md"

  pull_request:
    paths-ignore:
      - "**/*.lock"
      - "**/*.toml"
      - "**/README.md"
```

## Workflow Jobs and Steps
### Step 1: Defining the Build Job
**What?**  
The **`jobs`** section defines the **individual steps that will be executed in the workflow**.

**Why?**  
- The **`build`** job **sets up the necessary environment** and sequentially runs each action required for the CI process.

**How?**
```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # Specifies the OS environment for the workflow
```

### Step 2: Checking Out the Repository
**What?**  
Checks out the code from the repository to make it available for the subsequent steps.

**How?**
```yaml
    steps:
      - uses: actions/checkout@v4  # Uses the GitHub Action to clone the repository
```

### Step 3: Setting Up Python Environment
**What?**  
The workflow sets up Python version `3.12` using `actions/setup-python`.

**Why?**  
- To ensure the correct Python version is used for running tests and managing dependencies.
- Caches **`pip`** packages **to improve workflow speed**.

**How?**
```yaml
      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: 3.12
          cache: 'pip'
```

### Step 4: Installing Dependencies
**What?**  
Installs the project dependencies using `make install`. This typically refers to a command in the `Makefile` that runs `pip install`.

**Why?**  
- Ensures all necessary packages are available before running tests, linters, and build steps.

**How?**
```yaml
      - name: Install dependencies
        run: make install
```

### Step 5: Linting and Formatting Code
**What?**  
- **Linting**: Uses `ruff`, a linter for Python code, to identify and enforce code style issues.
- **Formatting**: Uses `ruff` to format the code according to the style guide.

**Why?**  
- To maintain code consistency and adhere to style guidelines.

**How?**
```yaml
      - name: Lint code with ruff
        run: make lint

      - name: Format code with ruff
        run: make format
```

### Step 6: Running Tests
**What?**  
Runs tests using `pytest` to ensure code functionality.

**Why?**  
- To verify that code changes do not break existing features.

**How?**
```yaml
      - name: Test with pytest
        run: make test
```

### Step 7: Building a Docker Container
**What?**  
Builds a Docker container for the application.

**Why?**  
- Docker containers package the application and its dependencies into a standardized unit, ensuring consistency across environments.

**How?**
```yaml
      - name: Build Docker Container
        run: make build
```

---


# Makefile for Managing a Python Project

This guide breaks down how to use a `Makefile` to streamline common development tasks such as installing dependencies, linting code, formatting code, running tests, building Docker images, running containers, and deploying applications to Azure.


## What is a `Makefile`?
**What?**  
A `Makefile` is a file containing a set of directives to automate tasks commonly executed during the development lifecycle.

**Why?**  
- **Automation**: Reduces manual effort by bundling commands for setup, linting, testing, and deploying.
- **Consistency**: Ensures that all developers run the same set of commands in the same way.
- **Simplicity**: Allows running complex command sequences with a simple `make <command>`.


## Makefile Targets Explained

### Step 1: Installing Dependencies
**What?**  
The `install` target updates `pip` and installs project dependencies listed in `requirements.txt`.

**Why?**  
- Ensures all necessary packages are installed to run the project.
- Keeps `pip` up-to-date for improved security and features.

**How?**
```bash
install:
	# Install Package Installer for Python
	pip install --upgrade pip && pip install -r requirements.txt
```
- `pip install --upgrade pip`: Upgrades `pip` to the latest version.
- `pip install -r requirements.txt`: Installs packages specified in `requirements.txt`.

Usage:
```bash
make install
```


### Step 2: Linting Code
**What?**  
The `lint` target uses `ruff`, a Python linter, to check for style issues and apply fixes as per the `pyproject.toml` configuration.

**Why?**  
- Ensures code follows a consistent style guide.
- Automatically fixes lint errors to adhere to project standards.

**How?**
```bash
lint:
	# Lint Code with Ruff using pyproject.toml
	ruff check . --fix --config pyproject.toml
```
- `ruff check .`: Runs the linter on the current directory.
- `--fix`: Automatically applies fixes to code style issues.
- `--config pyproject.toml`: Uses `pyproject.toml` for configuration settings.

Usage:
```bash
make lint
```


### Step 3: Formatting Code
**What?**  
The `format` target uses `ruff` to format code based on the style rules in `pyproject.toml`.

**Why?**  
- Improves code readability by applying consistent formatting rules.

**How?**
```bash
format:
	# Format Code with Ruff Formatter using pyproject.toml
	ruff format . --config pyproject.toml
```
- `ruff format .`: Formats code in the current directory.
- `--config pyproject.toml`: Uses the settings from `pyproject.toml`.

Usage:
```bash
make format
```


### Step 4: Running Tests
**What?**  
The `test` target is reserved for running the project's test suite. The actual command for running the tests should be added based on the testing framework in use (e.g., `pytest`).

**Why?**  
- Ensures that all features work as expected and that no regressions are introduced.

**How?**
```bash
test:
	# Test Code
```
You may replace `# Test Code` with an appropriate testing command:
```bash
pytest tests/
```

Usage:
```bash
make test
```


### Step 5: Building a Docker Image
**What?**  
The `build` target creates a Docker image for the application.

**Why?**  
- Packaging the application and its environment into a Docker image allows for easy and consistent deployment across different environments.

**How?**
```bash
build:
	# Build Docker Image
```
Replace `# Build Docker Image` with the Docker build command:
```bash
docker build -t my-image:latest .
```

Usage:
```bash
make build
```


### Step 6: Running a Docker Container
**What?**  
The `run` target starts a Docker container based on the built image.

**Why?**  
- Running the containerized application allows for testing the build in a controlled environment.

**How?**
```bash
run:
	# Run Docker Container
```
Replace `# Run Docker Container` with the Docker run command:
```bash
docker run -p 8000:8000 my-image:latest
```

Usage:
```bash
make run
```


### Step 7: Deploying to Azure
**What?**  
The `deploy` target manages the deployment of the Docker container to Azure.

**Why?**  
- Automates the process of deploying the container to an Azure service for production use.

**How?**
```bash
deploy:
	# Azure Deployment Setup with Docker
```
You may replace `# Azure Deployment Setup with Docker` with your deployment command to Azure:
```bash
az webapp up --name my-app --docker-image my-image:latest
```

Usage:
```bash
make deploy
```

---