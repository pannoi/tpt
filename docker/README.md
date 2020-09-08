## Docker

### Info

Docker-see on vahend, mis automatiseerib rakenduse juurutamine nii lihtne kui võimalik ja lihtsustab rakenduste protsesside konteinerite haldamiseks. Konteinerid sarnanevad virtuaalarvutitele, kuid need on paindlikumad ja efektiivsed, töötavad kiiremini ja sõltuvad vastuvõtva operatsioonisüsteemi süsteemist. Kõik see võimaldab teil käivitada rakendusi isoleeritud protsesside sees konteiner, koos isoleeritud ressursse, mis seisavad välja nende all.

Official documentation >  - https://docs.docker.com/

### Installation
> Debian 9

Alguses peate värskendama olemasolevat pakettide loendit:
```bash
sudo apt update -y
```
Nüüd me paigaldame mõned vajalikud paketid, mis võimaldab apt Manager töötada HTTPS:
```bash
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```
Nüüd me paigaldame mõned vajalikud paketid, mis võimaldab apt Manager töötada HTTPS:
```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```
Lisage Docker hoidla Manager APT allikad:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
```
Uuendame uuesti paketi andmebaasi:
```bash
sudo apt update -y
```
ПKontrollime, et paigaldus toimub Docker hoidla. See on lihtsam mitte kasutada Debian hoidla veendumaks, et me edukalt paigaldada Docker uusim versioon.
```bash
apt-cache policy docker-ce
```
Umbes me saame  järgmise järelduse (versioon võib olla erinev):
```bash
docker-ce:
  Installed: 5:19.03.8~3-0~debian-stretch
  Candidate: 5:19.03.8~3-0~debian-stretch
  Version table:
 *** 5:19.03.8~3-0~debian-stretch 500
        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
```
Pange tähele, minu puhul on Docker juba paigaldatud.

Paigaldage Docker:
```bash
sudo apt install docker-ce
```
Veendumaks, et keskmise suurusega on installitud ja teenus on üles ja töötab, sisestage järgmised käsud:
```bash
sudo systemctl status docker
```
```bash
docker --version
```

### Setting up the rights
Et töötada vaikselt koos keskmise suurusega ja mitte siseneda sudo parooli pidevalt ja mitte olla root kasutaja, peate lisama oma kasutaja keskmise suurusega rühma (rühm luuakse automaatselt pärast keskmise suurusega on paigaldatud).
```bash
sudo usermod -aG docker "имя пользователя"
```
```bash
su - "имя пользователя"
```
### Dealing with The Docker Command Line utility 
Vaata kõiki saadaolevaid käske:
```bash
docker
```
Kindla meeskonna sätted ja teave:
```bash
docker docker-subcommand --help
```
> Official documentation: https://docs.docker.com/engine/reference/commandline/docker/

### Create a dockerfile
Esiteks peate määratlema mõisted ja mõisted:

`docker file` koht, kus saate kirjeldada samme, mida soovite teha.

is created by this file `docker image`.

`docker image` image, Mille põhjal mahuti luuakse.

`docker container` tegelikult, konteiner, mis kestab ja milles protsessid teostatakse (taotluse keerutab)

töökataloogi, kus te töötate koos selle Docker. Loo faili mis tahes nimega, näiteks dockerfile  (vorming pole vajalik) juhend faili keskmise suurusega:


#### Suppose we want to run an app:

`FROM` Tmüts on lähtepilt, mida sa kavatsed kasutada tööks, samuti - `Docker base image`

`WORKDIR` määrata töökataloog.

`COPY` Lisage siia failid, mida soovite kasutada: scripts, design, etc.

`RUN` Milliseid käske teha, et luua oma pilt.

`EXPOSE` Milliseid käske teha, et luua oma pilt.

`CMD` Milliseid käske teha konteineri sees, kui see käivitatakse.

> Official documentation: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

### Dealing with Docker images
Saate otsida saadaolevaid pilte Docker Hub meeskond docker with a sub-command 'search'.

Näiteks, et leida Debian pilt, sisestage:
```bash
docker search debian
```
Ligikaudse väljundi lühendatud versioon:
```
NAME                                               DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
ubuntu                                             Ubuntu is a Debian-based Linux operating sys…   10852               [OK]
debian                                             Debian is a Linux distribution that's compos…   3472                [OK]
```

Aastal ametlik OK veerg osutab pildile, mille on loonud ja mida haldab Docker projekti rakendav ettevõte (ametlik kujutis).

Ametliku Debian pildi allalaadimiseks sisestage järgmine käsk:
```bash
docker pull debian
```
Allalaaditud pilti saab kasutada aluspildina keskmise suurusega faili.

Kujutise tegemine:
```bash
docker build -t "mõtle välja pildi nimi" "kus/punkt kataloog"
```

Kuva saadaolevad pildid:
```bash
docker images
```

Eemalda keskmise suurusega pilt:
```bash
docker image rm -f "имя образа"
```
> More information: https://docs.docker.com/engine/reference/commandline/image/

### Containers
Konteineri käivitamiseks järgige järgmist käsku:
```bash
docker run -p 80:80
```
Sel juhul on määratud pordid 80:80, kus süntaks on järgmine-"masina Port": konteiner Port "

Kombinatsioon lülitid-i ja-t annab teile juurdepääsu interaktiivne käsk Shell sees konteiner:
```bash
docker run -it "имя образа"
```
> More information: https://docs.docker.com/engine/reference/commandline/container/
