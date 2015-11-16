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

# WSO2 Server Nodes definition

# ESB 4.8.1 cartridge node
node /[0-9]{1,12}.*wso2esb-481/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2esb-4.8.1',
    module_name      => 'wso2esb481'

  }
}


# ESB 4.9.0 cartridge node
node /[0-9]{1,12}.*wso2esb-490/ inherits base {

  class { 'java': }
class { 'python_agent': }
class { 'configurator': }
class { 'wso2installer':
    server_name      => 'wso2esb-4.9.0',
    module_name      => 'wso2esb490'

  }
}


# IS 5.0.0 cartridge node
node /[0-9]{1,12}.*wso2is-500/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2is-5.0.0',
    module_name      => 'wso2is500'
  }
}


# API Manager 1.9.0 cartridge node
node /[0-9]{1,12}.*wso2am-190/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2am-1.9.0',
    module_name      => 'wso2am190'
  }
}

# IS 5.0.0 cartridge node for API Manager
node /[0-9]{1,12}.*wso2is-as-km-500/ inherits base {

  class { 'java': }
class { 'python_agent': }
class { 'configurator': }
class { 'wso2installer':
    server_name      => 'wso2is-5.0.0',
    module_name      => 'wso2isaskm500'
  }
}


# API Manager 1.9.1 cartridge node
node /[0-9]{1,12}.*wso2am-191/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2am-1.9.1',
    module_name      => 'wso2am191'
  }
}


# AppServer 5.2.1 cartridge node
node /[0-9]{1,12}.*wso2as-521/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2as-5.2.1',
    module_name      => 'wso2as521'
  }
}

# AppServer 5.3.0 cartridge node
node /[0-9]{1,12}.*wso2as-530/ inherits base {

  class { 'java': }
class { 'python_agent': }
class { 'configurator': }
class { 'wso2installer':
    server_name      => 'wso2as-5.3.0',
    module_name      => 'wso2as530'
  }
}


# DAS 3.0.0 cartridge node
node /[0-9]{1,12}.*wso2das-300/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2das-3.0.0',
    module_name      => 'wso2das300'
  }
}


# BRS 2.1.0 cartridge node
node /[0-9]{1,12}.*wso2brs-210/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2brs-2.1.0',
    module_name      => 'wso2brs210'
  }
}


# MB 3.0.0 cartridge node
node /[0-9]{1,12}.*wso2mb-300/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2mb-3.0.0',
    module_name      => 'wso2mb300'
  }
}


# BPS 3.5.0 cartridge node
node /[0-9]{1,12}.*wso2bps-350/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2bps-3.5.0',
    module_name      => 'wso2bps350'
  }
}


# DSS 3.2.2 cartridge node
node /[0-9]{1,12}.*wso2dss-322/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2dss-3.2.2',
    module_name      => 'wso2dss322'
  }
}


# GREG 5.0.0 cartridge node
node /[0-9]{1,12}.*wso2greg-500/ inherits base {

  class { 'java': }
  class { 'python_agent': }
  class { 'configurator': }
  class { 'wso2installer':
    server_name      => 'wso2greg-5.0.0',
    module_name      => 'wso2greg500'
  }
}


# GREG 5.1.0 cartridge node
node /[0-9]{1,12}.*wso2greg-510/ inherits base {

  class { 'java': }
class { 'python_agent': }
class { 'configurator': }
class { 'wso2installer':
    server_name      => 'wso2greg-5.1.0',
    module_name      => 'wso2greg510'
  }
}


# CEP 4.0.0 cartridge node
node /[0-9]{1,12}.*wso2cep-400/ inherits base {

  class { 'java': }
class { 'python_agent': }
class { 'configurator': }
class { 'wso2installer':
    server_name      => 'wso2cep-4.0.0',
    module_name      => 'wso2cep400'
  }
}

# Execution sequence
Class['ppaas_base'] -> Class['java'] -> Class['configurator']-> Class['python_agent'] -> Class['wso2installer']
