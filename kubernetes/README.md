## Kubernetes
Kubernetes или "k8s" - это инструмент, который позволяет решать множество вопросов по автоматизации и управлению вашей инфраструктурой.
Это платформа для управления контейнерами и развертываемыми в них сервисами. Она упрощает настройку и автоматизацию.
Как и в ситуации с Терраформом, здесь используются манифесты (`.yml` файлы), где нужно будет просто описать как мы видим нашу будущую инфраструктуру, а уже kubernetes займется выполнением.
Для того, чтобы работать с k8s у нас есть консольная утилита `kubectl`, как раз которой мы будем отправлять наши `YAML` файлы.
Очень важно упомянуть, что язык настройки здесь декларативный. К примеру, если вы уже описали манифест и создали 3 контейнера, а затем изменили и поставили значение 5, то он просто создаст и добавит еще 2.
Он не будет пересоздавать инфраструктуру и перезаписывать эти 3 контейнера другими новыми 5-ю.

> Более подробная документация про `Kubernetes` на русском языке: https://kubernetes.io/ru/docs/concepts/overview/what-is-kubernetes/

### Архитектура и компоненты

> Ссылка на официальную документацию на русском языке: https://kubernetes.io/ru/docs/concepts/overview/components/

### Установка на Windows 10
Ссылка на документацию по установке: https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
Возможные варианты для установки:
> Linux

> macOS

> Windows

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

> Далее нам нужно перенести `kubectl.exe` файл в папку `system32`.


Проверить установленную версию:
```bash
kubectl version --client
```

### Работа с Kubernetes
Теперь вы можете работать со своим кластером через CLI-инструмент `kubectl`.

> Более подробная официальная информация: https://kubernetes.io/ru/docs/setup/learning-environment/minikube/#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%BC

#### Создание namespace
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

Создать `namespace` (2 варианта):

```bash
kubectl create -f "имя"
```

```bash
kubectl create namespace "имя"
```

> Официальная документация: 
>> https://kubernetes.io/ru/docs/concepts/overview/working-with-objects/namespaces/
>> https://kubernetes.io/docs/tasks/administer-cluster/namespaces/


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

> Deployment

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: "имя deployment'а"
  namespace: "имя namespace"
```
