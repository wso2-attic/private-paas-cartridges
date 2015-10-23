#!/usr/bin/python

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


from distutils.dir_util import copy_tree
import logging
import logging.config
import os
from jinja2 import Environment, FileSystemLoader, meta
import sys

import constants
from configparserutil import ConfigParserUtil

PATH = os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(os.path.join(PATH, 'conf', 'logging_config.ini'))
log = logging.getLogger(__name__)
template_environment = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.abspath(os.sep)),
    trim_blocks=False)


def render_template(template_filename, configuration_context):
    """
    parse the template file and return the content as a text

    :param template_filename: template filename path
    :param configuration_context: dictionary containing configurations loaded from module.ini
    :return populated template content
    """
    settings = configuration_context[constants.CONFIG_SETTINGS_KEY]
    # Converting multi-valued params to dictionary
    params_context = configuration_context[constants.CONFIG_PARAMS_KEY]

    if ConfigParserUtil.str_to_bool(settings[constants.CONFIG_READ_FROM_ENVIRONMENT_KEY]):
        log.info("READ_FROM_ENVIRONMENT is set to True. Reading template parameters from environment variables")
        template_source = template_environment.loader.get_source(template_environment, template_filename)[0]
        parsed_content = template_environment.parse(template_source)
        variables = meta.find_undeclared_variables(parsed_content)
        params_context_dict = ConfigParserUtil.get_context_from_env(variables, params_context)
    else:
        params_context_dict = ConfigParserUtil.get_multivalued_attributes_as_dictionary(params_context)

    log.info("Rendering template file: %s using template parameters: %s", template_filename, params_context_dict)
    return template_environment.get_template(template_filename).render(params_context_dict)


def generate_file_from_template(source, target, configuration_context):
    """
    Generate file from the given template file

    :param source: Path to the template file
    :param target: Path to the output file
    :param configuration_context: dictionary containing configurations loaded from module.ini
    :return None
    """
    directory = os.path.dirname(target)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(target, 'w') as xml_file:
        content = render_template(source, configuration_context)
        log.debug("Writing content to [file] %s [content] %s", target, content)
        xml_file.write(content)


def generate_context(config_file_path):
    """
    Read the config.ini and generate context based on settings

    :param config_file_path: location of the module.ini file
    :return dictionary containing configurations loaded from module.ini
    """
    # Read configuration file
    config_parser = ConfigParserUtil()
    config_parser.optionxform = str
    config_parser.read(os.path.join(config_file_path))
    configurations = config_parser.as_dictionary()
    log.debug("Configurations loaded: %s", configurations)
    return configurations


def traverse(templates_dir, configuration_context):
    """
    traverse through the folder structure and generate xml files

    :param templates_dir: path to the template directory in template module
    :param configuration_context: dictionary containing configurations loaded from module.ini
    :return None
    """
    log.info("Scanning for templates in %s", templates_dir)
    carbon_home = ConfigParserUtil.get_carbon_home(configuration_context)
    for root, dirs, files in os.walk(templates_dir):
        for filename in files:
            # generating the relative path of the template
            template_file_path = os.path.join(root, filename)
            log.debug("Template file path: %s ", template_file_path)
            template_relative_path = os.path.splitext(os.path.relpath(os.path.join(root, filename), templates_dir))[0]
            log.debug("Teplate relative path: %s", template_relative_path)
            template_file_target = os.path.join(carbon_home, template_relative_path)
            log.debug("Template file target path: %s ", template_file_target)

            # populate the template and copy to target location
            generate_file_from_template(template_file_path, template_file_target, configuration_context)


def copy_files_to_pack(source, target):
    """
    Copy files in the template's files directory to pack preserving the structure provided
    :param source: path to files directory in template folder
    :param target: target path to copy the files in template folder
    :return:
    """
    result = copy_tree(source, target, verbose=1)
    log.info("Files copied [to] %s, [from] %s with [result] %s", source, target, result)


def configure():
    """
    Main method
    :return None
    """
    log.info("Running WSO2 Private PaaS Configurator...")
    # read template module dir from environmental vars or default to configurator's path
    template_module_parent_dir = os.environ.get(constants.TEMPLATE_MODULE_PATH_ENV_KEY,
                                                os.path.join(PATH, constants.TEMPLATE_MODULE_FOLDER_NAME))
    log.info("Scanning the template module directory: %s" % template_module_parent_dir)
    # traverse through the template directory
    only_directories = [f for f in os.listdir(template_module_parent_dir) if
                        os.path.isdir(os.path.join(template_module_parent_dir, f))]
    for file_name in only_directories:
        module_settings_file_path = os.path.join(template_module_parent_dir, file_name, constants.CONFIG_FILE_NAME)
        templates_dir = os.path.join(template_module_parent_dir, file_name, constants.TEMPLATES_FOLDER_NAME)
        files_dir = os.path.join(template_module_parent_dir, file_name, constants.FILES_FOLDER_NAME)
        if os.path.isfile(module_settings_file_path):
            log.info("Module settings file found for template module: %s", file_name)
        else:
            log.warn("Could not find module settings file at: %s. Skipping directory...", module_settings_file_path)
            continue

        log.info("Populating templates at: %s", templates_dir)
        configuration_context = generate_context(module_settings_file_path)
        traverse(templates_dir, configuration_context)

        # copy files directory if it exists
        if os.path.exists(files_dir):
            log.info("Copying files at: %s", files_dir)
            target = ConfigParserUtil.get_carbon_home(configuration_context)
            copy_files_to_pack(files_dir, target)

        log.info("Configuration completed for template module: %s", file_name)

    log.info("End of WSO2 Private PaaS Configurator")


if __name__ == "__main__":
    try:
        configure()
    except Exception as e:
        log.exception("Error while executing WSO2 Private PaaS Configurator: %s", e)
        sys.exit(1)
