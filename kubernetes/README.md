## Kubernetes

### Info

Kubernetes or "k8s" is a tool that solves a lot of automation and management issues. It is a platform for managing containers and services deployed in them. It makes it easier to set up and automate. As in the Terraform situation, there are manifestos where we just need to describe how we see our future infrastructure, and kubernetes will be engaged in implementation.

In order to work with k8s we have a kubectl console utility, just one that we will send our YAML files to. 
The language settings here are declarative, where Kubernetes looks and compares the value of the files (which was what became). For example, if you've already described the manifesto and created 3 containers, and then changed and put the value 5, then it will just create and add 2 more. It will not re-create the infrastructure and rewrite these 3 containers with other new 5.


> For more information about Kubernetes in Russian: https://kubernetes.io/ru/docs/concepts/overview/what-is-kubernetes/

### Architecture and components
> Link to official documentation in Russian: https://kubernetes.io/ru/docs/concepts/overview/components/

### Installation on Windows 10
Link to installation documentation: https://kubernetes.io/ru/docs/tasks/tools/install-minikube/ Possible options for installation:
> Linux

> macOS

> Windows

Installing an app `Minikube` with help  `Chocolatey` (launched with admin rights):
```bash
choco install minikube
```

Basic commands to use `Minikube`:
```bash
minikube start # run cluster
```

*You will start a virtual machine in your hyperviore (in my case - Hyper-V)*

```bash
minikube status # check cluster status
```

```bash
minikube stop # stop cluster work
```

```bash
minikube delete # delete cluster
```

Install `kubectl` with help of `Chocolatey` (launched with admin rights):
```bash
choco install kubernetes-cli
```

> Next we need to transfer the `kubectl.exe` file to the `system32` folder.


Check the installed version:
```bash
kubectl version --client
```

### Working with Kubernetes
Now you can work with your cluster through the CLI tool `kubectl`.

> For more information: https://kubernetes.io/ru/docs/setup/learning-environment/minikube/#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%BC

#### Namespace
Once you've launched the minikube start command and the virtual machine has gone up, you can move on to creating namespace and setting up YAML files. 

Almost all of Kubernetes' resources (pods, services, etc.) are in so-called namespace spaces. Name spaces are virtual clusters. 

Name spaces are a way of separating cluster resources.

Use the following command to list existing name spaces in the cluster:


```bash
kubectl get namespace
```

Next, you need to create a `.yml` file and describe `namespace`:
```bash
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```

Create `namespace`:

```bash
kubectl create namespace "имя"
```

Delete `namespace`:

```bash
kubectl delete ns "имя"
```

### Dealing with other objects

Just like with the name space, you can work with other resources.

You can display and delete information.

Bring it all out:


```bash
kubectl get all
```

Regarding the space of names:

```bash
kubectl get all -n "namespace"
```

Remove:

```bash
kubectl delete "что" "имя" -n "namespace"
```

See the description:

```bash
kubectl describe "что" "имя" -n "namespace"
```

> Official documentation: 
>> https://kubernetes.io/ru/docs/concepts/overview/working-with-objects/namespaces/
>> https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

#### Writing manifestos

Next, you can already deal with the description of your manifesto, where all the resources you need will be.

For example: pod, service, deployment.


> Pod

```bash
apiVersion: v1
kind: Pod
metadata:
  name: "pod name"
  namespace: "name namespace"
```

> Service

```bash
apiVersion: v1
kind: Service
metadata:
  name: "service name"
  namespace: "name namespace"
```

>> official documantation: https://kubernetes.io/docs/concepts/services-networking/service/

> Deployment

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: "name deployment"
  namespace: "name namespace"
```

>> official documantation: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

> For more information to learn about YAML file configurations:
>> https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
>> https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

#### Check, apply and run

Apply your YAML files one by one, with the next command:

```bash
kubectl apply -f "name manifesto file" (forat .yml)
```

To make sure your service is available to the rest of us, enter the team:

```bash
minikube service list
```

To check the health of the service, you can use the next command:

```bash
minikube service "service name" -n "name namespace"
```

#### Docker в Kubernetes
Kubernetes uses Docker to work with containers. You can use `Powershell` to work with the Docker in Windows, where you're supported by the same container and docker image commands using the Docker command utility. 

You can also use DockerHub to work with a `docker`:

> https://hub.docker.com/

An example of the authentication process on DockerHub with CLI commands:

> https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html
