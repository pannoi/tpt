## Helm

### Info

Helm - is a package manager for Kubernetes. Helm helps you manage apps in Kubernetes - Helm Charts help you identify, install, and update apps on Kubernetes. It is a chart management tool which also launches apps in Kubernetes.

Chart describes the data set needed to create a copy of the app in the Kubernetes cluster. It can have embedded charts and is used both to describe full-fledged services consisting of many dependent resources, and to describe individual independent components.

Charts are easy to create, you can share and publish.

Helm's policy is to give the best way to find, share and use apps built under Kubernetes.


> Official documentation: https://helm.sh/

### Background

> If you have customized Kubernetes, you can skip this step.

To work with the helm, you must have a `Minikube` and a working command line utility `kubectl`.

Make sure you have a cube running and have a namespace. If not, create.

```bash
minikube start
```

```bash
kubectl create "name namespace"
```

Check service:

```bash
minikube service $SVC_NAME -n $NAMESPACE
```

> more info: https://github.com/pannoi/tpt/tree/master/kubernetes

### Installation
> Using the script:

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

> Using Chocolatey (Windows)

```bash
choco install kubernetes-helm
```

Helm can also be installed on other systems and other ways:

> Official documentation: https://helm.sh/docs/intro/install/

### Charts

Once again, chart - is a collection of files that describe a linked set of Kubernetes resources. Most of the charts consist of a collection of `YAML` files.

Create chart:

```bash
helm create "name"
```

Start the chart:

```bash
helm install $CHART_NAME $PATH/TO/HELM --namespace=$NAMESPACE_NAME
```

> Dealing with charts (`YAML` files collection) in Helm and more detailed documentation with examples: https://helm.sh/docs/topics/charts/

> It may be useful: https://www.youtube.com/watch?v=Zzwq9FmZdsU - here are the examples of chart-building
