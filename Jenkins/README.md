# Terraform 

## Info

Terraform – see on vahend Hashicorp, mis aitab hallata infrastruktuuri deklaratiivselt. Sellisel juhul ei pea te pilveteenuse pakkuja konsoolis käsitsi looma eksemplare, võrke jne. lihtsalt kirjuta konfiguratsioon, mis ütleb teile, kuidas sa näed oma tulevase infrastruktuuri. See konfiguratsioon on loodud inimloetavas tekstivormingus. Kui soovite oma infrastruktuuri muuta, redigeerige konfiguratsiooni ja käivitage rakendus. Terraform saadab API kõned pilve pakkuja ühtlustada infrastruktuuri konfiguratsiooni selles failis.

Terraform – see on vahend Hashicorp, mis aitab hallata infrastruktuuri deklaratiivselt. Sellisel juhul ei pea te pilveteenuse pakkuja konsoolis käsitsi looma eksemplare, võrke jne. lihtsalt kirjuta konfiguratsioon, mis ütleb teile, kuidas sa näed oma tulevase infrastruktuuri. See konfiguratsioon on loodud inimloetavas tekstivormingus. Kui soovite oma infrastruktuuri muuta, redigeerige konfiguratsiooni ja käivitage rakendus. Terraform saadab API kõned pilve pakkuja ühtlustada infrastruktuuri konfiguratsiooni selles failis.

> Official documentation: https://www.terraform.io/docs/index.html

## Installation

Teil on vaja paigaldada muutmis  terraform [official provider](https://www.terraform.io/), nüüd me kasutame versiooni: `terraform version == v0.11.11`

Windows

1. Download Terraform `.zip` and extract it Win 10 from [here](https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_windows_amd64.zip);
2. Move extracted .exe file to `C:\Windows\System32\`

Linux

1. Download Terraform `.zip` and extract it Win 10 from [here](https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip);
2. Move extracted file to `/usr/bin`

## Authentication

Selleks, et autentida pilve, koos, on vaja kasutada autentimise kinnitamiseksg.

    ```bash
    az login
    ```

## Initialization

Sisselõiked protsess hakkab paigaldus hangub ja moodulid, mida kasutada skripti

```bash
terraform init
```

## Configure the variables

Kõik muutujad talletatakse variables.tf, saate neid kohandada   juurutamine


## View status

Terraform loobs  -i alguses faili nimega z. tfstate, mis talletab teavet taristu oleku kohta. Selle abil saate luua infrastruktuuri seisundi üksikasjalik vaade

- Detailed view

  ```bash
  terraform show
  ```

- Simplified view

  ```bash
  terraform state list
  ```

## Planning

Enne skripti alustamist on kõige parem näha, millised ressursid on loodud/muudetud/eemaldatud. Selleks kasutage meeskonda ja vaadake, kuidas skripti kasutamine muudab praeguse taristuse

    ```bash
    terraform plan
    ```

## Application

Kui olete näinud, et hoidla on kehtiv, võite käivitada skripti.


    ```bash
    terraform apply
    ```


    ```bash
    terraform apply -auto-approve
    ```

## Conclusions

Platvormi sees saate konfigureerida järeldusi näiteks generaatori abil loodavate ressursside põhjal (nt resource_id)

```bash
terraform output
```

## Destruction

Kui soovite eemaldada selle skriptiga lahtipakitud infrastruktuuri, käivitage:

```bash
terraform destroy
```

> P.S. Kasutab *.tfstate faili, veenduge, et see on olemas
