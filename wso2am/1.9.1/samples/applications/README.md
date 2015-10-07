WSO2AM-1.9.1 Application
=========================
A simple application with a wso2am-1.9.1 cartridge.

Application view
----------------
wso2am-1.9.1-app            <br />
-- wso2am-1.9.1-app-1       <br />
-- -- wso2am-1.9.1          <br />

Application folder structure
----------------------------
-- artifacts/[iaas]/ IaaS specific artifacts                <br />
-- scripts/common/ Common scripts for all iaases            <br />
-- scripts/[iaas] IaaS specific scripts                     <br />

How to run
----------
cd scripts/[iaas]/          <br />
./deploy.sh                 <br />

How to undeploy
---------------
cd scripts/[iaas]/          <br />
./undeploy.sh               <br />