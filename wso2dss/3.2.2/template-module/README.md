WSO2-DSS 3.2.2 Template for the Configurator
--------------------------------------------

###Creating DSS Template Module for Private PaaS

(1) Download the following [security patches](http://product-dist.wso2.com/downloads/carbon/4.2.0/) and copy the 
extracted patch folders to `files/repository/components/patches` directory.

**Security patches**
* patch1262
* patch1261
* patch1095
* patch0955

Final files folder should look like following.

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
│               ├── patch0955
│               │   ├── org.wso2.carbon.webapp.list.ui_4.2.1.jar
│               │   ├── org.wso2.carbon.webapp.mgt_4.2.2.jar
│               │   └── org.wso2.carbon.webapp.mgt.stub_4.2.0.jar
│               ├── patch1095
│               │   └── wss4j_1.5.11.wso2v6.jar
│               ├── patch1261
│               │   ├── org.wso2.carbon.tomcat.ext_4.2.0.jar
│               │   ├── org.wso2.carbon.tomcat.patch_4.2.0.jar
│               │   ├── tomcat_7.0.34.wso2v1.jar
│               │   └── tomcat-ha_7.0.34.wso2v1.jar
│               └── patch1262
│                   └── org.wso2.carbon.webapp.mgt_4.2.2.jar

(2) Build the template module zip file by running the following command.

```
mvn clean install
```

---
### Configuration parameters
Following are the configuration parameters that is used by the template.
You can configure following in the ***module.ini*** file.

#### Read from environment variables :


    READ_FROM_ENVIRONMENT = false
 

---------------------------------------------------------

#### Set the path of product directory :

    CARBON_HOME = <DSS_HOME>

---

#### Enable clustering : 

    CONFIG_PARAM_CLUSTERING = true

* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml

---
        
#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.dss.domain

* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = private-paas

* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < DSS_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < DSS_HOME >/repository/conf/tomcat/catalina-server.xml

---
#### Set worker/manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= worker

 * Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < DSS_HOME >/repository/conf/carbon.xml
 * Used in - < DSS_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_HOST_NAME = dss.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.dss.cloud-test.wso2.com

* Used in - < DSS_HOME >/repository/conf/axis2/axis2.xml
* Used in - < DSS_HOME >/repository/conf/carbon.xml

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

* < DSS_HOME >/repository/conf/user-mgt.xml
* < DSS_HOME >/repository/conf/datasources/master-datasources.xml
* < DSS_HOME >/repository/conf/registry.xml
---------------------------------------------------------

#### Set email related configurations

     CONFIG_PARAM_EMAIL_ADMIN_CONFIG_TARGET_EPR=https://localhost:9443/carbon/admin-mgt/validator_ajaxprocessor.jsp

##### Used in 

* < DSS_HOME >/repository/conf/email/email-admin-config.xml

---------------------------------------------------------

#### Set JVM tunning parameters

     CONFIG_PARAM_JVM_MEMORY_XMS=256m
     CONFIG_PARAM_JVM_MEMORY_XMX=1024m
     CONFIG_PARAM_JVM_MEMORY_MAX_PERM_SIZE=256m

##### Used in 

* < DSS_HOME >/bin/wso2server.sh
---------------------------------------------------------
