# WSO2 Private PaaS base image Dockerfile

WSO2 products base image Dockerfile defines required resources for building a Docker image with WSO2 product prerequisites.

## How to build

(1) Default username is root and password is set to wso2. If you want to disable root user login with credentials, remove following code block from the Docker file.
```
RUN mkdir -p /var/run/sshd
RUN echo 'root:wso2' | chpasswd
RUN sed -i "s/PermitRootLogin without-password/#PermitRootLogin without-password/" /etc/ssh/sshd_config
```

(2) Copy following files to the packages folder:

* [apache-stratos-cartridge-agent-4.1.4.zip ](http://www.apache.org/dyn/closer.cgi/stratos)
* [jdk-7u80-linux-x64.tar.gz](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
* [](Build the configurator and copy the configurator zip)

(3)  Run build.sh file to build the docker image:
```
sh build.sh
```

If you need to use the already build version of the configurator,execute the following command with the input parameter -b
```
sh build.sh -b
```

(4) List docker images:
```
docker images
```
(5) If successfully built docker image similar to following should display
```
wso2/base-image        4.1.2              ac57800e96c2        2 minutes ago         677.6 MB
```
## Docker environment variables
```
PROJECT_VERSION - WSO2 Private PaaS Cartridge Repo Version
PCA_HOME - Apache Stratos Python Cartridge Agent Home
JAVA_HOME - JAVA HOME
CONFIGURATOR_HOME - WSO2 Private PaaS Configurator Home
```
