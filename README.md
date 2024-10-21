# gRPC Server and Client with Docker

This project contains a gRPC server and client implemented in Python. The server and client are containerized using Docker. This README provides instructions on how to build and run both the server and client containers.

## Prerequisites

- Docker installed on your machine

## Go to the root directory:
- cd q2

## Build Docker Images
Build the Docker images for both the server and client:
- docker build -t grpc-server server
- docker build -t grpc-client client

## Create Docker Network
Create a Docker network to allow communication between the server and client containers:
- docker network create grpc-network

## Run Docker Containers
Run the server and client containers on the custom network:
- docker run -d --network grpc-network --name grpc-server -p 50051:50051 grpc-server
- docker run -it --network grpc-network --name grpc-client grpc-client

## Verify Network Configuration
Ensure that both the server and client containers are attached to the grpc-network:

- docker network inspect grpc-network

## Usage
Usage
Server:
The server will start and listen on port 50051 for incoming gRPC requests.

Client:
The client will prompt you to select an option:
1. Login
2. Logout
3. Exit

Follow the prompts to interact with the server.