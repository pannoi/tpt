## Docker

### Info

Docker - is a tool that automates application deployment as easily as possible and makes it easier to manage application processes in containers.
Containers are similar to virtual machines, but they are more flexible and efficient, work faster and more dependent on the host's operating system.
All of this allows you to run applications in isolated processes inside the container, along with the isolated resources that stand out beneath them.

> Оfficial documentation - https://docs.docker.com/

### Installation
> Debian 9

In the beginning, you need to update the existing list of packages:
```bash
sudo apt update -y
```
Now we're installing a few necessary packages that will allow the apt manager to work through HTTPS:
```bash
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```
Add a special GPG key to use the official Docker repository:
```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```
Add Docker repository to manager's APT sources:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
```
We will re-upgrade the package database:
```bash
sudo apt update -y
```
Let's check that the installation will be performed from the Docker repository. 
*It's easier not to use the Debian repository to make sure we successfully install Docker's latest version.*
```bash
apt-cache policy docker-ce
```
Approximately we get the following conclusion (the version may be different):
```bash
docker-ce:
  Installed: 5:19.03.8~3-0~debian-stretch
  Candidate: 5:19.03.8~3-0~debian-stretch
  Version table:
 *** 5:19.03.8~3-0~debian-stretch 500
        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
```
Please note, in my case Docker has already been installed.

Install Docker:
```bash
sudo apt install docker-ce
```
To make sure the docker is installed and the service is up and running, enter the following commands:
```bash
sudo systemctl status docker
```
```bash
docker --version
```

### Setting up the rights
To work quietly with the docker and not to enter the `sudo` password constantly and not to be under `root` user,
you need to add your user to the  `docker` group (The group will be created automatically after the docker is installed).
```bash
sudo usermod -aG docker "username"
```
```bash
su - "username"
```
### Dealing with The Docker Command Line utility 
See all available commands:
```bash
docker
```
Settings and information for a specific team:
```bash
docker docker-subcommand --help
```
> Official documentation:  https://docs.docker.com/engine/reference/commandline/docker/

### Creating a dockerfile
First, you need to define the concepts and terms:

`docker file` a place where you'll describe the steps you want to do.

`docker image` is created by this file.

`docker image` image, On the basis of which the container will be created.

`docker container` in fact, the container that will run and inside which processes are performed (the application spins)

Go to the work directory where you're going to work with the docker.
Create a file with any name, for example,  `dockerfile` (no format needed) Instruction for the file docker:


#### Suppose we want to run an app:

`FROM` That's the baseline image you're going to use for work, also - `Docker base image`

`WORKDIR` designate the working directory.

`COPY` add here the files you want to use: scripts, design, etc..

`RUN` which commands to perform to create your image.

`EXPOSE` Declare TCP port for use inside the container.

`CMD` what commands to perform inside the container when it is launched.

> Official documentation: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

### Dealing with Docker images
You can search for available images on Docker Hub with the team `docker` with a sub-command `search`.

For example, to find a Debian image, enter:
```bash
docker search debian
```
Shortened version of approximate output:
```
NAME                                               DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
ubuntu                                             Ubuntu is a Debian-based Linux operating sys…   10852               [OK]
debian                                             Debian is a Linux distribution that's compos…   3472                [OK]
```

*In the `OFFICIAL` column `OK` points to an image created and maintained by the company implementing the Docker project (official image). *

To download official image `debian`, enter command:
```bash
docker pull debian
```
The downloaded image can be used as a `base image` for the `docker file`. Image-making:

Creating image:
```bash
docker build -t "enter name" "where/choose directory"
```

View available images:
```bash
docker images
```

Remove docker image:
```bash
docker image rm -f "имя образа"
```
> More information: https://docs.docker.com/engine/reference/commandline/image/

### Containers
To start the container, follow the next command:
```bash
docker run -p 80:80
```
*In this case, the ports of 80:80 are specified, where the syntax is the next - "port of the machine": container port"*

The combination of switches -i and -t will give you access to an interactive command shell inside the container:
```bash
docker run -it "image name"
```
> More information: https://docs.docker.com/engine/reference/commandline/container/
