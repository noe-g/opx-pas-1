#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2019 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.


from sos.plugins import Plugin, DebianPlugin
import os

class DN_pas(Plugin,DebianPlugin):
    """ Collects opx-show-env output """

    plugin_name = os.path.splitext(os.path.basename(__file__))[0]
    profiles = ('networking','opx')

    def setup(self):
        self.add_cmd_output("/usr/bin/opx-show-env")
