
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

Q. What If We update Project ?
# If there is any update in the app then we can re-build the docker image and run the container.

# Pre-defined Docker Images :- We can check predefined docker images on Docker Hub (https://hub.docker.com/)

# pull python image - `docker pull python`

# pull nginx image - `docker pull nginx`

## Running Docker Container With Interactive mode (1:21:20)

# `docker run -it e7b63396cd33`

# Above command runs a Docker container interactively:

# `docker run` - starts a new container from an image
# `-it` - combines two flags:

# `-i` keeps STDIN open for interaction
# `-t` allocates a pseudo-TTY terminal


# `e7b63396cd33` - the image ID or tag to run

# The result is an interactive terminal session inside the container, allowing you to execute commands directly within it.

# Sharing Docker Images to Docker Hub 
1). Create a Docker Hub Account
2). Log in to Docker Hub from Terminal :- using command `docker login`
3). Tag Your Image :- Your image needs to follow Docker Hub's naming convention using command `docker tag dockernaru99/basic-react-webapp:01`
4). Push the Image using command `docker push dockernaru99/basic-react-webapp:01`
5). Verify the Upload :- Go to hub.docker.com and log into your account and check that your repository appears in your repositories list

## How to Pull Images remotely (01:35:43)

# We can docker image using command - `docker pull dockernaru99/basic-react-webapp:01`

## Docke Volume (1:38:21)

# A Docker volume is a persistent storage mechanism that exists outside of container lifecycles. Unlike container filesystems that disappear when containers are removed, volumes persist data independently.

# Key characteristics :-
- Stored in Docker-managed locations on the host
- Shared between containers
- Persist even after containers are deleted
- Managed by Docker (not directly accessible via host filesystem paths)

# Common use cases:
1). Database storage - Keep database files persistent across container restarts and updates. Without volumes, all database data would be lost when the container stops.
2). Configuration sharing - Share config files between multiple containers or between host and containers.
3). Development workflows - Mount source code directories so changes are immediately reflected without rebuilding containers.
4). Backup and migration - Easily backup, restore, or move data between different environments.
5). Log storage - Persist application logs outside containers for monitoring and debugging.

## Mount Binds in Docker (01:50:01)

Q. What are Bind Mounts?
# Bind mounts are a way to directly map a directory or file from the host machine into a container. Unlike Docker volumes, bind mounts use the absolute path of the host filesystem.

# Key characteristics of Bind Mounts :-
- The host directory/file is mounted directly into the container
- Changes made in the container are immediately reflected on the host (and vice versa)
- The host path must exist before mounting
- Uses the -v or --mount flag with absolute paths

# Command to mount bind - `docker run -v C:/Users/Narotam/Desktop/docker_learning/python-demo-project/server.txt:/myapp/server.txt --rm c4ba6fe4560f`

# Above command demonstrates a file-level bind mount for sharing a specific configuration or data file between host and container.

# What it does:
- Mounts the host file server.txt from the Windows desktop into the container at /myapp/server.txt
-  Runs container c4ba6fe4560f with --rm flag (auto-removes container after execution)

# Use case:
- Configuration sharing :- The server.txt likely contains server settings, connection strings, or application config
- Live updates :- Changes to the host file immediately reflect in the running container
- Development/testing :- Quickly test different configurations without rebuilding the image

Q. What is .dockerignore?
# `.dockerignore` is a file that tells Docker which files and directories to exclude when building a Docker image context.

# Purpose of `.dockerignore`:-
- Reduces build context size and speeds up builds
- Prevents sensitive files from being copied into images
- Excludes unnecessary files that don't belong in the container

# How it works:
- Place .dockerignore in the same directory as your Dockerfile
- Uses glob patterns similar to .gitignore
- Applied before any COPY or ADD commands in Dockerfile

# Communication From/To Containers :-
- From Container to Application
- From Local Machine DB to Container
- From Container to Container

## Working with APIs (02:01:47)

# If we are using any third by package or library to make API call then we nee dto install that package or library in container by specifying the install command.

## Container with Local DB (02:05:58)

# Communication Container & Local DB 

# We can't connect to DB using `localhost` as host instead we need to use `host.docker.internal`

# host.docker.internal is a special DNS name that resolves to the host machine's IP address from within a Docker container.

# Main use cases:
- Accessing host services :- When our containerized app needs to connect to services running on the host machine (like databases, APIs, or development servers)
- Development workflows :- Common in local development when we want a container to talk to services running directly on your laptop/desktop
- Cross-platform compatibility :- Works consistently across Windows, macOS, and Linux Docker Desktop,

# Example: If we have a web app in a container that needs to connect to a MySQL database running on your host machine, we'd use `host.docker.internal:3306` instead of `localhost:3306`.

# Note: This is primarily for Docker Desktop. On Linux with Docker Engine, you might need to use the actual host IP or add --add-host=host.docker.internal:host-gateway to your docker run command.

## Project with Multiple Containers (02:13:35)

# Communication between Containers :

# Command  - `docker run -d --env MYSQL_ROOT_PASSWORD="your_db_password" --env MYSQL_DATABASE="demodb"  --name mysqldb mysql`

# Above Docker command creates and runs a MySQL database container:
# `docker run` - Creates and starts a new container
# `-d` - Runs in detached mode (background)
# `--env MYSQL_ROOT_PASSWORD="your_db_password"` - Sets the root user password
# `--env MYSQL_DATABASE="demodb"` - Creates a database named "demodb" on startup
# `--name mysqldb` - Names the container "mysqldb"
# `mysql` - Uses the official MySQL image

# The container runs MySQL in the background with a root password and automatically creates the "demodb" database.

## Creating Docker Network (02:23:28)

# Command to create network in docker :- `docker network create my-net`

# If we are communicating with multiple containers then we can create docker network to run those multiple containers in same network with ease.

## What is Docker Compose (02:30:04)

# Docker compose is a configuration file to manage multiple containers running to same machine.

# Previously we used to run multiple containers using Docker Network where we need to pass a lot of information in the command that is too tricky and not a efficient way to run, so in order to avoid such things we should prefer using Docker Compose.

# Docker Compose useful commands

# Basic operations 
1). `docker-compose up` - Start all services defined in docker-compose.yml
2. `docker-compose up -d` - Start services in background (detached mode)
3. `docker-compose down` - Stop and remove all containers, networks
4. `docker-compose start` - Start existing stopped containers
5. `docker-compose stop` - Stop running containers without removing them
6. `docker-compose restart` - Restart all services

# Building & Images:
- `docker-compose build` - Build/rebuild images for services
- `docker-compose pull` - Pull latest images for all services

# Cleanup:
- `docker-compose down -v` - Stop services and remove volumes
- `docker-compose down --rmi all` - Stop services and remove images

## docker-compose with Multiple Containers (02:38:12)

## Docker compose with network (02:52:44)

# commands to watch list of networks available in docker :- `docker network ls`

# docker-compose with volume (02:58:58)

# We can add volumes with docker-compose as well to persist data

## docker-compose with ports (03:03:26)

# Docker Compose Summary (03:05:32)

# Docker Compose is a config file that make our task of managing and running containers easy. We can get rid of repetitive commands. All the services inside the config file share same network.

# Docker Compose useful commands
--> docker-compose up/down
--> -d detach Mode
--> -v to remove networks/volumes upon stop
--> --build to again build image and run