# WSO2 Private PaaS VM modules

This distribution contains following modules required for Virtual Machine scenario

 - init-scripts
 These scripts are used to bootstrap Private PaaS cartridge instances spawned.

 - Puppet
 A single Puppet module is used to configure VM instances spawned. The wso2installer Puppet module will only deploy the
 Python configurator module, Python cartridge agent module and WSO2 product pack. The rest of the configurations will be
 carried out by the Python configurator.