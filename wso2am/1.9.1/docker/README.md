# WSO2 AM 1.9.1 Dockerfile

Please note Following

* This image only support clustering with WSO2 Private Paas (Cannot run clustering with standalone)
* You can use this to run API manager as a single docker container with or without mounting external databases
* If you are running with Kubernetes use one of the minion ip as load balancer ip
* Use CONFIG_PARAM_USE_EXTERNAL_LB_FOR_KUBERNETES = true in cartridge if you are using an external lb with Kubernetes
* In VM Scenario, you need a load balancer to run with clustering
* If you are running with clustering, you need to mount external databases as they share dbs.


WSO2 AM 1.9.1 Dockerfile defines required resources for building a Docker image with WSO2 AM 1.9.1

## How to build

(1) Copy AM 1.9.1 binary pack to the packages folder:

* [wso2am-1.9.1.zip](http://wso2.com/api-management/)

(2) Generate template module `wso2am-1.9.1-template-module-<PROJECT_VERSION>.zip` as described in [README.md] (https://github.com/wso2/private-paas-cartridges/blob/master/wso2am/1.9.1/template-module/README.md) under "Creating AM Template Module for Private PaaS" section. Then copy the resulting Zip file to `packages` folder.

(3) Run build.sh file to build the docker image: (This will copy the plugins and template module to the docker image)
```
sh build.sh
```

(4) List docker images:
```
docker images
```

(5) If successfully built docker image similar to following should display
```
wso2/am-1.9.1        4.1.3              ac57800e96c2        2 minutes ago         1.145 GB
```
## Docker environment variables
```
PROJECT_VERSION - WSO2 Private PaaS Cartridge Repo Version
PCA_HOME - Apache Stratos Python Cartridge Agent Home
JAVA_HOME - JAVA HOME
CONFIGURATOR_HOME - WSO2 Private PaaS Configurator Home
WSO2_SERVER_TYPE - WSO2 Carbon Server type
WSO2_SERVER_VERSION - WSO2 Carbon Server version
TEMPLATE_MODULE_NAME - PPaaS Carbon Server template module name
```
