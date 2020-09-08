## Helm

### Info

Helm-on paketi Manager for Kubernetes. Helm aitab teil hallata rakendusi Kubernetes-helm diagrammid aitavad teil tuvastada, installida ja värskendada rakendusi Kubernetes. See on diagrammi haldamise vahend,   mis käivitab ka  rakendusi Kubernetes.
Он является инструментом для управления чартами и запускает приложения в Kubernetes.

Diagramm kirjeldab andmekomplekti, mis on vajalik rakenduse koopia loomiseks klastri Kubernetes. See võib olla manustatud diagrammid ja kasutatakse nii kirjeldada täiskohaga teenuseid, mis koosnevad paljudest sõltuvad ressursid, ja kirjeldada üksikuid iseseisvaid komponente.

Diagramme on lihtne luua, saate ühiskasutusse anda ja avaldada.

Helmi poliitika on anda parim viis Kubernetes alusel loodud rakenduste leidmiseks, jagamiseks ja kasutamiseks.

> Official documentation: https://helm.sh/

### Background

> Kui olete kohandatud Kubernetes, võite selle sammu vahele jätta.
Selleks, et töötada helmiga, peab teil olema Minikube ja töökäsuliini utiliit kubectl.
Veenduge, et teil on kuubik ja teil on nimeruumi. Kui ei, siis loo.


```bash
minikube start
```

```bash
kubectl create "имя namespace"
```

Check service:

```bash
minikube service $SVC_NAME -n $NAMESPACE
```

> Подробнее: https://github.com/pannoi/tpt/tree/master/kubernetes

### Installation
> Skripti kasutamine:

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

> С помощью Chocolatey (Windows)

```bash
choco install kubernetes-helm
```

Helmi saab paigaldada ka teistesse süsteemidesse ja muul viisil:

> Official documentation: https://helm.sh/docs/intro/install/

### Charts

Jällegi diagramm-on kogum faile, mis kirjeldavad lingitud komplekti Kubernetes ressursse. Enamik diagramme koosneb YAML failide kogumist.

Charti loomine:


```bash
helm create "имя"
```

Käivitage diagramm:

```bash
helm install $CHART_NAME $PATH/TO/HELM --namespace=$NAMESPACE_NAME
```

> Tegelemine graafikuid (YAML failide kogumine) helm ja üksikasjalikuma dokumentatsiooni näiteid:  https://helm.sh/docs/topics/charts/

> See võib olla kasulik: https://www.youtube.com/watch?v=Zzwq9FmZdsU - Siin on näited diagrammiehituse
