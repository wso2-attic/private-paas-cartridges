# WSO2 Private PaaS Cartridges

---
|  Branch | Build Status |
| :------ |:------------ | 
| master  | [![Build Status](https://wso2.org/jenkins/buildStatus/icon?job=private-paas-cartridges)](https://wso2.org/jenkins/job/private-paas-cartridges/) |
---

A cartridge provides a way to add new runtimes, services & middleware to WSO2 Private PaaS. It can be either a Docker image
or a Virtual Machine (VM) image created using following:

   - Cartridge Agent
   - Cartridge Agent Plugins
   - Configurator Template Module 
   - Runtime/Middleware/Service Distribution
   - Initialization Script

## Compatibility

Cartridges found in this repository can only be used with WSO2 Private PaaS 4.1.0 or later versions. The comaptible Private PaaS version is mentioned in each cartridge.

## How to build a Docker Image for a WSO2 Product

- Build the base image

Go to common/docker/base-image and follow the steps mentioned in the Readme file. 
This base image contains JDK, configurator, python cartridge agent and other dependencies.

- Build the WSO2 product docker image

Go to <WSO2 Product Name>/<Version>/docker and follow the steps in the Readme file.

