# Copyright (c) 2016 Mirantis, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import json

from tempest import config
from tempest.lib.common import rest_client

CONF = config.CONF

class ArtifactsClient(rest_client.RestClient):

    def __init__(self, auth_provider):
        super(ArtifactsClient, self.__init__(
            auth_provider,
            CONF.identity.region,
            CONF.artifacts.endpoint_type
            ))

    def _request_and_check_resp(self, request_func, uri,
                                rest_status):
        resp, body = request_func(uri)
        self.expected_success(rest_status, body)
        return rest_client.ResponseBody(resp, body)

    def _request_and_check_resp_data(self, request_func, uri, resp_status):
        resp, body = request_func(uri)
        self.expected_success(resp_status, resp.status)
        return resp, body

    def list_all_artifacts(self):
        uri = 'v1/artifacts/all'
        resp, body = self.get(uri)
        self.expected_success(200, resp.status)
        parsed = self._parse_resp(body)
        return parsed['artifacts']

