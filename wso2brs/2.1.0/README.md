## WSO2 Business Rules Server 2.1.0 Cartridge

### Profiles

   - Default
   - Worker
   - Manager

### Compatibility

WSO2 Private PaaS 4.1.0

### Special Notes

- Server Shutdown timeout can be changed adding a new property as follows under property section in a cartridge definition.

name : payload_parameter.CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT 
value : 120 

Default value is 120 seconds. Value should be specified in seconds.