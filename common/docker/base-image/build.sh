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

pushd `cd ${script_path}/../../; pwd`
configurator_version=`grep -oP '<version>\K[^<]+' pom.xml| head -1`
popd

wso2_base_image_version=${configurator_version%-*}
configurator_path=`cd ${script_path}/../../configurator; pwd`

echo "----------------------------------"
echo "Building Configurator"
echo "----------------------------------"
pushd ${configurator_path}
mvn clean install
cp -v target/ppaas-configurator-${configurator_version}.zip ${script_path}/packages/
popd

echo "----------------------------------"
echo "Building base docker image"
echo "----------------------------------"
sudo docker build -t wso2/base-image:${wso2_base_image_version} .
echo "Base docker image built successfully"
