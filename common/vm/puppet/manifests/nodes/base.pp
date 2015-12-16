# ----------------------------------------------------------------------------
#  Copyright 2005-2015 WSO2, Inc. http://www.wso2.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ----------------------------------------------------------------------------
#

# base node
node 'base' {

# General Configurations
  $ppaas_cartridge_version = '4.1.3'
  $server_ip               = $ipaddress

# PCA Configurations
  $pca_name             = 'apache-stratos-python-cartridge-agent'
  $pca_version          = '4.1.4'
  $local_package_dir    = '/mnt/packs'
  $mb_ip                = '192.168.30.96'
  $mb_port              = '1883'
  $cep_urls             = "192.168.30.96:7711"
  $cep_username         = 'admin'
  $cep_password         = 'admin'
  $bam_ip               = '192.168.30.97'
  $bam_port             = '7611'
  $bam_secure_port      = '7711'
  $bam_username         = 'admin'
  $bam_password         = 'admin'
  $truststore_password  = 'wso2carbon'
  $enable_log_publisher = 'false'
  $metadata_service_url = 'https://192.168.30.96:9443'
  $agent_log_level      = "INFO"

# JAVA Configurations
  $java_distribution    = 'jdk-7u80-linux-x64.tar.gz'
  $java_folder          = 'jdk1.7.0_80'

# Configurator Configurations
  $configurator_name    = 'wso2ppaas-configurator'
  $configurator_version = '4.1.3'

  require ppaas_base
}
