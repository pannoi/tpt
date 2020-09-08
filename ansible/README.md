# Ansible

## Info
Ansible on väga paindlik ja lihtne vahend kirjutamise skripte automatioon stsenaariumid  mis tahes keerukust. Saate kirjeldada    seda , Kuidas  lihtne arendaja keskkonnas nii keeruline suur multi-keskkond projekti (dev/etapp/prod).

> Official documentation: http://docs.ansible.com/
# Install

> Ubuntu

Esmalt peate värskendama paketid, mis on garanteeritud saada uusim versioon on mõistlik me vajame
```bash
sudo apt update
```
Samuti tasub ajakohastada paketid, mis on juba paigaldatud
```bash
sudo apt upgrade
```

Nüüd paigaldage Ansible
```bash
sudo apt install ansible
```
Veendumaks, et Ansible on installitud, järgige järgmist käsku:
```bash
ansible --versioon
```

Kõik plokid Ansible, olgu see playbooks või vars (muutujad), alustada, mida me ette kirjutada esimene rida faili:
```bash
---
```
# Playbooks

Mõistlik mänguraamatud on võimalus saata käske kaugarvutitega, kasutades skripte. Asemel individuaalselt kasutades Ansible käske eemalt kohandada arvuteid käsurealt, saate kohandada kogu keerukaid keskkondades läbides skripti ühte või mitut süsteemi.

File extension, whether it's playbook/tasks/variable (vars), is .yml

> Block structure in file  playbook.yml
```bash
---
- name: Install Packages
  hosts: all
  become: true
  roles:
    - role: tpt
```

## Tasks

Mõistlikud ülesanded-on ülesanded, mida teostatakse Ansible, paigaldamise tüüp paketid, käivitusteenused, lahtipakkimine, kopeerimine ja nagu. Nende dokumentide jaotisest rollidest/TPT/Tasks leiate näiteid.

Näide ploki ülesanne installida paketid, mis on salvestatud muutuja paketid
```bash
    - name: Install apcahe+php modules 
      apt:
          name: "{{ item }}" 
          update_cache: yes
          state: latest
      with_items: "{{ packages }}"
```

> Saate lugeda kõiki mooduleid siin: https://docs.ansible.com/ansible/2.3/list_of_all_modules.html

## Roles

See on võimalus rühmitada mitu ülesannet üheks Mahutiks, et tõhusalt automatiseerida oma tööd arusaadava kataloogistruktuuri abil.
Rolli struktuur:
```bash
/home/user/ansible:
    playbook.yml
    roles:
        tpt:
            tasks:
                main.yml
            vars:
                main.yml
```
Kaustas vars (Main. YML) saate määrata muutujad, mis võivad talletada teavet (nt rakenduste loend, tekst jne)/vars/Main.YML, näiteks muutujate kohta leiate selles dokumentatsioonis rolle jaotisest/TPT/vars.
