WSO2-GREG 5.0.0 Template for the Configurator
---------------------------------------------

###Creating GREG Template Module for Private PaaS

(1) Copy [mysql-connector-java-5.1.xx-bin.jar](http://dev.mysql.com/downloads/connector/j/) file to `<template_module_home>/files/repository/components/lib` folder. (Folder structure needs to be created.)

(2) Copy `<private_paas_home>/extensions/carbon/ppaas-membership-scheme/target/ppaas-membership-scheme-4.1.0-SNAPSHOT.jar` file to `<template_module_home>/files/repository/components/dropins` folder.

(3) Copy following jar files to `<template_module_home>/files/repository/components/dropins` folder.

 * activemq_client_5.10.0_1.0.0.jar
 * geronimo_j2ee_management_1.1_spec_1.0.1_1.0.0.jar
 * hawtbuf_1.9_1.0.0.jar 
 * org.apache.commons.lang3_3.1.0.jar
 * org.apache.stratos.common-4.1.0.jar
 * org.apache.stratos.messaging-4.1.0.jar


(4) Final files folder should look like following.

files
└── repository
    └── components
        ├── dropins
        │   ├── activemq_client_5.10.0_1.0.0.jar
        │   ├── geronimo_j2ee_management_1.1_spec_1.0.1_1.0.0.jar
        │   ├── hawtbuf_1.9_1.0.0.jar
        │   ├── org.apache.commons.lang3_3.1.0.jar
        │   ├── org.apache.stratos.common-4.1.0.jar
        │   ├── org.apache.stratos.messaging-4.1.0.jar
        │   └── ppaas-membership-scheme-4.1.0-SNAPSHOT.jar
        └── lib
            └── mysql-connector-java-5.1.34-bin.jar


(5) Build the template module with above files.

	mvn clean install

---
### Configuration parameters
Following are the configuration parameters that is used by the template.
You can configure following in the ***module.ini*** file.

#### Read from environment variables :


    READ_FROM_ENVIRONMENT = false
 

-------------------------------------------------------------------------------------

#### Set the path of product directory :

    CARBON_HOME = <GREG_HOME>

---

#### Enable clustering : 

    CONFIG_PARAM_CLUSTERING = true

* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = private-paas

* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml

---
        
#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.greg.domain

* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < GREG_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < GREG_HOME >/repository/conf/tomcat/catalina-server.xml

---
#### Set manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= mgt

 * Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < GREG_HOME >/repository/conf/carbon.xml
 * Used in - < GREG_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_WORKER_HOST_NAME = greg.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.greg.cloud-test.wso2.com

* Used in - < GREG_HOME >/repository/conf/axis2/axis2.xml
* Used in - < GREG_HOME >/repository/conf/carbon.xml

---

## Following are the configuration parameters used for setting up external databases 

---------------------------------------------------------
## Local Registry database configurations
#### Set URL
    CONFIG_PARAM_LOCAL_REGISTRY_DB_URL=jdbc:mysql://localhost:3306/local_reg_db?autoReconnect=true
#### Set Username
    CONFIG_PARAM_LOCAL_REGISTRY_DB_USERNAME=root
#### Set Password
    CONFIG_PARAM_LOCAL_REGISTRY_DB_PASSWORD=root
#### Set Driver class name
    CONFIG_PARAM_LOCAL_REGISTRY_DB_DRIVER=com.mysql.jdbc.Driver
---------------------------------------------------------

## Registry database configurations
#### Set URL
    CONFIG_PARAM_REGISTRY_DB_URL=jdbc:mysql://localhost:3306/reg_db?autoReconnect=true
#### Set Username
    CONFIG_PARAM_REGISTRY_DB_USERNAME=root
#### Set Password
    CONFIG_PARAM_REGISTRY_DB_PASSWORD=root
#### Set Driver class name
    CONFIG_PARAM_REGISTRY_DB_DRIVER=com.mysql.jdbc.Driver
---------------------------------------------------------

## Config database configurations
#### Set URL
    CONFIG_PARAM_CONFIG_DB_URL=jdbc:mysql://localhost:3306/config_db?autoReconnect=true
#### Set Username
    CONFIG_PARAM_CONFIG_DB_USERNAME=root
#### Set Password
    CONFIG_PARAM_CONFIG_DB_PASSWORD=root
#### Set Driver class name
    CONFIG_PARAM_CONFIG_DB_DRIVER=com.mysql.jdbc.Driver
---------------------------------------------------------

## User managemnet database configurations
#### Set URL
    CONFIG_PARAM_USER_MGT_DB_URL=jdbc:mysql://localhost:3306/user_db?autoReconnect=true
#### Set Username
    CONFIG_PARAM_USER_MGT_DB_USERNAME=root
#### Set Password
    CONFIG_PARAM_USER_MGT_DB_PASSWORD=root
#### Set Driver class name
    CONFIG_PARAM_USER_MGT_DB_DRIVER=com.mysql.jdbc.Driver
---------------------------------------------------------

##### Used in 

* < GREG_HOME >/repository/conf/user-mgt.xml
* < GREG_HOME >/repository/conf/datasources/master-datasources.xml
* < GREG_HOME >/repository/conf/registry.xml
---------------------------------------------------------

#### Set JVM tunning parameters

     CONFIG_PARAM_JVM_MEMORY_XMS=256m
     CONFIG_PARAM_JVM_MEMORY_XMX=1024m
     CONFIG_PARAM_JVM_MEMORY_MAX_PERM_SIZE=256m

##### Used in 

* < GREG_HOME >/bin/wso2server.sh
---------------------------------------------------------


(6) Since GReg does not require syncing of deployed artifacts between nodes, it is not required to enable deployment synchronizer features. Hence not reuired to configure Sign-up repo details (URL/ username/ password) in Private-Paas for the application.
