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

from plugins.contracts import ICartridgeAgentPlugin
from modules.util.log import LogFactory
import os
import subprocess
import psutil
import time


class WSO2CleanupHandler(ICartridgeAgentPlugin):
    log = LogFactory().get_log(__name__)

    # In the cartridge definition, CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT can be passed as seconds
    ENV_CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT = 'CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT'

    def run_plugin(self, values):

        timeout = values.get(WSO2CleanupHandler.ENV_CONFIG_PARAM_SERVER_SHUTDOWN_TIMEOUT, '120')

        # read pid value from the file
        filepath = os.environ.get('CARBON_HOME') + '/wso2carbon.pid'
        infile = open(filepath, 'r')
        read_value = infile.readline()
        pid_value = read_value.split('\n', 1)[0]

        WSO2CleanupHandler.log.info('PID value is ' + pid_value)

        start_command = "exec ${CARBON_HOME}/bin/wso2server.sh stop"
        env_var = os.environ.copy()
        p = subprocess.Popen(start_command, env=env_var, shell=True)
        output, errors = p.communicate()

        WSO2CleanupHandler.log.info('Executed wso2server.sh stop command for the server')

        available = True
        timeout_occurred = False
        start_time = time.time()

        while available:
            available = psutil.pid_exists(int(pid_value))
            end_time = time.time() - start_time
            time.sleep(1)
            if end_time > int(timeout):
                available = False
                timeout_occurred = True
                WSO2CleanupHandler.log.info('Timeout occurred for stopping the server!!!')

        if timeout_occurred:
            WSO2CleanupHandler.log.info('Could not stop the server. Timeout occurred!!!')
        else:
            WSO2CleanupHandler.log.info('Successfully stopped the server gracefully.')
