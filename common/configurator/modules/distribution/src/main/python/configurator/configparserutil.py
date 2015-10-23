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


import ConfigParser
import getopt
import os
import logging
import sys

import constants

log = logging.getLogger()


class ConfigParserUtil(ConfigParser.ConfigParser):
    def as_dictionary(self):
        """
        read configuration file and create a dictionary
        :return configurations as a dictionary
        """
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

    @staticmethod
    def convert_properties_to_dictionary(property):
        """
        convert and return multi valued properties as a dictionary e.g :- Members,port mappings
        :param property: multi-valued string property to be converted to a dictionary
        :return dictionary of properties
        """
        property = property.replace('[', '')
        property = property.replace(']', '')
        properties = property.split(",")
        return dict(s.split(':') for s in properties)

    @staticmethod
    def get_multivalued_attributes_as_dictionary(context):
        """
        find multivalued attributes from context and convert them to dictionary
        :param context:
        :return:dictionary of properties
        """

        for key, value in context.iteritems():
            if value and value.startswith('['):
                context[key] = ConfigParserUtil.convert_properties_to_dictionary(value)
        return context

    @staticmethod
    def get_context_from_env(template_variables, configuration_context):
        """
        Read values from environment variables
        :param template_variables: list of variables
        :param configuration_context: dictionary containing configurations loaded from module.ini
        :return dictionary containing values for variables
        """
        context = {}
        while template_variables:
            var = template_variables.pop()
            if not os.environ.get(var):
                if var in configuration_context:
                    context[var] = os.environ.get(var, configuration_context[var])
                else:
                    log.warn("Variable %s is not found in module.ini or in environment variables", var)
            else:
                context[var] = os.environ.get(var)

        context = ConfigParserUtil.get_multivalued_attributes_as_dictionary(context)
        return context

    @staticmethod
    def str_to_bool(input_string):
        """
        parse string to boolean value
        :param input_string: string to be parsed as a boolean
        :return: boolean value of input string
        """
        input_string = str(input_string).strip().lower()
        if input_string == 'true':
            return True
        elif input_string == 'false':
            return False
        else:
            raise ValueError

    @staticmethod
    def print_usage():
        print "./configurator.py [-d <template_directory>]"

    @staticmethod
    def get_carbon_home(configuration_context):
        return os.environ.get(constants.CONFIG_CARBON_HOME_KEY,
                              configuration_context[constants.CONFIG_SETTINGS_KEY][constants.CONFIG_CARBON_HOME_KEY])

    @staticmethod
    def get_template_module_dir_from_cargs(cli_arguments):
        template_module_parent_dir = None
        try:
            opts, args = getopt.getopt(cli_arguments, "hd:")
        except getopt.GetoptError:
            log.error("Invalid argument was given.")
            ConfigParserUtil.print_usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-h":
                ConfigParserUtil.print_usage()
                sys.exit(0)
            elif opt == "-d":
                template_module_parent_dir = os.path.abspath(arg)

        return template_module_parent_dir
