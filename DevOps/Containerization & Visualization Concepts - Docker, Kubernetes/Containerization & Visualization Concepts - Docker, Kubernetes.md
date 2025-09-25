# Virtualization & Containerization

## Virtualization
Creates Virtual Version of a computing resource.

### Types
1. **Virtual Machine**: Simulated Computer Systems inside another computer. It has its own OS and Applications. It's an emulation of a computer.

## Containerization
Isolated Environment. Packaging software with dependencies into isolated units. Uses OS-level virtualization. Ensures consistent behavior across environments.

### Characteristics of Containers
1. Reliably run multiple applications on a single host
2. Each application has its own container

### Benefits
1. **Isolation**: Do not interfere with other applications. If one crashes it won't affect others
2. **Portability & Reproducibility**

### Use Cases
1. **Microservice Architecture**: Software design where applications are split into small, independent services
2. **Container Orchestration**: Automating deployment, scaling, and management of containers. Uses Declarative Programming

### OS Level Virtualization
Virtualizing the Operating System itself, rather than the entire computer. This is also called "Containerization".

---

# Docker

Building, Distributing, Running applications using containers.

## Components

### 1. Docker Desktop
GUI for managing applications and containers

### 2. Docker Daemon
Core service responsible for building, running and managing docker objects. Needs to be running whenever you use docker

### 3. Docker Objects
- **Images**: Docker File → Image (Blueprint)
- **Containers**: Image → Containers

### 4. Docker Hub
Centralized location for storing and managing container images

## Docker Instructions

- **FROM**: Specifies starting point, defines the image we are building on
- **COPY**: Copy files needed in following docker instructions
- **RUN**: Run a command within a container
- **ENTRYPOINT**: Defines default behavior. Specifies command to run at initiation. Primary purpose of the container
- **docker build**: Builds Docker Image from docker file
- **docker run**: Creates and runs Docker Container from Docker image

---

# Kubernetes

Grouping containers into logical units. Distributed system.

## Components

### 1. Pod
- Consists of One or more containers
- Smallest deployable unit
- Unique environment where applications run

### 2. Node
- One or more pods
- Serve as hosts where pods run
- Smallest unit of computing hardware
- A specific pod does not always run on the same node

### 3. Control Plane
- Manages Nodes & Pods
- Smartly assigns pods to available nodes
- Brain of the cluster

### 4. Cluster
Group of multiple thousands of nodes

---

# Software Tools

- **Container Management**: Docker
- **Container Automation**: Kubernetes (Automatically managing and Coordinating multiple containers)
- **Virtualization**: Oracle VM VirtualBox, VMware