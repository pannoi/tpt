## Kubernetes

### Инфо

Kubernetes или "k8s" - это инструмент, который позволяет решать множество вопросов по автоматизации и управлению вашей инфраструктурой.
Это платформа для управления контейнерами и развертываемыми в них сервисами. Она упрощает настройку и автоматизацию.
Как и в ситуации с Терраформом, здесь используются манифесты, где нужно будет просто описать как мы видим нашу будущую инфраструктуру, а уже kubernetes займется выполнением.

Для того, чтобы работать с k8s у нас есть консольная утилита `kubectl`, как раз которой мы будем отправлять наши `YAML` файлы.

Язык настройки здесь декларативный, где Kubernetes смотрит и сравнение значения файлов (что было, что стало). К примеру, если вы уже описали манифест и создали 3 контейнера, а затем изменили и поставили значение 5, то он просто создаст и добавит еще 2.
Он не будет пересоздавать инфраструктуру и перезаписывать эти 3 контейнера другими новыми 5-ю.

> Более подробная документация про `Kubernetes` на русском языке: https://kubernetes.io/ru/docs/concepts/overview/what-is-kubernetes/

### Архитектура и компоненты

> Ссылка на официальную документацию на русском языке: https://kubernetes.io/ru/docs/concepts/overview/components/

### Установка
Ссылка на документацию по установке: https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
Возможные варианты для установки:
> Linux

> macOS

> Windows

Перед установкой на win10 вам надо включить гипервизор(hyper-v)

Установите приложение  Chocolatey

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Установка приложения `Minikube` с помощью `Chocolatey` (запущенный с правами администратора):

```bash
choco install minikube
```

Базовые команды для использования `Minikube`:

```bash
minikube start # запустить кластер
```

*У вас запустится виртуальная машина в вашем гипервизоре (в моем случае - Hyper-V)*

```bash
minikube status # проверить статус состояния кластера
```

```bash
minikube stop # остановить работу кластера
```

```bash
minikube delete # удалить кластер
```

Установка утилиты `kubectl` с помощью `Chocolatey` (запущенный с правами администратора):

```bash
choco install kubernetes-cli
```

Далее нам нужно перенести `kubectl.exe` файл в папку `system32`.


Проверить установленную версию:

```bash
kubectl version --client
```

### Работа с Kubernetes
Теперь вы можете работать со своим кластером через CLI-инструмент `kubectl`.

> Более подробная официальная информация: https://kubernetes.io/ru/docs/setup/learning-environment/minikube/#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%BC

#### Namespace
После того, как вы запустили команду `minikube start` и виртуальная машина поднялась, можно переходить к создаю `namespace` и настройки `YAML` файлов.

Почти все ресурсы Kubernetes'a (поды, сервисы и другие) находятся в так называемых пространствах имен - `namespace`.

Пространства имён представляют собой виртуальные кластеры. Пространства имен - это способ разделения ресурсов кластера.

Используйте следующую команду, чтобы вывести список существующих пространств имён в кластере:

```bash
kubectl get namespace
```

Далее, вам нужно создать `.yml` файл и описать `namespace`:
```bash
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```

Создать `namespace`:

```bash
kubectl create namespace "имя"
```

Удалить `namespace`:

```bash
kubectl delete ns "имя"
```

### Работа с остальными объектами

Точно также, как с пространством имен, можно работать и с другими ресурсами.

Можно выводить информацию и удалять их.

Вывести все:

```bash
kubectl get all
```

Относительно пространства имен:

```bash
kubectl get all -n "namespace"
```

Удалить:

```bash
kubectl delete "что" "имя" -n "namespace"
```

Посмотреть описание:

```bash
kubectl describe "что" "имя" -n "namespace"
```

> Официальная документация: 
>> https://kubernetes.io/ru/docs/concepts/overview/working-with-objects/namespaces/
>> https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

#### Написание манифестов

Далее вы можете уже заняться описанием своего манифеста, где будут все нужные вам ресурсы.

К примеру: pod, service, deployment.

> Pod

```bash
apiVersion: v1
kind: Pod
metadata:
  name: "имя пода"
  namespace: "имя namespace"
```

> Service

```bash
apiVersion: v1
kind: Service
metadata:
  name: "имя сервиса"
  namespace: "имя namespace"
```

>> Официальная документация: https://kubernetes.io/docs/concepts/services-networking/service/

> Deployment

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: "имя deployment"
  namespace: "имя namespace"
```

>> Официальная документация: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

> Более подробная информация для изучения конфигураций `YAML` файлов:
>> https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
>> https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

#### Проверка, применение и запуск

Примените ваши `YAML` файлы один за другим, с помощью следующей команды:

```bash
kubectl apply -f "имя манифест файла" (с расширением .yml)
```

Чтобы убедиться в наличии вашего сервиса среди остальных, введите команду:

```bash
minikube service list
```

Для проверки работоспособности сервиса, можете использовать следующую команду:

```bash
minikube service "имя сервиса" -n "имя namespace"
```

#### Docker в Kubernetes
Для работы с контейнерами в Kubernetes используется Docker. Для работы с докером в Windows можно использовать `Powershell`, где поддерживаются все те же команды по работе с контейнерами и образами докера посредством командной утилиты `Docker`.

Также, для работы с докером вы можете использовать DockerHub:

> https://hub.docker.com/

Пример процесса аутентификации на DockerHub c помощью CLI-команд:

> https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html
