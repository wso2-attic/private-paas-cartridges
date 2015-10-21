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

# Start an GREG cluster with docker
memberId=1
version=`head -50 ../pom.xml | awk -F'>' '/version/ {printf $2}' | awk -F'<' '{print $1}'`
image_version=${version%-*} # Remove the SNAPSHOT string for non-released versions

startWkaMember() {
	name="wso2greg-${memberId}-wka"
	container_id=`docker run -e CONFIG_PARAM_CLUSTERING=true -e CONFIG_PARAM_MEMBERSHIP_SCHEME=wka -d -P --name ${name} wso2/greg-5.0.0:${image_version}`
	memberId=$((memberId + 1))
	wka_member_ip=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' ${container_id}`
	echo "GREG wka member started: [name] ${name} [ip] ${wka_member_ip} [container-id] ${container_id}"
	sleep 1
}

startMember() {
	name="wso2greg-${memberId}"
	container_id=`docker run -e CONFIG_PARAM_CLUSTERING=true -e CONFIG_PARAM_MEMBERSHIP_SCHEME=wka -e CONFIG_PARAM_WKA_MEMBERS="["${wka_member_ip}:4000]"" -d -P --name ${name} wso2/greg-5.0.0:${image_version}`
	memberId=$((memberId + 1))
	member_ip=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' ${container_id}`
	echo "GREG member started: [name] ${name} [ip] ${member_ip} [container-id] ${container_id}"
	sleep 1
}

echo "Starting an GREG cluster with docker..."
startWkaMember
startMember
startMember
