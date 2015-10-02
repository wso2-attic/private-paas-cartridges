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
common_plugin_path=`cd ${script_path}/../../../common/plugins/; pwd`
skip_template_build=false

pushd `cd ${script_path}/../../../; pwd`
VERSION=`mvn help:evaluate -Dexpression=project.version 2>/dev/null| grep -v "^\["`
IMAGE_VERSION=${VERSION%-*} # Remove the SNAPSHOT string for non-released versions
popd

# Arg1 - "skip" flag
# Arg2 - product type
# Arg3 - product version
# Arg4 - product plugins path
# Arg5 - template module path
# Arg6 - cartridge docker build script path
# Arg7 - docker image name
function build_image () {
    echo "skip flag: ${1}"
    echo "product type: ${2}"
    echo "product version: ${3}"
    echo "product plugins path: ${4}"
    echo "template module path: ${5}"
    echo "cartridge docker build script path: ${6}"
    echo "docker image name: ${7}"

    if ! [[ "${skip_template_build}" = "true" ]] ; then
       echo "-----------------------------------"
       echo "Building" $2 - $3 "template module"
       echo "-----------------------------------"
       pushd $5
       mvn clean install
       cp -v target/$2-$3-template-module-${VERSION}.zip $6/packages/
       popd

       echo "----------------------------------"
       echo "Copying" $2 - $3 "python plugins"
       echo "----------------------------------"
       pushd $4
       cp * $6/plugins
       popd

       echo "----------------------------------"
       echo "Copying" $2 - $3 "common plugins"
       echo "----------------------------------"
       pushd ${common_plugin_path}
       cp * $6/plugins
       popd
    fi

    echo "----------------------------------"
    echo "Building" $2 - $3 "docker image"
    echo "----------------------------------"
    sudo docker build -t wso2/$7-$3:$IMAGE_VERSION .

    echo $2 - $3 "docker image built successfully."
}