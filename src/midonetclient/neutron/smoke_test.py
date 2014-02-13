# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014 Midokura PTE LTD.
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
#
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

import logging
import sys
import uuid

from midonetclient.neutron.client import MidonetClient


logging.basicConfig(format="%(asctime)-15s %(name)s %(message)s")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


def smoke_test(client):
    print '-------- Midonet Client Smoke Test Starting-----'

    # Create a network
    net_id = str(uuid.uuid4())
    input = {"id": net_id,
             "name": "tenant",
             "tenant_id": "tenant",
             "admin_state_up": True,
             "router:external": False}
    output = client.create_network(input)
    assert output["id"] == net_id
    print '-------- network created: %s----' % net_id

    # Create an external network
    ext_net_id = str(uuid.uuid4())
    input = {"id": ext_net_id,
             "name": "provider",
             "tenant_id": "provider",
             "admin_state_up": True,
             "router:external": True}
    output = client.create_network(input)
    assert output["id"] == ext_net_id
    print '-------- external network created: %s----' % ext_net_id

    # Create a subnet on each
    subnet_id = str(uuid.uuid4())
    input = {"id": subnet_id,
             "name": "tenant",
             "tenant_id": "tenant",
             "ip_version": 4,
             "network_id": net_id,
             "cidr": "10.0.0.0/24",
             "gateway_ip": "10.0.0.1",
             "enable_dhcp": True,
             "shared": False}
    output = client.create_subnet(input)
    assert output["id"] == subnet_id
    print '-------- subnet created: %s-----' % subnet_id

    ext_subnet_id = str(uuid.uuid4())
    input = {"id": ext_subnet_id,
             "name": "provider",
             "tenant_id": "provider",
             "ip_version": 4,
             "network_id": ext_net_id,
             "cidr": "200.0.0.0/24",
             "gateway_ip": "200.0.0.1",
             "enable_dhcp": False,
             "shared": False}
    output = client.create_subnet(input)
    assert output["id"] == ext_subnet_id
    print '-------- external net subnet created: %s-----' % ext_subnet_id

    # Create a security group
    sg_id = str(uuid.uuid4())
    input = {"id": sg_id,
             "name": "tenant",
             "tenant_id": "tenant",
             "description": "description"}
    output = client.create_security_group(input)
    assert output["id"] == sg_id
    print '-------- security group created: %s-----' % sg_id

    # Create an ingress TCP security group rule
    ingress_rule_id = str(uuid.uuid4())
    input = {"id": ingress_rule_id,
             "direction": "ingress",
             "tenant_id": "tenant",
             "ethertype": "ipv4",
             "port_range_max": 100,
             "port_range_min": 50,
             "protocol": "tcp",
             "remote_ip_prefix": "10.0.0.3/24",
             "security_group_id": sg_id}
    output = client.create_security_group_rule(input)
    assert output["id"] == ingress_rule_id
    print '-------- ingress sg rule created: %s-----' % ingress_rule_id

    # Create an egress ICMP security group rule
    egress_rule_id = str(uuid.uuid4())
    input = {"id": egress_rule_id,
             "direction": "egress",
             "tenant_id": "tenant",
             "ethertype": "ipv4",
             "port_range_max": 200,
             "port_range_min": 200,
             "protocol": "icmp",
             "remote_group_id": sg_id,
             "security_group_id": sg_id}
    output = client.create_security_group_rule(input)
    assert output["id"] == egress_rule_id
    print '-------- egress sg rule created: %s-----' % egress_rule_id

    # Create a port on tenant network and assign a security group.
    port_id = str(uuid.uuid4())
    input = {"id": port_id,
             "network_id": net_id,
             "name": "tenant",
             "tenant_id": "tenant",
             "admin_state_up": True,
             "mac_address": "3e:d0:70:c3:ea:e3",
             "fixed_ips": [{
                 "ip_address": "10.0.0.3",
                 "subnet_id": subnet_id
             }],
             "security_groups": [sg_id]}
    output = client.create_port(input)
    assert output["id"] == port_id
    print '-------- port created: %s-----' % port_id

    # TODO: Find a way to emulate attaching the router to a provider router.

    # Create a router that's linked to the external network
    router_id = str(uuid.uuid4())
    input = {"id": router_id,
             "name": "name",
             "admin_state_up": True,
             "tenant_id": "tenant",
             "external_gateway_info": {
                 "network_id": ext_net_id,
                 "enable_snat": True
             }}
    output = client.create_router(input)
    assert output["id"] == router_id
    print '-------- router created: %s-----' % router_id

    # Add a router interface
    interface_input = {"subnet_id": subnet_id}
    output = client.add_router_interface(router_id, interface_input)
    assert output["port_id"] is not None
    print '-------- router interface added: %s-----' % output["port_id"]

    # Create a floating IP on the external network
    floating_ip_id = str(uuid.uuid4())
    input = {"id": floating_ip_id,
             "floating_network_id": ext_net_id}
    output = client.create_floating_ip(input)
    assert output["id"] == floating_ip_id
    print '-------- floating IP created: %s-----' % floating_ip_id

    # TODO Add updates, especially for routers and floating IP

    print '-------- Cleaning Up ----------'

    # Remove floating IP
    client.delete_floating_ip(floating_ip_id)
    print '-------- floating IP deleted: %s-----' % floating_ip_id

    # Remove router interface
    client.remove_router_interface(router_id, interface_input)
    print '-------- router interface deleted: %s-----' % subnet_id

    # Delete everything
    client.delete_router(router_id)
    print '-------- router deleted: %s-----' % router_id

    client.delete_port(port_id)
    print '-------- port deleted: %s-----' % port_id

    client.delete_security_group_rule(egress_rule_id)
    print '-------- egress SG rule deleted: %s-----' % egress_rule_id

    client.delete_security_group_rule(ingress_rule_id)
    print '-------- ingress SG rule deleted: %s-----' % ingress_rule_id

    client.delete_security_group(sg_id)
    print '-------- security group deleted: %s-----' % sg_id

    client.delete_subnet(ext_subnet_id)
    print '-------- external net subnet deleted: %s-----' % ext_subnet_id

    client.delete_subnet(subnet_id)
    print '-------- subnet deleted: %s-----' % subnet_id

    client.delete_network(ext_net_id)
    print '-------- external network deleted: %s-----' % ext_net_id

    client.delete_network(net_id)
    print '-------- network deleted: %s-----' % net_id

    print '---------- Midonet Client Smoke Test Completed! -----------'


def main():

    if len(sys.argv) < 4:
        print >> sys.stderr, "Functional testing "
        print >> sys.stderr, "Usage: " + sys.argv[0] \
            + " <URI> <username> <password> [project_id]"
        sys.exit(-1)

    uri = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    if len(sys.argv) > 4:
        project_id = sys.argv[4]
    else:
        project_id = None

    client = MidonetClient(uri, username, password, project_id=project_id)

    smoke_test(client)


if __name__ == "__main__":
    main()
