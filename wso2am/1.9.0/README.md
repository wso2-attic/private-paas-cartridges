## WSO2 API Manager 1.9.0 Cartridge

### Profiles

   - Default
   - Key Manager
   - Gateway Manager
   - Gateway Worker 
   - Publisher
   - Store 
   - Publisher + Store

### Compatibility

WSO2 Private PaaS 4.1.0

### Special Notes

- Server Shutdown timeout can be changed adding a new property as follows under property section in a cartridge definition.

name : CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT 
value : 120 

Default value is 120 seconds. Value should be specified in seconds.

- Create database tables before deploying the application