# Data Science Environment Setup

This project sets up a complete data science environment using Docker. It integrates Jupyter, PostgreSQL, Streamlit, and MLflow, providing a robust setup for data analysis, machine learning, and data visualization.

## Project Components

- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Jupyter Notebook**: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- **Streamlit**: An open-source app framework for Machine Learning and Data Science teams.
- **MLflow**: An open-source platform for managing the end-to-end machine learning lifecycle.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Docker
- Docker Compose

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wasit7/teaching_2024.git
   cd dsi321/data_science
   ```

2. **Build and run the containers**
   ```bash
   docker-compose up --build
   ```

This command builds the Docker images if they don't exist and starts the containers.

### Usage

- **Accessing Jupyter Notebook**: Navigate to `http://localhost:8888`. Use the token provided in the terminal logs to log in.
- **Accessing Streamlit**: Open `http://localhost:8501` to view the Streamlit application.
- **Accessing MLflow**: Visit `http://localhost:5000` to track and manage your ML experiments.
- **Connecting to PostgreSQL**: Use any database client with the following credentials:
  - **Host**: localhost
  - **Port**: 5432
  - **User**: user
  - **Password**: password
  - **Database**: datascience

## Project Structure

```plaintext
/data-science-environment
|-- docker-compose.yml
|-- /postgres
|   |-- Dockerfile
|-- /jupyter
|   |-- Dockerfile
|-- /streamlit
|   |-- Dockerfile
|   |-- app.py
|-- /mlflow
|   |-- Dockerfile
|-- README.md
```

### Customizing the Environment

You can customize each service by modifying its corresponding Dockerfile or the docker-compose.yml file to include additional dependencies, change versions, or expose new ports.

## Testing

Describe how to run the automated tests for this system. Include details about what kinds of tests are available and what they verify.

```bash
docker-compose exec <service_name> pytest
```

## Troubleshooting Common Issues

- **Issue 1**: Jupyter Notebook is inaccessible.
  - **Solution**: Check the Docker logs for any error messages or incorrect port mappings.
- **Issue 2**: Streamlit does not update changes.
  - **Solution**: Ensure volumes are properly mounted and Streamlit is set to watch for changes.

## Authors

- **Wasit Plimrasert** - *Initial work* - [wasit7](https://github.com/Yourwasit7Username)
