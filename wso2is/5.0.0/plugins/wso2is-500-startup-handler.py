# ------------------------------------------------------------------------
#
# Copyright 2005-2015 WSO2, Inc. (http://wso2.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License
#
# ------------------------------------------------------------------------

import subprocess
import socket
import os
import time

from plugins.contracts import ICartridgeAgentPlugin
from modules.util.log import LogFactory
from entity import *
import mdsclient
from config import Config


class WSO2StartupHandler(ICartridgeAgentPlugin):
    """
    Configures and starts configurator, carbon server
    """
    log = LogFactory().get_log(__name__)

    # class constants
    CONST_PORT_MAPPINGS = "PORT_MAPPINGS"
    CONST_APPLICATION_ID = "APPLICATION_ID"
    CONST_MB_IP = "MB_IP"
    CONST_SERVICE_NAME = "SERVICE_NAME"
    CONST_CLUSTER_ID = "CLUSTER_ID"
    CONST_WORKER = "worker"
    CONST_MANAGER = "manager"
    CONST_MGT = "mgt"

    CONST_PORT_MAPPING_MGT_HTTP_TRANSPORT = "mgt-http"
    CONST_PORT_MAPPING_MGT_HTTPS_TRANSPORT = "mgt-https"
    CONST_PROTOCOL_HTTP = "http"
    CONST_PROTOCOL_HTTPS = "https"
    CONST_PPAAS_MEMBERSHIP_SCHEME = "private-paas"
    CONST_PRODUCT = "IS"

    SERVICES = ["wso2is-500-manager", "wso2is-as-km-500-manager"]

    # list of environment variables exported by the plugin
    ENV_CONFIG_PARAM_SUB_DOMAIN = 'CONFIG_PARAM_SUB_DOMAIN'
    ENV_CONFIG_PARAM_MB_HOST = 'CONFIG_PARAM_MB_HOST'
    ENV_CONFIG_PARAM_CLUSTER_IDs = 'CONFIG_PARAM_CLUSTER_IDs'
    ENV_CONFIG_PARAM_HTTP_PROXY_PORT = 'CONFIG_PARAM_HTTP_PROXY_PORT'
    ENV_CONFIG_PARAM_HTTPS_PROXY_PORT = 'CONFIG_PARAM_HTTPS_PROXY_PORT'
    ENV_CONFIG_PARAM_HOST_NAME = 'CONFIG_PARAM_HOST_NAME'
    ENV_CONFIG_PARAM_MGT_HOST_NAME = 'CONFIG_PARAM_MGT_HOST_NAME'
    ENV_CONFIG_PARAM_LOCAL_MEMBER_HOST = 'CONFIG_PARAM_LOCAL_MEMBER_HOST'

    # clustering related environment variables read from payload_parameters
    ENV_CONFIG_PARAM_CLUSTERING = 'CONFIG_PARAM_CLUSTERING'
    ENV_CONFIG_PARAM_MEMBERSHIP_SCHEME = 'CONFIG_PARAM_MEMBERSHIP_SCHEME'

    ENV_CONFIG_PARAM_PROFILE = 'CONFIG_PARAM_PROFILE'
    CONST_PROFILE_KEY_MANAGER = 'KeyManager'
    ENV_LB_IP = 'LB_IP'
    ENV_CONFIG_PARAM_KEYMANAGER_IP = 'CONFIG_PARAM_KEYMANAGER_IP'
    CONST_CONFIG_PARAM_KEYMANAGER_PORTS = 'CONFIG_PARAM_KEYMANAGER_PORTS'
    ENV_CONFIG_PARAM_GATEWAY_IP = 'CONFIG_PARAM_GATEWAY_IP'
    CONST_CONFIG_PARAM_GATEWAY_PORTS = 'CONFIG_PARAM_GATEWAY_PORTS'
    ENV_CONFIG_PARAM_GATEWAY_WORKER_IP = 'CONFIG_PARAM_GATEWAY_WORKER_IP'
    CONST_CONFIG_PARAM_GATEWAY_WORKER_PORTS = 'CONFIG_PARAM_GATEWAY_WORKER_PORTS'
    CONST_KUBERNETES = "KUBERNETES"
    CONST_VM = "VM"
    CONST_EXTERNAL_LB_FOR_KUBERNETES = "EXTERNAL_LB_FOR_KUBERNETES"
    CONST_GATEWAY_MANAGER_SERVICE_NAME = "wso2am-191-gw-manager"
    CONST_GATEWAY_WORKER_SERVICE_NAME = "wso2am-191-gw-worker"
    ENV_CONFIG_PARAM_GATEWAY_WORKER_PT_HTTP_PROXY_PORT = 'CONFIG_PARAM_GATEWAY_WORKER_PT_HTTP_PROXY_PORT'
    ENV_CONFIG_PARAM_GATEWAY_WORKER_PT_HTTPS_PROXY_PORT = 'CONFIG_PARAM_GATEWAY_WORKER_PT_HTTPS_PROXY_PORT'
    ENV_CONFIG_PARAM_GATEWAY_HTTPS_PROXY_PORT = 'CONFIG_PARAM_GATEWAY_HTTPS_PROXY_PORT'

    # This is payload parameter which enables to use an external lb when using kubernetes. Use true when using with kub.
    ENV_CONFIG_PARAM_USE_EXTERNAL_LB_FOR_KUBERNETES = 'CONFIG_PARAM_USE_EXTERNAL_LB_FOR_KUBERNETES'
    CONST_KM_SERVICE_NAME = 'KEY_MANAGER_SERVICE_NAME'

    def run_plugin(self, values):

        # read from 'values'
        port_mappings_str = values[self.CONST_PORT_MAPPINGS].replace("'", "")
        app_id = values[self.CONST_APPLICATION_ID]
        mb_ip = values[self.CONST_MB_IP]
        service_type = values[self.CONST_SERVICE_NAME]
        my_cluster_id = values[self.CONST_CLUSTER_ID]
        clustering = values.get(self.ENV_CONFIG_PARAM_CLUSTERING, 'false')
        membership_scheme = values.get(self.ENV_CONFIG_PARAM_MEMBERSHIP_SCHEME)
        profile = os.environ.get(self.ENV_CONFIG_PARAM_PROFILE)
        lb_ip = os.environ.get(self.ENV_LB_IP)
        external_lb = values.get(WSO2StartupHandler.ENV_CONFIG_PARAM_USE_EXTERNAL_LB_FOR_KUBERNETES, 'false')

        # read topology from PCA TopologyContext
        topology = TopologyContext.topology

        # log above values
        WSO2StartupHandler.log.info("Port Mappings: %s" % port_mappings_str)
        WSO2StartupHandler.log.info("Application ID: %s" % app_id)
        WSO2StartupHandler.log.info("MB IP: %s" % mb_ip)
        WSO2StartupHandler.log.info("Service Name: %s" % service_type)
        WSO2StartupHandler.log.info("Cluster ID: %s" % my_cluster_id)
        WSO2StartupHandler.log.info("Clustering: %s" % clustering)
        WSO2StartupHandler.log.info("Membership Scheme: %s" % membership_scheme)
        WSO2StartupHandler.log.info("Profile: %s" % profile)
        WSO2StartupHandler.log.info("LB IP: %s" % lb_ip)

        # export Proxy Ports as Env. variables - used in catalina-server.xml
        mgt_http_proxy_port = self.read_proxy_port(port_mappings_str, self.CONST_PORT_MAPPING_MGT_HTTP_TRANSPORT,
                                                   self.CONST_PROTOCOL_HTTP)
        mgt_https_proxy_port = self.read_proxy_port(port_mappings_str, self.CONST_PORT_MAPPING_MGT_HTTPS_TRANSPORT,
                                                    self.CONST_PROTOCOL_HTTPS)

        self.export_env_var(self.ENV_CONFIG_PARAM_HTTP_PROXY_PORT, mgt_http_proxy_port)
        self.export_env_var(self.ENV_CONFIG_PARAM_HTTPS_PROXY_PORT, mgt_https_proxy_port)

        if profile == self.CONST_PROFILE_KEY_MANAGER:
            # this is for key_manager profile to support IS for API Manager
            # remove previous data from metadata service
            # add new values to meta data service - key manager ip and mgt-console port
            # retrieve values from meta data service - gateway ip, gw mgt console port, pt http and https ports
            # check deployment is vm, if vm update /etc/hosts with values
            # export retrieve values as environment variables
            # set the start command

            self.remove_data_from_metadata(self.ENV_CONFIG_PARAM_KEYMANAGER_IP)
            self.remove_data_from_metadata(self.CONST_CONFIG_PARAM_KEYMANAGER_PORTS)
            self.remove_data_from_metadata(self.CONST_KM_SERVICE_NAME)

            self.add_data_to_meta_data_service(self.ENV_CONFIG_PARAM_KEYMANAGER_IP, lb_ip)
            self.add_data_to_meta_data_service(self.CONST_CONFIG_PARAM_KEYMANAGER_PORTS,
                                               "Ports:" + mgt_https_proxy_port)
            self.add_data_to_meta_data_service(self.CONST_KM_SERVICE_NAME, service_type)

            gateway_ip = self.get_data_from_meta_data_service(app_id, self.ENV_CONFIG_PARAM_GATEWAY_IP)
            gateway_ports = self.get_data_from_meta_data_service(app_id, self.CONST_CONFIG_PARAM_GATEWAY_PORTS)
            gateway_worker_ip = self.get_data_from_meta_data_service(app_id, self.ENV_CONFIG_PARAM_GATEWAY_WORKER_IP)
            gateway_worker_ports = self.get_data_from_meta_data_service(app_id,
                                                                        self.CONST_CONFIG_PARAM_GATEWAY_WORKER_PORTS)

            environment_type = self.find_environment_type(external_lb, service_type, app_id)

            if environment_type == WSO2StartupHandler.CONST_KUBERNETES:
                gateway_host = gateway_ip
                gateway_worker_host = gateway_worker_ip
            else:
                gateway_host_name = self.get_host_name_from_cluster(self.CONST_GATEWAY_MANAGER_SERVICE_NAME, app_id)
                gateway_worker_host_name = self.get_host_name_from_cluster(self.CONST_GATEWAY_WORKER_SERVICE_NAME,
                                                                           app_id)
                gateway_host = gateway_host_name
                gateway_worker_host = gateway_worker_host_name

                self.update_hosts_file(gateway_ip, gateway_host_name)
                self.update_hosts_file(gateway_worker_ip, gateway_worker_host_name)

            member_ip = socket.gethostbyname(socket.gethostname())
            self.set_host_name(app_id, service_type, member_ip)
            self.export_env_var(self.ENV_CONFIG_PARAM_GATEWAY_IP, gateway_host)
            self.set_gateway_ports(gateway_ports)
            self.export_env_var(self.ENV_CONFIG_PARAM_GATEWAY_WORKER_IP, gateway_worker_host)
            self.set_gateway_worker_ports(gateway_worker_ports)

        # set sub-domain
        sub_domain = None
        if service_type.endswith(self.CONST_MANAGER):
            sub_domain = self.CONST_MGT
        elif service_type.endswith(self.CONST_WORKER):
            sub_domain = self.CONST_WORKER
        self.export_env_var(self.ENV_CONFIG_PARAM_SUB_DOMAIN, sub_domain)

        # if CONFIG_PARAM_MEMBERSHIP_SCHEME is not set, set the private-paas membership scheme as default one
        if clustering == 'true' and membership_scheme is None:
            membership_scheme = self.CONST_PPAAS_MEMBERSHIP_SCHEME
            self.export_env_var(self.ENV_CONFIG_PARAM_MEMBERSHIP_SCHEME, membership_scheme)

        # check if clustering is enabled
        if clustering == 'true':
            # set hostnames
            self.export_host_names(topology, app_id)
            # check if membership scheme is set to 'private-paas'
            if membership_scheme == self.CONST_PPAAS_MEMBERSHIP_SCHEME:
                # export Cluster_Ids as Env. variables - used in axis2.xml
                self.export_cluster_ids(topology, app_id, service_type, my_cluster_id)
                # export mb_ip as Env.variable - used in jndi.properties
                self.export_env_var(self.ENV_CONFIG_PARAM_MB_HOST, mb_ip)

        # set instance private ip as CONFIG_PARAM_LOCAL_MEMBER_HOST
        private_ip = self.get_member_private_ip(topology, Config.service_name, Config.cluster_id, Config.member_id)
        self.export_env_var(self.ENV_CONFIG_PARAM_LOCAL_MEMBER_HOST, private_ip)

        # start configurator
        WSO2StartupHandler.log.info("Configuring WSO2 %s..." % self.CONST_PRODUCT)
        config_command = "python ${CONFIGURATOR_HOME}/configurator.py"
        env_var = os.environ.copy()
        p = subprocess.Popen(config_command, env=env_var, shell=True)
        output, errors = p.communicate()
        WSO2StartupHandler.log.info("WSO2 %s configured successfully" % self.CONST_PRODUCT)

        # start server
        WSO2StartupHandler.log.info("Starting WSO2 %s ..." % self.CONST_PRODUCT)
        if service_type.endswith(self.CONST_WORKER):
            start_command = "exec ${CARBON_HOME}/bin/wso2server.sh -DworkerNode=true start"
        else:
            start_command = "exec ${CARBON_HOME}/bin/wso2server.sh -Dsetup start"
        env_var = os.environ.copy()
        p = subprocess.Popen(start_command, env=env_var, shell=True)
        output, errors = p.communicate()
        WSO2StartupHandler.log.info("WSO2 %s started successfully" % self.CONST_PRODUCT)

    def get_member_private_ip(self, topology, service_name, cluster_id, member_id):
        service = topology.get_service(service_name)
        if service is None:
            raise Exception("Service not found in topology [service] %s" % service_name)

        cluster = service.get_cluster(cluster_id)
        if cluster is None:
            raise Exception("Cluster id not found in topology [cluster] %s" % cluster_id)

        member = cluster.get_member(member_id)
        if member is None:
            raise Exception("Member id not found in topology [member] %s" % member_id)

        if member.member_default_private_ip and not member.member_default_private_ip.isspace():
            WSO2StartupHandler.log.info(
                "Member private ip read from the topology: %s" % member.member_default_private_ip)
            return member.member_default_private_ip
        else:
            local_ip = socket.gethostbyname(socket.gethostname())
            WSO2StartupHandler.log.info(
                "Member private ip not found in the topology. Reading from the socket interface: %s" % local_ip)
            return local_ip

    def set_gateway_worker_ports(self, gateway_worker_ports):
        """
        Expose gateway worker ports
        :return: void
        """
        gateway_pt_http_pp = None
        gateway_pt_https_pp = None

        if gateway_worker_ports is not None:
            gateway_wk_ports_array = gateway_worker_ports.split(":")
            if gateway_wk_ports_array:
                gateway_pt_http_pp = gateway_wk_ports_array[1]
                gateway_pt_https_pp = gateway_wk_ports_array[2]

        self.export_env_var(self.ENV_CONFIG_PARAM_GATEWAY_WORKER_PT_HTTP_PROXY_PORT, str(gateway_pt_http_pp))
        self.export_env_var(self.ENV_CONFIG_PARAM_GATEWAY_WORKER_PT_HTTPS_PROXY_PORT, str(gateway_pt_https_pp))

    def set_gateway_ports(self, gateway_ports):
        """
        Expose gateway ports
        Input- Ports:30003
        :return: void
        """
        gateway_mgt_https_pp = None

        if gateway_ports is not None:
            gateway_ports_array = gateway_ports.split(":")
            if gateway_ports_array:
                gateway_mgt_https_pp = gateway_ports_array[1]

        self.export_env_var(self.ENV_CONFIG_PARAM_GATEWAY_HTTPS_PROXY_PORT, str(gateway_mgt_https_pp))

    def set_host_name(self, app_id, service_name, member_ip):
        """
        Set hostname of service read from topology for any service name
        export hostname and update the /etc/hosts
        :return: void
        """
        host_name = self.get_host_name_from_cluster(service_name, app_id)
        self.export_env_var(self.ENV_CONFIG_PARAM_HOST_NAME, host_name)
        self.update_hosts_file(member_ip, host_name)

    def update_hosts_file(self, ip_address, host_name):
        """
        Updates /etc/hosts file with clustering hostnames
        :return: void
        """
        config_command = "echo %s  %s >> /etc/hosts" % (ip_address, host_name)
        env_var = os.environ.copy()
        p = subprocess.Popen(config_command, env=env_var, shell=True)
        output, errors = p.communicate()
        WSO2StartupHandler.log.info(
            "Successfully updated [ip_address] %s & [hostname] %s in etc/hosts" % (ip_address, host_name))

    def get_host_name_from_cluster(self, service_name, app_id):
        """
        Get hostname for a service
        :return: hostname
        """
        clusters = self.get_clusters_from_topology(service_name)

        if clusters is not None:
            for cluster in clusters:
                if cluster.app_id == app_id:
                    hostname = cluster.hostnames[0]

        return hostname

    def find_environment_type(self, external_lb, service_name, app_id):
        """
        Check for vm or kubernetes
        :return: Vm or Kubernetes
        """

        if external_lb == 'true':
            return WSO2StartupHandler.CONST_EXTERNAL_LB_FOR_KUBERNETES
        else:
            isKubernetes = self.check_for_kubernetes_cluster(service_name, app_id)

            if isKubernetes:
                return WSO2StartupHandler.CONST_KUBERNETES
            else:
                return WSO2StartupHandler.CONST_VM

    def get_clusters_from_topology(self, service_name):
        """
        get clusters from topology
        :return: clusters
        """
        clusters = None
        topology = TopologyContext().get_topology()

        if topology is not None:
            if topology.service_exists(service_name):
                service = topology.get_service(service_name)
                clusters = service.get_clusters()
            else:
                WSO2StartupHandler.log.error("[Service] %s is not available in topology" % service_name)

        return clusters

    def check_for_kubernetes_cluster(self, service_name, app_id):
        """
        Check the deployment is kubernetes
        :return: True
        """
        isKubernetes = False
        clusters = self.get_clusters_from_topology(service_name)

        if clusters is not None:
            for cluster in clusters:
                if cluster.app_id == app_id:
                    isKubernetes = cluster.is_kubernetes_cluster

        return isKubernetes

    def get_data_from_meta_data_service(self, app_id, receive_data):
        """
        Get data from meta data service
        :return: received data
        """
        mds_response = None
        while mds_response is None:
            WSO2StartupHandler.log.info(
                "Waiting for " + receive_data + " to be available from metadata service for app ID: %s" % app_id)
            time.sleep(1)
            mds_response = mdsclient.get(app=True)
            if mds_response is not None and mds_response.properties.get(receive_data) is None:
                mds_response = None

        return mds_response.properties[receive_data]

    def add_data_to_meta_data_service(self, key, value):
        """
        add data to meta data service
        :return: void
        """
        mdsclient.MDSPutRequest()
        data = {"key": key, "values": [value]}
        mdsclient.put(data, app=True)

    def remove_data_from_metadata(self, key):
        """
        remove data from meta data service
        :return: void
        """
        mds_response = mdsclient.get(app=True)

        if mds_response is not None and mds_response.properties.get(key) is not None:
            read_data = mds_response.properties[key]
            check_str = isinstance(read_data, (str, unicode))

            if check_str == True:
                mdsclient.delete_property_value(key, read_data)
            else:
                check_int = isinstance(read_data, int)
                if check_int == True:
                    mdsclient.delete_property_value(key, read_data)
                else:
                    for entry in read_data:
                        mdsclient.delete_property_value(key, entry)

    def export_host_names(self, topology, app_id):
        """
        Set hostnames of services read from topology for worker manager instances
        exports MgtHostName and HostName

        :return: void
        """
        mgt_host_name = None
        host_name = None
        for service_name in self.SERVICES:
            if service_name.endswith(self.CONST_MANAGER):
                mgr_cluster = self.get_cluster_of_service(topology, service_name, app_id)
                if mgr_cluster is not None:
                    mgt_host_name = mgr_cluster.hostnames[0]
            elif service_name.endswith(self.CONST_WORKER):
                worker_cluster = self.get_cluster_of_service(topology, service_name, app_id)
                if worker_cluster is not None:
                    host_name = worker_cluster.hostnames[0]

        self.export_env_var(self.ENV_CONFIG_PARAM_MGT_HOST_NAME, mgt_host_name)
        self.export_env_var(self.ENV_CONFIG_PARAM_HOST_NAME, host_name)

    def export_cluster_ids(self, topology, app_id, service_type, my_cluster_id):
        """
        Set clusterIds of services read from topology for worker manager instances
        else use own clusterId

        :return: void
        """
        cluster_ids = []
        cluster_id_of_service = None
        if service_type.endswith(self.CONST_MANAGER) or service_type.endswith(self.CONST_WORKER):
            for service_name in self.SERVICES:
                cluster_of_service = self.get_cluster_of_service(topology, service_name, app_id)
                if cluster_of_service is not None:
                    cluster_id_of_service = cluster_of_service.cluster_id
                if cluster_id_of_service is not None:
                    cluster_ids.append(cluster_id_of_service)
        else:
            cluster_ids.append(my_cluster_id)
        # If clusterIds are available, export them as environment variables
        if cluster_ids:
            cluster_ids_string = ",".join(cluster_ids)
            self.export_env_var(self.ENV_CONFIG_PARAM_CLUSTER_IDs, cluster_ids_string)

    @staticmethod
    def get_cluster_of_service(topology, service_name, app_id):
        cluster_obj = None
        clusters = None
        if topology is not None:
            if topology.service_exists(service_name):
                service = topology.get_service(service_name)
                if service is not None:
                    clusters = service.get_clusters()
                else:
                    WSO2StartupHandler.log.warn("[Service] %s is None" % service_name)
            else:
                WSO2StartupHandler.log.warn("[Service] %s is not available in topology" % service_name)
        else:
            WSO2StartupHandler.log.warn("Topology is empty.")

        if clusters is not None:
            for cluster in clusters:
                if cluster.app_id == app_id:
                    cluster_obj = cluster

        return cluster_obj

    @staticmethod
    def read_proxy_port(port_mappings_str, port_mapping_name, port_mapping_protocol):
        """
        returns proxy port of the requested port mapping

        :return: void
        """

        # port mappings format: NAME:mgt-http|PROTOCOL:http|PORT:30001|PROXY_PORT:0|TYPE:NodePort;
        #                       NAME:mgt-https|PROTOCOL:https|PORT:30002|PROXY_PORT:0|TYPE:NodePort;
        #                       NAME:pt-http|PROTOCOL:http|PORT:30003|PROXY_PORT:7280|TYPE:ClientIP;
        #                       NAME:pt-https|PROTOCOL:https|PORT:30004|PROXY_PORT:7243|TYPE:NodePort

        if port_mappings_str is not None:
            port_mappings_array = port_mappings_str.split(";")
            if port_mappings_array:

                for port_mapping in port_mappings_array:
                    # WSO2StartupHandler.log.debug("port_mapping: %s" % port_mapping)
                    name_value_array = port_mapping.split("|")
                    name = name_value_array[0].split(":")[1]
                    protocol = name_value_array[1].split(":")[1]
                    proxy_port = name_value_array[3].split(":")[1]
                    # If PROXY_PORT is not set, set PORT as the proxy port (ex:Kubernetes),
                    if proxy_port == '0':
                        proxy_port = name_value_array[2].split(":")[1]

                    if name == port_mapping_name and protocol == port_mapping_protocol:
                        return proxy_port

    @staticmethod
    def export_env_var(variable, value):
        """
        exports key value pairs as env. variables

        :return: void
        """
        if value is not None:
            os.environ[variable] = value
            WSO2StartupHandler.log.info("Exported environment variable %s: %s" % (variable, value))
        else:
            WSO2StartupHandler.log.warn("Could not export environment variable %s " % variable)
