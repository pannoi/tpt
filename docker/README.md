## Docker

### Инфо

Docker - это инструмент, который максимально просто позволяет автоматизировать развертывание приложений и упрощает процесс управления процессами приложения в контейнерах.
Контейнеры похожи на виртуальные машины, но они более гибкие и эффективные, быстрее работают и в большей степени зависят от операционной системы хоста.
Все это позволяет запускать приложения в изолированных процессах внутри контейнера вместе с изолированными ресурсами, которые выделяются под них.

> Официальная документация - https://docs.docker.com/

### Установка
> Debian 9

В начале нужно обновить сущетсвующий список пакетов:

```bash
sudo apt update -y
```

Теперь устанавливаем несколько необходимых пакетов, который позволят менеджеру apt работать через HTTPS:

```bash
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

Нужно добавить специальный ключ GPG для использования официального репозитория Docker:

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

Добавляем репозиторий Docker к источникам APT менеджера:

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
```

Снова обновим базу данных пакетов:

```bash
sudo apt update -y
```

Проверим, что установка будет выполняться из репозитория Docker.
*Проще не использовать репозиторий Debian, чтобы быть уверенным в том, что мы успешно установим Docker последней версии.*

```bash
apt-cache policy docker-ce
```

Примерно следующий вывод (версия может отличаться):

```bash
docker-ce:
  Installed: 5:19.03.8~3-0~debian-stretch
  Candidate: 5:19.03.8~3-0~debian-stretch
  Version table:
 *** 5:19.03.8~3-0~debian-stretch 500
        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
```

Прошу заметить, в моем случае Docker уже установлен.

Устанавливаем Docker:

```bash
sudo apt install docker-ce
```

Чтобы убедиться, что докер установлен и сервис запущен, введите следующие команды:

```bash
sudo systemctl status docker
```
Должно появиться примерно следующие

```bash
root@debian:/home/it# sudo systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: e
   Active: active (running) since Tue 2020-10-20 17:05:00 EEST; 1min 17s ago
	...
```
И проверяем версию
```bash
docker --version
```

### Настройка прав
Чтобы спокойно работать с докером и не вводить постоянно пароль из-под `sudo` и не находиться под `root` пользователем,
нужно добавить вашего пользователя в группу `docker` (Группа создатся автоматически после установки докера).

```bash
sudo usermod -a -G docker NAME
```
Если возникнит ошибка с паролем то попробуйте удалить пароль

```bash
passwd -d NAME
```

```bash
su - NAME
```

### Работа с утилитой командной строки Docker
Просмотреть все доступные команды:

```bash
docker
```

Параметры и информация для конкретной команды:

```bash
docker docker-subcommand --help
```

> Официальная документация: https://docs.docker.com/engine/reference/commandline/docker/

### Создание dockerfile

Для начала, нужно определиться с понятиями и терминами:

`docker file` место, где будут описаны действия, которые вы хотите выполнить.

По этому файлу создается `docker image`.

`docker image` image, на базе которого создатся контейнер.

`docker container` собственно, контейнер, который будем запускать и внутри которого выполняются процессы (крутится приложение)

Перейдите в рабочую директорию, в которой собираетесь работать с докером.
Создайте файл с любым именем, к примеру, `dockerfile` (указывать никакой формат не нужно)
Инструкция для докер файла:


#### Предположим, что мы хотим запустить приложение:

`FROM` какой базовый image вы собираетесь использовать для работы, также - `Docker base image`

`WORKDIR` обозначить рабочую директорию.

`COPY` добавить сюда файлы, которые хотите использовать: скрипты, оформление и т.д.

`RUN` какие команды выполнить для создания вашего имиджа.

`EXPOSE` декларируем TCP порт для использования внутри контейнера.

`CMD` какие команды выполнять внутри контейнера, когда он будет запущен.

> Официальная документация: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

### Работа с Docker образами

Вы можете выполнять поиск доступных образов на Docker Hub с помощью команды `docker` с субкомандой `search`.

Например, чтобы найти образ `Debian`, введите:

```bash
docker search debian
```

Укороченный вариант примерного вывода:

```
NAME                                               DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
ubuntu                                             Ubuntu is a Debian-based Linux operating sys…   10852               [OK]
debian                                             Debian is a Linux distribution that's compos…   3472                [OK]
```

*В столбце `OFFICIAL` `OK` указывает на образ, созданный и поддерживаемый компанией, реализующей проект Docker (официальный образ).*

Чтобы загрузить официальный образ `debian`, введите следующую команду:

```bash
docker pull debian
```

Загруженный образ можно использовать как `base image` для `docker file`.

Создание образа:

```bash
docker build -t "придумайте имя для образа" "куда/укажите директорию"
```

Посмотреть имеющиеся образы:

```bash
docker images
```

Удалить docker image:

```bash
docker image rm -f "имя образа"
```

> Более подробная официальная документация: https://docs.docker.com/engine/reference/commandline/image/

### Контейнеры

Чтобы запустить контейнер, выполните следующую команду:

```bash
docker run -p 80:80
```

*В данном случае указываются порты 80:80, где синтаксис следующий - "порт машины":"порт контейнера"*

Сочетание переключателей `-i` и `-t` предоставит вам доступ к интерактивной командной оболочке внутри контейнера:

```bash
docker run -it "имя образа"
```

> Более подробная официальная документация: https://docs.docker.com/engine/reference/commandline/container/
