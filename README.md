# Comparing Request- and Event-Driven Microservices in a Container Cluster
This is the repository used for the Bachelor thesis of Jim Teräväinen and Martin Kuiper. All code is made available with all rights waived and may be used for further research, personal projects and anything else.

## Purpose
This code was used to try and answer our research question:

How does the choice of a request- or event-driven architecture affect the behaviour of a microservices application running in a container cluster, in regards to:
* Response time from initial request to final response.
* Throughput of total possible reactions or responses during a time period.
* Functionality of the application during updates of services.
* Reliability regarding the number of errors as a consequence of the communication strategy.

# How to use
## Installation
### Windows
1. Install WSL (Windows Subsystem for Linux).
2. Install Docker.
3. Install Minikube.
4. Hard Restart PC.
5. Try starting Minikube by using powershell as shown below. If it does not work, try restarting again or enabling virtualization in BIOS.
```powershell
minikube start
```
6. Install kubectl using powershell.
```powershell
minikube kubectl -- get po -A
```
## Request-Driven Application
Start minikube cluster.
```bash
minikube start
```
Apply the request-driven yaml file to automatically create all deployments and services. The following command assumes the terminal is currently in the project folder.
```bash
kubectl apply -f ./request-driven/request-driven.yaml
```
Now simply find the IP of the api service and then you may make get-requests using your browser or any tool of your choice.
```bash
minikube service rd-api-service --url
```
## Event-Driven Application
Start minikube cluster.
```bash
minikube start
```
Apply the YAML file for the RabbitMQ custom resource cluster. For Windows: add "" around the url.
```bash
kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
```
Apply the YAML file for the RabbitMQ StatefulSet. The following command assumes the terminal is currently in the project folder. NOTE: The RabbitMQ service is slow to start and might need a minute before becoming available.
```bash
kubectl apply -f ./event-driven/definition.yaml
```
Apply the event-driven yaml file to automatically create all deployments and services. The following command assumes the terminal is currently in the project folder.
```bash
kubectl apply -f ./event-driven/event-driven.yaml
```
Now simply find the IP of the api service and then you may make get-requests using your browser or any tool of your choice.
```bash
minikube service ed-api-service --url
```
