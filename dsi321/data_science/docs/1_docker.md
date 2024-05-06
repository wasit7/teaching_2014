### Chapter 1: Docker and Docker-Compose Setup

#### Overview
This chapter introduces Docker and Docker Compose, essential tools for developing, shipping, and running applications. By using Docker, developers can simplify the setup process and ensure consistency across multiple development and production environments. We will guide you through the installation of Docker and Docker Compose, setting up a basic container, and running multi-container applications using `docker-compose`.

#### 1. Introduction to Docker
Docker is a platform for developing, shipping, and running applications inside containers. Containers allow a developer to package up an application with all the parts it needs, such as libraries and dependencies, and ship it all out as one package.

#### 2. Installing Docker
To install Docker on your local machine or a virtual machine (VM), follow these steps:

- **On a Local Machine:**
  ```bash
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo groupadd docker
  sudo usermod -aG docker $USER
  newgrp docker
  docker run hello-world  # Test installation
  docker --version  # Check Docker version
  ```

- **On a Virtual Machine (VM):**
  - **Create a VM on Google Cloud Platform (GCP):**
    - Go to the GCP Console.
    - Create a new instance with Ubuntu 22.04 LTS as the operating system.
    - Under "Security," add manually generated SSH keys (refer to external guides like YouTube tutorials for SSH setup).

  - **Set up Firewall Rules:**
    - Navigate to the Compute Engine, select your VM instance.
    - Under networking details, access the firewall settings and create a new rule allowing all incoming traffic on desired ports for your applications.

#### 3. Installing Docker Compose
Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services, networks, and volumes:

  ```bash
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  docker-compose --version  # Verify installation
  ```

#### 4. Creating Your First Docker Container
After installing Docker, test your setup by running a simple container:

  ```bash
  docker run hello-world
  ```

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

#### 5. Setting Up Your First Docker Compose Project
To demonstrate a basic Docker Compose setup, we'll create a simple configuration for running a Jupyter Notebook server:

- **Create and Configure `docker-compose.yml`:**
  - Navigate to your project directory (create one if it doesn't exist):
    ```bash
    mkdir data_science && cd data_science
    nano docker-compose.yml
    ```
  - Enter the following configuration:
    ```yaml
    version: '3.8'
    services:
      jupyter:
        image: jupyter/scipy-notebook:latest
        ports:
          - "8888:8888"
        volumes:
          - ./notebooks:/home/jovyan/work
    ```

- **Start the Jupyter Notebook Service:**
  ```bash
  docker-compose up -d
  docker-compose ps  # Check the status of the service
  docker-compose logs jupyter  # View logs to get the Jupyter token
  ```

- **Adjust Permissions for Notebooks Directory (if necessary):**
  ```bash
  sudo chmod ugo+rwx notebooks/
  ```

#### 6. Accessing the Jupyter Notebook
Once the Jupyter Notebook server is up, you can access it through your browser by navigating to `http://localhost:8888` and entering the token provided in the logs.

#### Conclusion
This chapter covered the fundamentals of setting up Docker and Docker Compose on your local machine or a VM, with a practical example of deploying a Jupyter Notebook server. These tools not only facilitate seamless development environments but also ensure that applications run consistently across different systems.