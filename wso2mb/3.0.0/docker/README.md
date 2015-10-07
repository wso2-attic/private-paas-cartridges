# WSO2 MB 3.0.0 Dockerfile

WSO2 MB 3.0.0 Dockerfile defines required resources for building a Docker image with WSO2 MB 3.0.0.

## How to build

(1) Copy wso2mb-3.0.0 binary pack to the packages folder:

* [wso2mb-3.0.0.zip](http://wso2.com/products/message-broker/)

(2) Generate template module `wso2mb-3.0.0-template-module-<PPAAS_VERSION>.zip` as described in [README.md](https://github.com/wso2/private-paas-cartridges/blob/master/wso2mb/3.0.0/template-module) under "Creating MB Template Module for Private PaaS" section.


(3) Run build.sh file to build the docker image. (This will copy the plugins and template module to the docker image)
```
sh build.sh clean
```

(4) List docker images:
```
docker images
```
(5) If successfully built, docker image similar to following should display.
```
wso2/mb        3.0.0              ac57800e96c2        2 minutes ago         777.6 MB
```
## Docker environment variables
```
PPAAS_VERSION - WSO2 Private PaaS Version
PCA_HOME - Apache Stratos Python Cartridge Agent Home
JAVA_HOME - JAVA HOME
CONFIGURATOR_HOME - WSO2 Private PaaS Configurator Home
WSO2_SERVER_TYPE - WSO2 Carbon Server type
WSO2_SERVER_VERSION - WSO2 Carbon Server version
TEMPLATE_MODULE_NAME - PPaaS Carbon Server template module name
```