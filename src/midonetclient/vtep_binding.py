# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from midonetclient import vendor_media_type
from midonetclient.resource_base import ResourceBase
from midonetclient.resource_base import ResourceId
from midonetclient.util import is_valid_ipv4_address

class VtepBinding(ResourceBase):

    media_type = vendor_media_type.APPLICATION_VTEP_BINDING_JSON

    def __init__(self, uri, dto, auth):
        super(VtepBinding, self).__init__(uri, dto, auth)

    def get_id(self):
        """Returns a VtepBindingId for this binding.

        The ID of a VTEP binding is a composite key of its management IP,
        physical port, and VLAN ID.
        """
        return VtepBindingId(self.get_mgmt_ip(),
                             self.get_port_name(),
                             self.get_vlan_id())

    def get_mgmt_ip(self):
        return self.dto['mgmtIp']

    def get_port_name(self):
        return self.dto['portName']

    def get_vlan_id(self):
        return self.dto['vlanId']

    def get_network_id(self):
        return self.dto['networkId']

    def mgmt_ip(self, management_ip):
        self.dto['mgmtIP'] = management_ip
        return self

    def port_name(self, port_name):
        self.dto['portName'] = port_name
        return self

    def vlan_id(self, vlan_id):
        self.dto['vlanId'] = vlan_id
        return self

    def network_id(self, network_id):
        self.dto['networkId'] = network_id
        return self


class VtepBindingId(ResourceId):
    """Represents a VTEP binding composite ID."""
    def __init__(self, management_ip, port_name, vlan_id):
        super(ResourceId, self).__init__()

        if not is_valid_ipv4_address(management_ip):
            raise Exception("Invalid IPv4 address passed to VtepBindingId.")
        self.management_ip = management_ip
        self.port_name = port_name
        self.vlan_id = vlan_id

    def __str__(self):
        return ('VTEPBinding:VTEP-MANAGEMENT-IP=%s,'
                'PORT-NAME=%s,VLAN=%s' % (self.management_ip,
                                          self.port_name,
                                          str(self.vlan_id)))

    def __eq__(self, other):
        return (isinstance(other, VtepBindingId) and
                self.management_ip == other.management_ip and
                self.port_name == other.port_name and
                self.vlan_id == other.vlan_id)

    def __hash__(self):
        return str(self).__hash__()
