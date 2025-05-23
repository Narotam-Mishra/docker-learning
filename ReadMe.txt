
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

## Creating Demo Project - React Webpp (30:44)

## How to create DockerFile? (38:11)

# Useful commands

# `docker build .` - this command is used to build docker image in root directory 

# `docker image ls` - this command is used to list docker image 

## Manage and Running Containers (49:24)

# `docker stop determined_lichterman` - this command gracefully stops a running container. `determined_lichterman` is docker container name

# `docker ps` - this command lists all currently running containers in docker.

# Command to run docker image (in attach mode) :- `docker run -p 5173:5173 f5d351fba0fc`

# Command Breakdown

==> `docker run`

# Purpose:- Creates and starts a new container from a Docker image

# Action: This is the main command to execute a Docker container

===> `-p 5173:5173`

# Flag: -p (or --publish) is used for port mapping/forwarding

# Format: -p HOST_PORT:CONTAINER_PORT
Breakdown:

# First 5173: Port on your host machine (your computer)

#Second 5173: Port inside the Docker container

# Function: Maps port 5173 on your local machine to port 5173 inside the container

# Result: When you access localhost:5173 in your browser, traffic gets forwarded to port 5173 inside the container

==> `f5d351fba0fc`

# Type: Docker image ID (shortened form)

# Full form: This is likely a truncated version of a longer hash like f5d351fba0fc1a2b3c4d5e6f7a8b9c0d1e2f3a4b

# Purpose: Identifies which Docker image to use for creating the container

# What happens when you run this command :- `docker run -p 5173:5173 f5d351fba0fc`

1). Container Creation:- Docker creates a new container from image `f5d351fba0fc`

2). Port Binding:- Sets up port forwarding from your machine's port 5173 to the container's port 5173

3). Container Start:- Starts the container and runs the default command (in your case, npm run dev)

4). Network Access:- Oour react application becomes accessible at http://localhost:5173

# Running Container In Detached Mode :- Suppose we want to run our docker container in background and terminal shouldn't be block due to this then we should prefer running container in detached mode.

# Benefits of running container in detached mode :-
1). Terminal Freedom :- Our terminal remains free to run other commands immediately.

2). Background Services :- Perfect for running services that should continue running in the background.

3). Session Independence :- It prevents accidental container shutdown when terminal disconnects.

4). Production Deployments :- It allows automation scripts to start containers without hanging

## When to Use Each Mode ?

# Use Attached Mode when:
- Debugging: You need to see real-time logs
- Development: Interactive debugging sessions
- One-time tasks: Scripts or commands that run once and exit
- Learning: Understanding what the application is doing.

# Use Detached Mode when:
- Production services: Web servers, APIs, databases
- Long-running processes: Background workers, schedulers
- Multiple containers: Running several containers simultaneously
- CI/CD pipelines: Automated deployments

# Command to run docker image (in detached mode) :- `docker run -d -p 5173:5173 f5d351fba0fc`

# Identifies flags: -d (detached) and -p 5173:5173 (port mapping)

# When we run docker container in detached mode (using above command) :-
- Container ID returned immediately
- Container runs in background
- Application accessible at http://localhost:5173
- Terminal remains free for other commands

# Running Multiple Containers - we run multiple container from same docker image by just changing the port number. For example - 1). `docker run -d -p 5173:5173 f5d351fba0fc` will run the docker container on port 5173,
2). `docker run -d -p 5175:5173 f5d351fba0fc` will run the docker container on port 5175,
3). `docker run -d -p 5177:5173 f5d351fba0fc` will run the docker container on port 5177,

## Useful Info for Containers (01:02:25)

# `docker ps -a` - this command used to show list of all available container whereas `docker ps` command used to show only running container.

# Command to run docker image (in detached mode and will be removed once we stop) :- `docker run -d --rm -p 5173:5173 f5d351fba0fc`

# --rm flag will automatically deletes the container when it stops running. It prevents accumulation of stopped containers and keeps your system clean

# Above command breakdown :-
==> -d: Detached mode (runs in background)
==> --rm: Auto-remove container when it stops
==> -p 5173:5173: Port mapping
==> f5d351fba0fc: Image ID

Q. How to give custom name to docker container? 
# Using this command `docker run -d --rm --name "reactwebapp" -p 5173:5173 f5d351fba0fc`

# Above command runs a Docker container with the following configuration :-

-d: Runs in background (detached mode)
--rm: Automatically deletes the container when it stops
--name "reactwebapp": Names the container "reactwebapp" for easy reference
-p 5173:5173: Maps port 5173 from your computer to port 5173 inside the container
f5d351fba0fc: Uses the Docker image with this ID

Result: Creates a background container named "reactwebapp" that's accessible at localhost:5173 and will automatically clean itself up when stopped.

## Managing Docker Images (1:06:36)

Q. How to give custom name to docker image?
# using this command - `docker build -t myreactapp:01 .`

# Above command builds a Docker image with the following configuration :-

# `docker build`:- Creates a Docker image from a Dockerfile
# `-t myreactapp:01`:- Tags the image with name "myreactapp" and version "01"
# `.` :- Uses the current directory as the build context (where Dockerfile is located)

# Result: Creates a Docker image named "myreactapp:01" from the Dockerfile in the current directory, which can then be used to run containers.

# Comamnd  - `docker build -t myreactapp:02 .`

# Above command builds a Docker image with the following configuration :-

# `docker build` :- Creates a Docker image from a Dockerfile
# `-t myreactapp:02` :- Tags the image with name "myreactapp" and version "02"
# `.` :- Uses the current directory as the build context

# Key Difference :-
- myreactapp:01 creates version "01" of the image
- myreactapp:02 creates version "02" of the same image

Q. How to delete docker image?
# using command - `docker rmi myreactapp:02`

# Above command removes a Docker image:

# `docker rmi` :- Removes (deletes) a Docker image
# `myreactapp:02` :- Specifies the image name and tag to delete

# Result: Permanently deletes the "myreactapp:02" image from your local Docker storage, freeing up disk space. The image will no longer appear in docker images list.
Note: You cannot remove an image if containers are currently using it - you must stop and remove those containers first.

# What If We update Project ?
