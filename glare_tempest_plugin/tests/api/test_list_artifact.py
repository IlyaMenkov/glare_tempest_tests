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


import os
import testtools

from tempest import config

from glare_tempest_plugin.tests.api import base

CONF = config.CONF


class TestListSanity(base.BaseArtifactTest):

    @testtools.testcase.attr('smoke')
    def test_list_artifacts(self):
        art = self.artifacts_client.create_artifact('images', 'tempest_test')
        art_list = self.artifacts_client.list_artifacts('images')
        raise RuntimeError(art_list)
