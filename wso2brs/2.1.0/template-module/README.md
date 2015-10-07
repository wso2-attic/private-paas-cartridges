WSO2-BRS 2.1.0 Template for the Configurator
-------------------------------------------------------------------------------------

###Creating BRS Template Module for Private PaaS

(1) Download the following [security patches](http://product-dist.wso2.com/downloads/carbon/4.2.0/) and copy the 
extracted patch folders to `files/repository/components/patches` directory.

**Security patches**
* patch1262
* patch1095
* patch1261
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

```

(2) Build the template module using the following command.

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

    CARBON_HOME = <BRS_HOME>

---

#### Enable clustering :

    CONFIG_PARAM_CLUSTERING = true

* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = wka

* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.brs.domain

* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < BRS_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < BRS_HOME >/repository/conf/tomcat/catalina-server.xml

---
#### Set worker/manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= worker

 * Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < BRS_HOME >/repository/conf/carbon.xml
 * Used in - < BRS_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_WORKER_HOST_NAME = brs.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.brs.cloud-test.wso2.com

* Used in - < BRS_HOME >/repository/conf/axis2/axis2.xml
* Used in - < BRS_HOME >/repository/conf/carbon.xml

---

## Following are the config parameters used for setting up external database

#### Set URL for registry DB

    CONFIG_PARAM_REGISTRY_DB_URL= jdbc:mysql://localhost:3306/registry_db

#### Set Username for registry DB

    CONFIG_PARAM_REGISTRY_DB_USER_NAME=root

#### Set Password for registry DB
```
    CONFIG_PARAM_REGISTRY_DB_PASSWORD=root
```
#### Set Driver class name for registry DB

    CONFIG_PARAM_REGISTRY_DB_DRIVER_CLASS_NAME=com.mysql.jdbc.Driver

#### Set URL for user DB

    CONFIG_PARAM_USER_MGT_DB_URL= jdbc:mysql://localhost:3306/user_db

#### Set Username for user DB

    CONFIG_PARAM_USER_MGT_DB_USER_NAME=root

#### Set Password for user DB
```
    CONFIG_PARAM_USER_MGT_DB_PASSWORD=root
```
#### Set Driver class name for user DB

    CONFIG_PARAM_USER_MGT_DB_DRIVER_CLASS_NAME=com.mysql.jdbc.Driver

##### Used in

* < BRS_HOME >/repository/conf/user-mgt.xml
* < BRS_HOME >/repository/conf/datasources/master-datasources.xml
* < BRS_HOME >/repository/conf/registry.xml