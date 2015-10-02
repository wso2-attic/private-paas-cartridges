#!/bin/bash
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
set -e
prgdir=`dirname "$0"`
script_path=`cd "$prgdir"; pwd`
wso2_product_type="wso2is"
docker_image_name="is"
wso2_product_version="5.0.0"
wso2_product_template_module_path=`cd ${script_path}/../template-module/; pwd`
wso2_product_plugin_path=`cd ${script_path}/../plugins/; pwd`

source ${script_path}/../../../common/docker/scripts/build-helper.sh

if [ "$1" = "skip" ]; then
   skip_template_build=true
else
   skip_template_build=false
fi

build_image $skip_template_build $wso2_product_type $wso2_product_version $wso2_product_plugin_path \
              $wso2_product_template_module_path $script_path $docker_image_name