## Kubernetes

### Info

Kubernetes või "k8s" on tööriist, mis lahendab palju automaatika ja juhtimise küsimusi. See on platvorm nende konteinerite ja teenuste haldamiseks. See lihtsustab häälestamis-ja automatiseerida. Nagu näiteks terraformi olukorras, on olemas valimisprogramme, kus me peame lihtsalt kirjeldama, kuidas meie tulevast taristut näeme, ja kubernetes tegeleb rakendamisega.

Selleks, et töötada k8s meil on kubectl konsooli utiliit, vaid üks, et me saadame oma YAML faile. Keelesätted siin on deklaratiivne, kus Kubernetes otsib ja võrdleb failide väärtust (mis oli muutus). Näiteks kui olete juba kirjeldanud manifesti ja loonud 3 konteinerid, ja seejärel muuta ja panna väärtus 5, siis lihtsalt luua ja lisada 2 rohkem. See ei loo taristut uuesti ja kirjutab need 3 konteinerit ümber koos teiste uute 5-ga.

> Lisateavet Kubernetes vene keeles: https://kubernetes.io/ru/docs/concepts/overview/what-is-kubernetes/

### Architecture and components

> Link ametlike dokumentidega vene keeles: https://kubernetes.io/ru/docs/concepts/overview/components/

### Installation on Windows 10
Link dokumentatsiooni paigaldamiseks: https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
options for installation:
> Linux

> macOS

> Windows

Rakenduse installimineMinikube Abiga Chocolatey ((käivitatud administraatoriõigustega):
```bash
choco install minikube
```

Rakenduse installimineMinikube Abiga Chocolatey ((käivitatud administraatoriõigustega): `Minikube`:
```bash
minikube start # запустить кластер
```

*Te alustate virtuaalmasinat oma hüperviore (minu juhul- Hyper-V)*

```bash
minikube status # check cluster status
```

```bash
minikube stop # stop cluster work
```

```bash
minikube delete # stop cluster work
```

Paigaldage kubectl koos Chocolatey (käivitatud administraatori õigustega):
```bash
choco install kubernetes-cli
```

> Järgmisena peame kubectl. exe faili üle kanda kausta system32.


Kontrollige installitud versiooni:
```bash
kubectl version --client
```

### Working with Kubernetes
Nüüd saate töötada oma klastri kaudu CLI tööriista kubectl.

> Lisateabe saamiseks: https://kubernetes.io/ru/docs/setup/learning-environment/minikube/#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%BC

#### Namespace
Kui olete käivitanud minikube Start käsk ja virtuaalne masin on läinud, saate liikuda luua nimeruumi ja seadistamise YAML faile. Peaaegu kõik Kubernetes ressursid (kookonid, teenused jne) on niinimetatud nimeruumi ruumid. Nimeruumid on virtuaalsed klastrid. Nimeruumid on klastri ressursside eraldamise viis.

Klastri olemasolevate nimeruumide loetlemiseks kasutage järgmist käsku:

```bash
kubectl get namespace
```

Klastri olemasolevate nimeruumide loetlemiseks kasutage järgmist käsku:
```bash
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```

Luua `namespace`:

```bash
kubectl create namespace "имя"
```

Emaldada `namespace`:

```bash
kubectl delete ns "имя"
```

### Dealing with other objects

Nagu nimiruumi, saate töötada teiste ressurssidega.

Saate teavet kuvada ja kustutada.

Tooge kõik välja.

```bash
kubectl get all
```

Seoses nimede ruumina:

```bash
kubectl get all -n "namespace"
```

Eemaldada:

```bash
kubectl delete "что" "имя" -n "namespace"
```

Vaata kirjeldust:
```bash
kubectl describe "что" "имя" -n "namespace"
```

> ОAmetlikud dokumendid:
>> https://kubernetes.io/ru/docs/concepts/overview/working-with-objects/namespaces/
>> https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

#### Writing manifestos

Järgmisena saate juba oma manifesti kirjeldusega tegeleda, kus kõik vajalikud ressursid on.

Näiteks:  pod, service, deployment.

> Pod

```bash
apiVersion: v1
kind: Pod
metadata:
  name: "name pod "
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
  name: "имя deployment"
  namespace: "имя namespace"
```

>> official documantation: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

> For more information to learn about YAML file configurations:
>> https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
>> https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

#### Kontrolli,  Rakenda  ja  Käivita

Rakenda oma YAML-failid ükshaaval, järgmise käsuga:

```bash
kubectl apply -f "имя манифест файла" (с расширением .yml)
```

To make sure your service is available to the rest of us, enter the team:

```bash
minikube service list
```

To check the health of the service, you can use the next command:

```bash
minikube service "имя сервиса" -n "имя namespace"
```

#### Docker in Kubernetes
Kubernetes kasutab Docker konteineriga töötamiseks. PowerShelli abil saate töötada Windows keskmise suurusega, kus te toetate sama konteineri ja keskmise suurusega pildi käsud keskmise suurusega käsu utiliidi abil. Võite kasutada ka dockerhub töötamiseks keskmise suurusega:


> https://hub.docker.com/

An example of the authentication process on DockerHub with CLI commands:

> https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html
