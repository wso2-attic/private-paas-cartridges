WSO2-IS 5.0.0 Template for the Configurator
-------------------------------------------------------------------------------------


###Creating IS Template Module for Private PaaS

(1) Download the following [security patches](http://product-dist.wso2.com/downloads/carbon/4.2.0/) and copy the 
    extracted patch folders to `files/repository/components/patches` directory.

**Security patches**

* patch1270
* patch1268
* patch1262
* patch1261
* patch1256
  - Note: copy authenticationendpoint.war and oauth2.war files in resources folder of this patch to files/repository/deployment/server/webapps folder
* patch1235
* patch1194
* patch1193
* patch1095
* patch0955


Final files folder should look like following.

```
├── files
│   ├── bin
│   ├── dbscripts
│   ├── lib
│   └── repository
│       ├── components
│       │   ├── dropins
│       │   ├── lib
│       │   └── patches
│       │       ├── patch0955
│       │       │   ├── org.wso2.carbon.webapp.list.ui_4.2.1.jar
│       │       │   ├── org.wso2.carbon.webapp.mgt_4.2.2.jar
│       │       │   └── org.wso2.carbon.webapp.mgt.stub_4.2.0.jar
│       │       ├── patch1095
│       │       │   └── wss4j_1.5.11.wso2v6.jar
│       │       ├── patch1193
│       │       │   └── org.wso2.carbon.webapp.mgt_4.2.0.jar
│       │       ├── patch1194
│       │       │   └── org.wso2.carbon.identity.application.authenticator.samlsso_4.2.1.jar
│       │       ├── patch1235
│       │       │   └── org.wso2.carbon.identity.mgt_4.2.2.jar
│       │       ├── patch1256
│       │       │   ├── org.wso2.carbon.identity.core_4.2.3.jar
│       │       │   ├── org.wso2.carbon.identity.sso.saml_4.2.3.jar
│       │       │   ├── org.wso2.carbon.identity.sts.passive.ui_4.2.1.jar
│       │       │   └── org.wso2.carbon.ui_4.2.0.jar
│       │       ├── patch1261
│       │       │   ├── org.wso2.carbon.tomcat.ext_4.2.0.jar
│       │       │   ├── org.wso2.carbon.tomcat.patch_4.2.0.jar
│       │       │   ├── tomcat_7.0.34.wso2v1.jar
│       │       │   └── tomcat-ha_7.0.34.wso2v1.jar
│       │       ├── patch1262
│       │       │   └── org.wso2.carbon.webapp.mgt_4.2.2.jar
│       │       ├── patch1268
│       │       │   ├── org.wso2.carbon.identity.application.authenticator.basicauth_4.2.0.jar
│       │       │   ├── org.wso2.carbon.identity.core_4.2.0.jar
│       │       │   ├── org.wso2.carbon.identity.mgt_4.2.0.jar
│       │       │   └── org.wso2.carbon.user.core_4.2.0.jar
│       │       └── patch1270
│       │           ├── org.wso2.carbon.identity.application.authenticator.basicauth_4.2.1.jar
│       │           ├── org.wso2.carbon.identity.core_4.2.2.jar
│       │           └── org.wso2.carbon.identity.mgt_4.2.1.jar
│       └── deployment
│           └── server
│               └── webapps
│                   ├── authenticationendpoint.war
│                   └── oauth2.war

```

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
 

-------------------------------------------------------------------------------------

#### Set the path of product directory :

    CARBON_HOME = <IS_HOME>

---

#### Enable clustering : 

    CONFIG_PARAM_CLUSTERING = true

* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Membership Schema :

    CONFIG_PARAM_MEMBERSHIP_SCHEME = wka

* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml

---
        
#### Set Domain :

    CONFIG_PARAM_DOMAIN = wso2.am.domain

* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml

---

#### Well known members declaration :

    CONFIG_PARAM_WKA_MEMBERS = "127.0.0.1:4000,127.0.1.1:4001"

* Format - "ip_address1:port1,ip_address2:port2"
* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml

---

#### Set Local Member Hostname and port :

    CONFIG_PARAM_LOCAL_MEMBER_HOST = 127.0.0.1
    CONFIG_PARAM_LOCAL_MEMBER_PORT = 4000

* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml

---

### Set Port offset :

    CONFIG_PARAM_PORT_OFFSET = 0

* Used in - < IS_HOME >/repository/conf/carbon.xml

---
#### Set proxy ports when using a load balancer :

    CONFIG_PARAM_HTTP_PROXY_PORT = 80
    CONFIG_PARAM_HTTPS_PROXY_PORT = 443

* Used in - < IS_HOME >/repository/conf/tomcat/catalina-server.xml

---

#### Enable Embedded LDAP

    CONFIG_PARAM_EMBEDDED_LDAP = true

* Used in - <IS_HOME>/repository/conf/embedded-ldap.xml

---
#### Set LDAP Connection URL

    CONFIG_PARAM_LDAP_CONNECTION_URL = ldap://localhost:10389

* Used in - <IS_HOME>/repository/conf/user-mgt.xml

---

#### Set worker/manger sub-domain in nodes  :

    CONFIG_PARAM_SUB_DOMAIN= worker

 * Used in - < IS_HOME >/repository/conf/axis2/axis2.xml
 * Used in - < IS_HOME >/repository/conf/carbon.xml
 * Used in - < IS_HOME >/repository/conf/registry.xml

---
#### Set worker and manager hostnames

    CONFIG_PARAM_WORKER_HOST_NAME = am.cloud-test.wso2.com
    CONFIG_PARAM_MGT_HOST_NAME = mgt.am.cloud-test.wso2.com

* Used in - < IS_HOME >/repository/conf/axis2/axis2.xml
* Used in - < IS_HOME >/repository/conf/carbon.xml

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

* < IS_HOME >/repository/conf/user-mgt.xml
* < IS_HOME >/repository/conf/datasources/master-datasources.xml
* < IS_HOME >/repository/conf/registry.xml
