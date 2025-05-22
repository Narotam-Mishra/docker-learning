
### Docker Learning

## Docker Learning material - https://drive.google.com/drive/folders/1deQSD0iRrIiaotN-FI5jvruJtj31aNa-

## What is a Docker? (01:38)

# Docker is a containerization platform for developing, packaging, shipping and running applications. It provides the ability to run an application in an isolated environment called a container. It makes deployment and development very efficient.

## Why we need Docker? (02:32)

- Consistency Across Environments :- Docker packages our application with all its dependencies into a container, ensuring it behaves the same in development, testing, and production.

- Isolation :- Each container runs in its own environment, isolated from others.

- Portability :- Containers can run anywhere: on your laptop, a server, cloud provider (like AWS, GCP, Azure), or even on CI/CD pipelines.

- Simplified Configuration :- Docker uses a Dockerfile to define how an app should be built and run. This makes setup repeatable and automated.

- Microservices Ready :- Makes it easy to break your application into smaller, manageable services (microservices), each running in its own container.

## What is Container (05:40)

# A way to package an application with all the necessary dependencies and configuration that can be easily shared. It makes the deployment and development efficient.

## Architecture of Docker (7:39)

# Key components of Docker :-

1). Docker Client :- The Docker Client is the primary way users interact with Docker. We use the Docker CLI (Command Line Interface) to run commands like `docker build`, `docker pull`, `docker run`, etc. These commands are sent to the Docker Daemon (Server). Main features of Docker Client :-
- acts as the user interface.
- communicates with the Docker Daemon using REST APIs over UNIX sockets or network interfaces.

2). Docker Daemon (dockerd) :- It listens to Docker API requests from the client and performs requested tasks. The Docker Daemon runs in the background and is responsible for managing :-
- Docker images
- Containers
- Networks
- Volumes

# Main features of Docker Daemon :-
- core component that manages all container-related activities.
- can communicate with other Docker daemons to manage services in a Docker Swarm.

3). Docker Registries :- A registry stores Docker images. `Docker Hub` is the default public registry. We can also set up private registries for secure image storage.

# Key commands :-
- docker push – uploads image to registry.
- docker pull – downloads image from registry.

4). Dockerfile :- A script of instructions to build a Docker image. Each command creates a layer in the final image, making it efficient and cacheable.

# Running multiple version of same Application in Docker :- By using Docker's container for each version we can do this

# Other way to run multiple version of same Application is using Virtual Machines.

## Docker Vs VM (11:31)

# Docker - It has low impact on OS, very fast, low disk space usage. Sharing, re-building and distribution is easy. It encapsulate apps instead of whole machine.

# VM - It has high impact on OS, slower, high disk space storage usage. Sharing, re-building and distribution is challenging. It encapsulate whole machine.

# Main Components of Docker :- 
- DockerFile,
- Docker Image,
- Docker Container,
- Docker Registry

## Flow of Docker (13:13)

# DockerFile -----> Docker Image -----> Docker Container
#         |               |                    |
#   (Instructions)   (Template)         (Running Instance)
#
# Flow Diagram:
#
#   +------------+      docker build      +-------------+      docker run      +-----------------+
#   | Dockerfile |  ------------------>  | Docker Image |  -----------------> | Docker Container |
#   +------------+                       +-------------+                      +-----------------+
#
#   (Set of steps)                        (Snapshot)                          (Live app) 


# DockerFile :- It is simple text file with instructions to build an image.

# Docker Image :- It is a single file with all the dep and lib to run the program.

# Docker Container :- Instance of a Docker Image.

## What is Dockerfile (14:17)

## What is Docker Registry (14:57)

# A Docker registry is a central repository for storing and distributing Docker images.

# What is Docker Hub?
# Docker Hub is a cloud-based registry service where we can store, share, and manage Docker images. It allows users to find and download public images or upload their own for collaboration and deployment.

# Difference between Registry vs Repository :- 
- Docker Registry: A Docker Registry is a storage and distribution system for Docker images. It is the server or service (like Docker Hub, AWS ECR, or a private registry) that stores multiple repositories.

- Docker Repository: A Docker Repository is a collection of related Docker images (usually for a specific application or service) with different tags (versions). A repository exists within a registry.

# In short:
- Registry = the server/service that stores images.
- Repository = a set of images (with tags) for a specific project within a registry.
