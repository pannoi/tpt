# Molecule

## Инфо

Модульное тестирование в Ansible является ключом к тому, чтобы убедиться, что роли работают должным образом. Molecule упрощает этот процесс, позволяя указывать сценарии, тестирующие роли в различных средах. 

Используя Ansible изнутри, Molecule выгружает роли поставщику, который развертывает роль в сконфигурированной среде и вызывает верификатор (например, Testinfra) для проверки дрейфа конфигурации. Это гарантирует, что ваша роль внесла все ожидаемые изменения в среду в этом конкретном сценарии.

> Официальная документация https://molecule.readthedocs.io/en/latest/#

## Подготовка среды

Обновление обеспечит включение в ваш репозиторий последней версии пакета python-pip, который установит pip и Python.

```bash
Sudo apt-get update
``` 

pip будет использоваться для создания виртуальной среды и установки дополнительных пакетов. 

```bash
sudo apt-get install -y python-pip
```

Использование pip для установки модуля Python + virtualenv:

```bash
python -m pip install virtualenv
```

Создание и активирование виртуальной среды:
```bash
python -m virtualenv
```

Активируйте его, чтобы убедиться, что ваши действия ограничены этой средой:
```bash
source my_env/bin/activate
```

Установка molecule и docker с помощью pip:
```bash
python -m pip install molecule docker
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
Тестовую матрицу можно посмотреть в файле molecule.yml, который по дефолту хранится тут:
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
