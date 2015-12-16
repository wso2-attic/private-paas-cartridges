WSO2-BPS 3.5.0 Template for the Configurator
--------------------------------------------

###Creating BPS Template Module for Private PaaS

Note: In order to use 'private-paas' membership scheme, you need to build
[carbon 4.4.1](https://github.com/wso2/carbon-kernel/tree/v4.4.1) with
[Private PaaS membership scheme change](https://github.com/wso2/carbon-kernel/pull/391)
and add the resulting jar as a patch to `files/repository/components/patches` directory as below:

```
├── files
│   ├── bin
│   ├── dbscripts
│   ├── lib
│   └── repository
│       └── components
│           ├── dropins
│           ├── lib
│           └── patches
│               ├── patch9999
│               │   └── org.wso2.carbon.core-4.4.1.jar
```

(1) Build the template module zip file by running the following command.

```
mvn clean install
```

---
### Configuration parameters
Following are the configuration parameters that is used by the template.
You can configure following in the ***module.ini*** file.

#### Read from environment variables :


    READ_FROM_ENVIRONMENT = false
 

-------------------------------------------------------------------------------------

#### Set the path of product directory :

    CARBON_HOME = <BPS_HOME>

---

#### Enable clustering : 

    CONFIG_PARAM_CLUSTERING = true

* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = private-paas

* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml

---
        
#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.bps.domain

* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < BPS_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < BPS_HOME >/repository/conf/tomcat/catalina-server.xml

---
#### Set worker/manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= worker

 * Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < BPS_HOME >/repository/conf/carbon.xml
 * Used in - < BPS_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_WORKER_HOST_NAME = bps.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.bps.cloud-test.wso2.com

* Used in - < BPS_HOME >/repository/conf/axis2/axis2.xml
* Used in - < BPS_HOME >/repository/conf/carbon.xml

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

* < BPS_HOME >/repository/conf/user-mgt.xml
* < BPS_HOME >/repository/conf/datasources/master-datasources.xml
* < BPS_HOME >/repository/conf/registry.xml

---------------------------------------------------------

#### Set JVM tunning parameters

     CONFIG_PARAM_JVM_MEMORY_XMS=256m
     CONFIG_PARAM_JVM_MEMORY_XMX=1024m
     CONFIG_PARAM_JVM_MEMORY_MAX_PERM_SIZE=256m

##### Used in 

* < BPS_HOME >/bin/wso2server.sh
---------------------------------------------------------
