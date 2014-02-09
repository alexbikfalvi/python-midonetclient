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
import webob.exc as exc

from midonetclient.neutron.client import MidonetClient


logging.basicConfig(format="%(asctime)-15s %(name)s %(message)s")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


def test_network_crud(client):
    print '-------- Testing Network CRUD-----'
    id = str(uuid.uuid4())
    input = {"id": id,
             "name": "name",
             "tenant_id": "tenant_id",
             "admin_state_up": True,
             "router:external": True}
    output = client.create_network(input)
    assert output["id"] == id

    test_subnet_crud(client, id)
    test_subnet_bulk(client, id)

    output["admin_state_up"] = False
    client.update_network(id, output)
    output = client.get_network(id)
    assert output["admin_state_up"] is False

    client.delete_network(id)

    try:
        client.get_network(id)
        assert False
    except exc.HTTPNotFound:
        pass


def test_network_bulk(client):
    print '-------- Testing Network Bulk-----'
    id1 = str(uuid.uuid4())
    id2 = str(uuid.uuid4())
    input = [{"id": id1,
              "name": "name1",
              "tenant_id": "tenant_id1",
              "admin_state_up": True},
             {"id": id2,
              "name": "name2",
              "tenant_id": "tenant_id2",
              "admin_state_up": False}]

    output = client.create_network_bulk(input)
    assert len(output) == 2
    diff = [x for x in output if x["id"] not in [id1, id2]]
    assert len(diff) == 0

    client.delete_network(id1)
    client.delete_network(id2)


def test_subnet_crud(client, net_id):
    print '-------- Testing Subnet CRUD-----'
    id = str(uuid.uuid4())
    input = {"id": id,
             "name": "name",
             "tenant_id": "tenant_id",
             "ip_version": 4,
             "network_id": net_id,
             "cidr": "10.0.0.0/24",
             "gateway_ip": "10.0.0.1",
             "enable_dhcp": True,
             "shared": False}
    output = client.create_subnet(input)
    assert output["id"] == id

    output["enable_dhcp"] = False
    output = client.update_subnet(id, output)
    print output
    assert output["enable_dhcp"] is False

    output["enable_dhcp"] = True
    output = client.update_subnet(id, output)
    assert output["enable_dhcp"] is True

    client.delete_subnet(id)

    try:
        client.get_subnet(id)
        assert False
    except exc.HTTPNotFound:
        pass


def test_subnet_bulk(client, net_id):
    print '-------- Testing Subnet Bulk-----'
    id1 = str(uuid.uuid4())
    id2 = str(uuid.uuid4())
    input = [{"id": id1,
             "name": "name1",
             "tenant_id": "tenant_id1",
             "ip_version": 4,
             "network_id": net_id,
             "cidr": "10.0.0.0/24",
             "gateway_ip": "10.0.0.1",
             "enable_dhcp": True,
             "shared": False},
             {"id": id2,
              "name": "name2",
              "tenant_id": "tenant_id2",
              "ip_version": 4,
              "network_id": net_id,
              "cidr": "10.0.1.0/24",
              "gateway_ip": "10.0.1.1",
              "enable_dhcp": False,
              "shared": True}]

    output = client.create_subnet_bulk(input)
    assert len(output) == 2
    diff = [x for x in output if x["id"] not in [id1, id2]]
    assert len(diff) == 0

    client.delete_subnet(id1)
    client.delete_subnet(id2)


def test_security_group_crud(client):
    print '-------- Testing Security Group CRUD-----'
    id = str(uuid.uuid4())
    input = {"id": id,
             "name": "name1",
             "tenant_id": "tenant_id",
             "description": "description"}
    output = client.create_security_group(input)
    assert output["id"] == id
    assert output["name"] == "name1"

    test_security_group_rule_crud(client, id)
    test_security_group_rule_bulk(client, id)

    output["name"] = "name2"
    client.update_security_group(id, output)
    output = client.get_security_group(id)
    assert output["name"] == "name2"

    client.delete_security_group(id)
    try:
        client.get_security_group(id)
        assert False
    except exc.HTTPNotFound:
        pass


def test_security_group_bulk(client):
    print '-------- Testing Security Group Bulk-----'
    id1 = str(uuid.uuid4())
    id2 = str(uuid.uuid4())
    input = [{"id": id1,
              "name": "name1",
              "tenant_id": "tenant_id1",
              "description": "description1"},
             {"id": id2,
              "name": "name2",
              "tenant_id": "tenant_id2",
              "description": "description2"}]

    output = client.create_security_group_bulk(input)
    assert len(output) == 2
    diff = [x for x in output if x["id"] not in [id1, id2]]
    assert len(diff) == 0

    client.delete_security_group(id1)
    client.delete_security_group(id2)


def test_security_group_rule_crud(client, sg_id):
    print '-------- Testing Security Group Rule CRUD-----'
    id = str(uuid.uuid4())
    input = {"id": id,
             "direction": "ingress",
             "tenant_id": "tenant_id",
             "ethertype": "ipv4",
             "port_range_max": 100,
             "port_range_min": 50,
             "protocol": "tcp",
             "remote_ip_prefix": "10.0.0.3/24",
             "security_group_id": sg_id}
    output = client.create_security_group_rule(input)
    assert output["id"] == id
    assert output["security_group_id"] == sg_id

    client.delete_security_group_rule(id)
    try:
        client.get_security_group_rule(id)
        assert False
    except exc.HTTPNotFound:
        pass


def test_security_group_rule_bulk(client, sg_id):
    print '-------- Testing Security Group Rule bulk-----'
    id1 = str(uuid.uuid4())
    id2 = str(uuid.uuid4())
    input = [{"id": id1,
              "direction": "ingress",
              "tenant_id": "tenant_id1",
              "ethertype": "ipv4",
              "port_range_max": 100,
              "port_range_min": 50,
              "protocol": "tcp",
              "remote_ip_prefix": "10.0.0.3/24",
              "security_group_id": sg_id},
             {"id": id2,
              "direction": "egress",
              "tenant_id": "tenant_id2",
              "ethertype": "ipv4",
              "port_range_max": 200,
              "port_range_min": 200,
              "protocol": "icmp",
              "security_group_id": sg_id}]
    output = client.create_security_group_rule_bulk(input)
    assert len(output) == 2
    diff = [x for x in output if x["id"] not in [id1, id2]]
    assert len(diff) == 0

    # Check the rules from sg
    sg2 = client.get_security_group(sg_id)
    assert sg2["id"] == sg_id
    assert len(sg2["security_group_rules"]) == 2
    diff = [x for x in sg2["security_group_rules"]
            if x["id"] not in [id1, id2]]
    assert len(diff) == 0

    client.delete_security_group_rule(id1)
    client.delete_security_group_rule(id2)


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

    test_network_crud(client)
    test_network_bulk(client)
    test_security_group_crud(client)
    test_security_group_bulk(client)


if __name__ == "__main__":
    main()
