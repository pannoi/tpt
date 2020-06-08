# Molecule

## Info

Modulaarne testimine on Ansible on võti veendumaks, et rollid toimivad korralikult. Molekul lihtsustab seda protsessi, võimaldades teil määrata stsenaariumid, mis testima rolle erinevates keskkondades. 

Kasutades Ansible sees, molekuli eemaldab rollide hankija, mis juurutab rolli konfigureeritud keskkonnas ja kutsub kontrollija (nt Testinfra) kontrollida triivi konfiguratsiooni. See tagab, et teie roll on teinud kõik oodatud muudatused keskkonnas selles konkreetses stsenaariumis.

> Official documentation  https://molecule.readthedocs.io/en/latest/#

> Use for work:
molecule 2.20
ansible 2.7

## Preparing the environment

See värskendus tagab, et uusim versioon Python-PIP pakett, mis installib PIP ja Python, sisaldub teie hoidla.

```bash
Sudo apt-get update
``` 

PIP kasutatakse luua virtuaalne keskkond ja paigaldada täiendavaid pakette. 

```bash
sudo apt-get install -y python-pip
```

Kasutades PIP paigaldada Python moodul ja virtualenv:

```bash
python -m pip install virtualenv
```

Virtuaalkeskkonna loomine ja aktiveerimine:
```bash
python -m virtualenv
```

Aktiveerige see veendumaks, et teie tegevus piirdub selle keskkonnaga:
```bash
source my_env/bin/activate
```

Install molecule and docker with pip:
```bash
python -m pip install molecule docker
```

## Creating a role in Molecule
```bash
molecule init role -r role-name -d docker
```
Lipp r näitab rolli nime, kuigi-d näitab draiverit, mis pakub hosts molekuli kasutamiseks testimiseks.

Loodud rolli kataloogi minna, peate käivitama järgmise käsu:
```bash
cd role-name
```

## Configuration file molecule.yml

Enne testi algust kontrollib molekuli molekuli. YML konfiguratsioonifaili veendumaks, et kõik on õige  järjekorras. See prindib ka katsemaatriksi, mis määrab katsemeetmete võtmise viisi. Testmaatriksi võib näha molekuli. YML-failis, mida talletatakse siin vaikimisi:

> /home/username/role-name/molecule/default/molecule.yml

## Role test

Kontrollige vaikerolli, et näha, kas molekul on õigesti seadistatud:
```bash
molecule test
```
Katsetamise järeldus näeb välja selline:
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
