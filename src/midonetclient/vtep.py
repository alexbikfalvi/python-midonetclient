# Copyright (c) 2014 Midokura SARL, All Rights Reserved.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
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
from midonetclient.vtep_binding import VtepBinding

class Vtep(ResourceBase):

    media_type = vendor_media_type.APPLICATION_VTEP_JSON
    PORT_NAME = '{portName}'
    VLAN_ID = '{vlanId}'

    def __init__(self, uri, dto, auth):
        super(Vtep, self).__init__(uri, dto, auth)

    def get_name(self):
        return self.dto['name']

    def get_description(self):
        return self.dto['description']

    def get_management_ip(self):
        return self.dto['managementIp']

    def get_management_port(self):
        return self.dto['managementPort']

    def get_tunnel_ip_addresses(self):
        return self.dto['tunnelIpAddrs']

    def get_connection_state(self):
        return self.dto['connectionState']

    def get_tunnel_zone_id(self):
        return self.dto['tunnelZoneId']

    def get_id(self):
        """Returns a VtepId for this VTEP."""
        return VtepId(self.get_management_ip())

    def name(self, name):
        self.dto['name'] = name
        return self

    def description(self, desc):
        self.dto['description'] = desc
        return self

    def management_ip(self, ip_addr):
        self.dto['managementIp'] = ip_addr
        return self

    def management_port(self, port):
        self.dto['managementPort'] = port
        return self

    def tunnel_ip_addresses(self, addresses):
        self.dto['tunnelIpAddrs'] = addresses
        return self

    def connection_state(self, conn_state):
        self.dto['connectionState'] = conn_state
        return self

    def tunnel_zone_id(self, tunnel_zone_id):
        self.dto['tunnelZoneId'] = tunnel_zone_id
        return self

    def get_vtep_binding_template(self):
        return self.dto['vtepBindingTemplate']

    def get_bindings(self):
        query = {}
        headers = {'Accept':
                   vendor_media_type.APPLICATION_VTEP_BINDING_COLLECTION_JSON}
        return self.get_children(self.dto['bindings'],
                                 query,
                                 headers,
                                 VtepBinding)

    def add_binding(self):
        return VtepBinding(self.dto['bindings'],
                           {'mgmtIp': self.get_management_ip()},
                           self.auth)

    def get_binding(self, binding_id):
        """Returns a binding for this VTEP with the given VtepBindingId.

        Args:
            binding_id: A VtepBindingId.
        Returns:
            A binding for this VTEP with the given VtepBindingId.
        """
        return self._get_resource_with_params(
                VtepBinding, self.get_uri(), self.get_vtep_binding_template(),
                {self.PORT_NAME : binding_id.port_name,
                 self.VLAN_ID : binding_id.vlan_id})


class VtepId(ResourceId):
    """Represents a VTEP ID, which is its management IP address."""
    def __init__(self, ip_addr):
        super(ResourceId, self).__init__()

        if not is_valid_ipv4_address(ip_addr):
            raise Exception("Invalid IPv4 address passed to VtepId.")
        self.management_ip = ip_addr

    def __str__(self):
        return 'VTEP-MANAGEMENT-IP:%s' % self.management_ip

    def __eq__(self, other):
        return (isinstance(other, VtepId) and
                self.management_ip == other.management_ip)

    def __hash__(self):
        return self.management_ip.__hash__()
