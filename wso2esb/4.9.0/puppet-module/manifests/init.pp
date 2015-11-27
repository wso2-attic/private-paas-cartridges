#----------------------------------------------------------------------------
#  Copyright 2005-2013 WSO2, Inc. http://www.wso2.org
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
#----------------------------------------------------------------------------
#
# Class: as
#
# This class installs WSO2 AS
#
# Parameters:
#
# Actions:
#   - Install WSO2 ESB
#
# Requires:
#
# Sample Usage:
#

class esb (
  $version               = undef,
  $offset                = 0,
  $esb_subdomain         = "esb",
  $clustering_port       = '4000',
  $config_db             = governance,
  $depsync               = false,
  $sub_cluster_domain    = mgt,
  $clustering            = false,
  $members               = {},
  $owner                 = root,
  $group                 = root,
  $catridge_version      = undef,
  $configurator_version  = undef,
  $target                = '/mnt',
  $monitoring            = false) inherits esb::params {
  $deployment_code       = 'esb'
  $service_code          = 'esb'
  $carbon_version        = $version
  $carbon_home           = "${target}/wso2${service_code}-${carbon_version}"

  $service_templates  = [ 
    'conf/carbon.xml',
    'conf/jndi.properties',
    'conf/andes-jndi.properties',
    'conf/datasources/esb-datasources.xml',
    'wso2server.sh',
    'conf/axis2/axis2.xml',
  ]

  $common_templates   = [ 
    'conf/user-mgt.xml',
    'conf/registry.xml',
    'conf/tenant-mgt.xml',
    'conf/datasources/master-datasources.xml',
  ]


  tag('esb')

  esb::clean { $deployment_code:
    mode   => $maintenance_mode,
    target => $carbon_home;
  }

  esb::initialize { $deployment_code:
    repo             => $package_repo,
    version          => $version,
    mode   		       => $maintenance_mode,
    service   		   => $service_code,
    deployment_code	 => $deployment_code,
    local_dir 		   => $local_package_dir,
    owner        		 => $owner,
    target   	    	 => $target,
    require 		     => Clean[$deployment_code];
  }


  esb::deploy { $deployment_code:
    security 		 => true,
    owner    		 => $owner,
    group    		 => $group,
    target   		 => $carbon_home,
    require  		 => Initialize[$deployment_code];
  }

  esb::push_templates { 
    $service_templates: 
      target    => $carbon_home,
      directory => $deployment_code,
      require   => Deploy[$deployment_code];

    $common_templates:
      target    => $carbon_home,
      directory => 'wso2base',
      require   => Deploy[$deployment_code],
  }

  file { "${carbon_home}/bin/wso2server.sh":
    ensure  => present,
    owner   => $owner,
    group   => $group,
    mode    => '0755',
    content => template("${deployment_code}/wso2server.sh.erb"),
    require => Deploy[$deployment_code],
    #    notify  => Service["wso2${service_code}"],
  }


  file { "/etc/init.d/wso2${service_code}":
    ensure  		 => present,
    owner   		 => 'root',
    group   		 => 'root',
    mode    		 => '0775',
    content 		 => template("${deployment_code}/wso2${service_code}.erb"),
    require 		 => Deploy[$deployment_code],
  }

 
#  service { "wso2${service_code}":
#    ensure   		 => running,
#    hasstatus  		 => true,
#    hasrestart 		 => true,
#    enable   		 => true,
#    require    		 => [
#        Initialize[$deployment_code],
#        Deploy[$deployment_code],
#        Push_templates[$service_templates],
#        File["${carbon_home}/bin/wso2server.sh"],
#        File["/etc/init.d/wso2${service_code}"],
#
#      ]
#  }
}

