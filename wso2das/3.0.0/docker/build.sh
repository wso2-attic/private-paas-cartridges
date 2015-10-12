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
wso2_product_type="wso2das"
wso2_product_version="3.0.0"
docker_image_name="das"
wso2_product_template_module_path=`cd ${script_path}/../template-module/; pwd`
wso2_product_plugin_path=`cd ${script_path}/../plugins/; pwd`

pushd `cd ${script_path}/../template-module/; pwd`
VERSION=`mvn help:evaluate -Dexpression=project.version 2>/dev/null| grep -v "^\["`
IMAGE_VERSION=${VERSION%-*} # Remove the SNAPSHOT string for non-released versions
popd

if [ -f ${script_path}/../../../common/docker/scripts/build-helper.sh ]; then
    source ${script_path}/../../../common/docker/scripts/build-helper.sh
else
    # build-helper.sh will be available in the distribution zip archive
    source build-helper.sh
fi

if [ -d ${script_path}/../../../common/plugins/ ]; then
    common_plugin_path=`cd ${script_path}/../../../common/plugins/; pwd`
else
    common_plugin_path=$wso2_product_plugin_path
fi

if [ "$1" = "skip" ]; then
   skip_template_build=true
else
   skip_template_build=false
fi

build_image $skip_template_build $wso2_product_type $wso2_product_version $wso2_product_plugin_path \
              $wso2_product_template_module_path $script_path $docker_image_name $common_plugin_path \
              $IMAGE_VERSION $VERSION