# Molecule

## Инфо

Модульное тестирование в Ansible является ключом к тому, чтобы убедиться, что роли работают должным образом. Molecule упрощает этот процесс, позволяя указывать сценарии, тестирующие роли в различных средах. 

Используя Ansible изнутри, Molecule выгружает роли поставщику, который развертывает роль в сконфигурированной среде и вызывает верификатор (например, Testinfra) для проверки дрейфа конфигурации. Это гарантирует, что ваша роль внесла все ожидаемые изменения в среду в этом конкретном сценарии.

> Официальная документация https://molecule.readthedocs.io/en/latest/#

> Для работы используйте:
molecule==2.20
ansible==2.7

## Подготовка среды

Перед установкой надо установить на свою виртуальную машину Docker и Python3

## Docker

 Первым делом обновите существующий список пакетов
 
```bash
sudo apt update
```

Затем установите несколько необходимых пакетов, которые позволяют apt использовать пакеты через HTTPS

```bash
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

Добавьте ключ GPG для официального репозитория Docker в вашу систему

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

Добавьте репозиторий Docker в источники APT

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
```

Потом обновите базу данных пакетов и добавьте в нее пакеты Docker из недавно добавленного репозитория

```bash
sudo apt update
```

Установите Docker

```bash
sudo apt install docker-ce
```

Проверить установку Docker`a

```bash
docker –version
```

Если выдает ошибку то попробуйте

```bash
apt-get update && apt-get upgrade
```

```bash
apt-get dist-upgrade
```

## Python3

Начать необходимо с установки пакетов, необходимых для сборки исходного кода Python

```bash
sudo apt update
```

```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wge
```

Загрузить исходный код последней версии со страницы загрузки Python, используя следующую команду curl

```bash
curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
```

После скачивания необходимо разархивировать

```bash
tar -xf Python-3.7.3.tar.xz
```

Перейдите в каталог Python и запустите скрипт configure, который выполнит ряд проверок, чтобы убедиться, что все зависимости в системе присутствуют

```bash
cd Python-3.7.3
```

```bash
./configure --enable-optimizations
```

Запустите make, чтобы начать процесс сборки

```bash
make -j 8
```

После завершения сборки установите двоичные файлы Python

```bash
sudo make altinstall
```

На данный момент Python 3.7 установлен в вашей системе Debian и готов к использованию. Вы можете проверить это, набрав

```bash
python3.7 –version
```

## Molecule

Обновление обеспечит включение в ваш репозиторий последней версии пакета python-pip, который установит pip и Python.

```bash
sudo apt-get update
``` 

pip будет использоваться для создания виртуальной среды и установки дополнительных пакетов. 

```bash
sudo apt-get install -y python3-pip
```

Использование pip для установки модуля Python + virtualenv:

```bash
python3 -m pip install virtualenv
```

Создание и активирование виртуальной среды:

```bash
python3 -m virtualenv env_name
```

Активируйте его, чтобы убедиться, что ваши действия ограничены этой средой:

```bash
source env_name/bin/activate
```

Установка molecule и docker с помощью pip:

```bash
python -m pip install molecule docker
```

Если после предедущей команды появилась ошибка

```bash
WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
You should consider upgrading via the '/home/it/bred2/bin/python3 -m pip install --upgrade pip' command.
```
поробуйте команду

```bash
pip install --upgrade pip
```

## Создание роли в Molecule

```bash
molecule init role -r role-name -d docker
```

Флаг -r указывает имя роли, в то время как -d указывает драйвер, который предоставляет хосты для Molecule для использования в тестировании.

Чтобы перейти в каталог созданной роли, нужно выполнить следующую команду:

```bash
cd role-name
```

## Файл конфигурации molecule.yml

Перед началом теста Molecule проверяет конфигурационный файл molecule.yml, чтобы убедиться, что все в порядке. Он также печатает эту тестовую матрицу, которая определяет порядок тестовых действий.
Тестовую матрицу можно посмотреть в файле molecule.yml, который по умолчанию хранится тут:

> /home/username/role-name/molecule/default/molecule.yml

## Тестирование роли

Проверьте роль по умолчанию, чтобы проверить, правильно ли настроена Молекула:

```bash
molecule test
```

Вывод при тестировании выглядит следующим образом:

```bash
Output
--> Validating schema /home/username/role-name/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── lint
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    └── destroy
...
```
