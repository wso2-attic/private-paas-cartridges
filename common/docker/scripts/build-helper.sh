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

# Arg1  - "skip" flag
# Arg2  - product type
# Arg3  - product version
# Arg4  - product plugins path
# Arg5  - template module path
# Arg6  - cartridge docker build script path
# Arg7  - docker image name
# Arg8  - common plugin path
# Arg9  - Docker image version
# Arg10 - Project version
function build_image () {
    echo "skip flag: ${1}"
    echo "product type: ${2}"
    echo "product version: ${3}"
    echo "product plugins path: ${4}"
    echo "template module path: ${5}"
    echo "cartridge docker build script path: ${6}"
    echo "docker image name: ${7}"
    echo "common plugin path: ${8}"
    echo "Docker image version: ${9}"
    echo "Project version: ${10}"

    if ! [[ "${1}" = "true" ]] ; then
       echo "-----------------------------------"
       echo "Building" $2 - $3 "template module"
       echo "-----------------------------------"
       pushd $5
       mvn clean install
       cp -v target/$2-$3-template-module-${10}.zip $6/packages/
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
       pushd ${8}
       cp *.py *.yapsy-plugin $6/plugins
       popd
    fi

    echo "----------------------------------"
    echo "Building" $2 - $3 "docker image"
    echo "----------------------------------"
    sudo docker build -t wso2/$7-$3:$9 .

    echo $2 - $3 "docker image built successfully."
}