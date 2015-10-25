## WSO2 Identity Server 5.0.0 Cartridge

### Profiles

   - Default

### Compatibility

WSO2 Private PaaS 4.1.0 or above

### Special Notes

- Server Shutdown timeout can be changed adding a new property as follows under property section in a cartridge definition.

name : payload_parameter.CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT
value : 120 

Default value is 120 seconds. Value should be specified in seconds.

- Create database tables before deploying the application

- If you are running WSO2 Identity Server as a Key Manager, Make sure following changes are included.
  
  1. Use the pre packaged Identity Server pack which is designed to run as Key Manager. Do not use the default IS pack.
     Download from  - [WSO2 Identity Server](http://product-dist.wso2.com/downloads/api-manager/1.9.1/identity-server/wso2is-5.0.0.zip)
     Refer [Docs](https://docs.wso2.com/display/CLUSTER420/Configuring+the+Pre-Packaged+Identity+Server+5.0.0+with+API+Manager+1.9.1)
      
  2. Rename the patch0012 kernal patch to patch9999 if you are applying the WSO2 Identity Server Service Pack for 5.0.0.
     This is to support private-paas membership schema which comes from kernal patch 12. 
     
  3. If you are creating a docker image change only the default IS pack with pre packaged IS pack. Plugins and template module 
  is same which is used in IS cartridge
  
  4. In VM scenario use the following structure for puppet. 
  
   wso2iskm500
  │   │   ├── packs
  │   │   │   └── Include the pre packaged IS pack and default IS template module
  │   │   └── plugins
  │   │       └── Include default IS plugins 
