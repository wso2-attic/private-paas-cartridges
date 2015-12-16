WSO2-AS 5.3.0 Template for the Configurator
-------------------------------------------------------------------------------------

###Creating AS Template Module for Private PaaS

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

    CARBON_HOME = <AS_HOME>

---

#### Enable clustering : 

    CONFIG_PARAM_CLUSTERING = true

* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = wka

* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml

---
        
#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.am.domain

* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < AS_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < AS_HOME >/repository/conf/tomcat/catalina-server.xml

---
#### Set worker/manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= worker

 * Used in - < AS_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < AS_HOME >/repository/conf/carbon.xml
 * Used in - < AS_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_WORKER_HOST_NAME = am.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.am.cloud-test.wso2.com

* Used in - < AS_HOME >/repository/conf/axis2/axis2.xml
* Used in - < AS_HOME >/repository/conf/carbon.xml

---

## Following are the config parameters used for setting up external database 
#### Set URL

    CONFIG_PARAM_URL= jdbc:mysql://localhost:3306/

#### Set Username

    CONFIG_PARAM_USER_NAME=root

#### Set Password
```
CONFIG_PARAM_PAMSWORD=root
```
#### Set Driver class name

    CONFIG_PARAM_DRIVER_CLAMS_NAME=com.mysql.jdbc.Driver

#### Set Max Active

    CONFIG_PARAM_MAX_ACTIVE=50

#### Set Max Wait

    CONFIG_PARAM_MAX_WAIT=60000

#### Set test on borrow

    CONFIG_PARAM_TEST_ON_BORROW=true

#### Set validation query
    CONFIG_PARAM_VALIDATION_QUERY=SELECT 1

#### Set validation interval

    CONFIG_PARAM_VALIDATION_INTERVAL=30000

#### Set Local Registry database

    CONFIG_PARAM_REGISTRY_LOCAL1="jdbc/WSO2CarbonDB:REGISTRY_LOCAL1"

#### Set Registry database

    CONFIG_PARAM_REGISTRY_DB="jdbc/WSO2RegistryDB:REGISTRY_DB"

#### Set datasource and shared user database

    CONFIG_PARAM_USER_DB="jdbc/WSO2UMDB:WSO2_USER_DB"

##### Used in 

* < AS_HOME >/repository/conf/user-mgt.xml
* < AS_HOME >/repository/conf/datasources/master-datasources.xml
* < AS_HOME >/repository/conf/registry.xml
