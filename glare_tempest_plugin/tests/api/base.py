# Copyright 2016 Red Hat, Inc.
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


from tempest import config
from tempest import exceptions
from tempest.lib import exceptions as lib_exc
import tempest.test
from tempest.lib import base
from glare_tempest_plugin import clients
from glare_tempest_plugin.common import plugin_utils


CONF = config.CONF


class BaseArtifactTest(base.BaseTestCase):


    @classmethod
    def setUpClass(cls):
        super(BaseArtifactTest, cls).setUpClass()
        cls.resource_setup()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def get_client_with_isolated_creds(cls, type_of_creds="admin"):
        creds = cls.get_configured_isolated_creds(type_of_creds=type_of_creds)

        os = clients.Manager(credentials=creds)
        client = os.artifact_client