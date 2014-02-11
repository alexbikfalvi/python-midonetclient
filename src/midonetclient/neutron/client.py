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

from midonetclient.httpclient import HttpClient

LOG = logging.getLogger(__name__)


class MediaType(object):

    APP = "application/vnd.org.midonet.Application-v3+json"
    NEUTRON = "application/vnd.org.midonet.neutron.Neutron-v1+json"
    NETWORK = "application/vnd.org.midonet.neutron.Network-v1+json"
    NETWORKS = "application/vnd.org.midonet.neutron.Networks-v1+json"
    SUBNET = "application/vnd.org.midonet.neutron.Subnet-v1+json"
    SUBNETS = "application/vnd.org.midonet.neutron.Subnets-v1+json"
    PORT = "application/vnd.org.midonet.neutron.Port-v1+json"
    PORTS = "application/vnd.org.midonet.neutron.Ports-v1+json"
    ROUTER = "application/vnd.org.midonet.neutron.Router-v1+json"
    ROUTERS = "application/vnd.org.midonet.neutron.Routers-v1+json"
    SECURITY_GROUP = \
        "application/vnd.org.midonet.neutron.SecurityGroup-v1+json"
    SECURITY_GROUPS = \
        "application/vnd.org.midonet.neutron.SecurityGroups-v1+json"
    SECURITY_GROUP_RULE = \
        "application/vnd.org.midonet.neutron.SecurityGroupRule-v1+json"
    SECURITY_GROUP_RULES = \
        "application/vnd.org.midonet.neutron.SecurityGroupRules-v1+json"


class UrlProvider(object):

    def __init__(self):
        self.app = None
        self.neutron = None
        self.cache = {}

    def _get_application(self):
        if self.app is None:
            self.app = self.client.get(self.base_uri, MediaType.APP)
        return self.app

    def _get_neutron(self):
        if self.neutron is None:
            app = self._get_application()
            self.neutron = self.client.get(app["neutron"], MediaType.NEUTRON)
        return self.neutron

    def network_url(self, id):
        return self._get_neutron()["network_template"].replace("{id}", id)

    def networks_url(self):
        return self._get_neutron()["networks"]

    def subnet_url(self, id):
        return self._get_neutron()["subnet_template"].replace("{id}", id)

    def subnets_url(self):
        return self._get_neutron()["subnets"]

    def port_url(self, id):
        return self._get_neutron()["port_template"].replace("{id}", id)

    def ports_url(self):
        return self._get_neutron()["ports"]

    def router_url(self, id):
        return self._get_neutron()["router_template"].replace("{id}", id)

    def routers_url(self):
        return self._get_neutron()["routers"]

    def security_group_url(self, id):
        return self._get_neutron()["security_group_template"].replace(
            "{id}", id)

    def security_groups_url(self):
        return self._get_neutron()["security_groups"]

    def security_group_rule_url(self, id):
        return self._get_neutron()["security_group_rule_template"].replace(
            "{id}", id)

    def security_group_rules_url(self):
        return self._get_neutron()["security_group_rules"]


class MidonetClient(UrlProvider):

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri
        self.client = HttpClient(base_uri, username, password,
                                 project_id=project_id)
        super(MidonetClient, self).__init__()

    def create_network(self, network):
        LOG.info("create_network %r", network)
        return self.client.post(self.networks_url(), MediaType.NETWORK,
                                body=network)

    def create_network_bulk(self, networks):
        LOG.info("create_network_bulk entered")
        return self.client.post(self.networks_url(), MediaType.NETWORKS,
                                body=networks)

    def delete_network(self, id):
        LOG.info("delete_network %r", id)
        self.client.delete(self.network_url(id))

    def get_network(self, id):
        LOG.info("get_network %r", id)
        return self.client.get(self.network_url(id), MediaType.NETWORK)

    def get_networks(self):
        LOG.info("get_networks")
        return self.client.get(self.networks_url(), MediaType.NETWORKS)

    def update_network(self, id, network):
        LOG.info("update_network %r", network)
        return self.client.put(self.network_url(id), MediaType.NETWORK,
                               network)

    def create_subnet(self, subnet):
        LOG.info("create_subnet %r", subnet)
        return self.client.post(self.subnets_url(), MediaType.SUBNET,
                                body=subnet)

    def create_subnet_bulk(self, subnets):
        LOG.info("create_subnet_bulk entered")
        return self.client.post(self.subnets_url(), MediaType.SUBNETS,
                                body=subnets)

    def delete_subnet(self, id):
        LOG.info("delete_subnet %r", id)
        self.client.delete(self.subnet_url(id))

    def get_subnet(self, id):
        LOG.info("get_subnet %r", id)
        return self.client.get(self.subnet_url(id), MediaType.SUBNET)

    def get_subnets(self):
        LOG.info("get_subnets")
        return self.client.get(self.subnets_url(), MediaType.SUBNETS)

    def update_subnet(self, id, subnet):
        LOG.info("update_subnet %r", subnet)
        return self.client.put(self.subnet_url(id), MediaType.SUBNET, subnet)

    def create_port(self, port):
        LOG.info("create_port %r", port)
        return self.client.post(self.ports_url(), MediaType.PORT, body=port)

    def create_port_bulk(self, ports):
        LOG.info("create_port_bulk entered")
        return self.client.post(self.ports_url(), MediaType.PORTS, body=ports)

    def delete_port(self, id):
        LOG.info("delete_port %r", id)
        self.client.delete(self.port_url(id))

    def get_port(self, id):
        LOG.info("get_port %r", id)
        return self.client.get(self.port_url(id), MediaType.PORT)

    def get_ports(self):
        LOG.info("get_ports")
        return self.client.get(self.ports_url(), MediaType.PORTS)

    def update_port(self, id, port):
        LOG.info("update_port %r", port)
        return self.client.put(self.port_url(id), MediaType.PORT, port)

    def create_router(self, router):
        LOG.info("create_router %r", router)
        return self.client.post(self.routers_url(), MediaType.ROUTER,
                                body=router)

    def delete_router(self, id):
        LOG.info("delete_router %r", id)
        self.client.delete(self.router_url(id))

    def get_router(self, id):
        LOG.info("get_router %r", id)
        return self.client.get(self.router_url(id), MediaType.ROUTER)

    def get_routers(self):
        LOG.info("get_routers")
        return self.client.get(self.routers_url(), MediaType.ROUTERS)

    def update_router(self, id, router):
        LOG.info("update_router %r", router)
        return self.client.put(self.router_url(id), MediaType.ROUTER, router)

    def create_security_group(self, security_group):
        LOG.info("create_security_group %r", security_group)
        return self.client.post(self.security_groups_url(),
                                MediaType.SECURITY_GROUP,
                                body=security_group)

    def create_security_group_bulk(self, security_groups):
        LOG.info("create_security_group_bulk entered")
        return self.client.post(self.security_groups_url(),
                                MediaType.SECURITY_GROUPS,
                                body=security_groups)

    def delete_security_group(self, id):
        LOG.info("delete_security_group %r", id)
        self.client.delete(self.security_group_url(id))

    def get_security_group(self, id):
        LOG.info("get_security_group %r", id)
        return self.client.get(self.security_group_url(id),
                               MediaType.SECURITY_GROUP)

    def get_security_groups(self):
        LOG.info("get_security_groups")
        return self.client.get(self.security_groups_url(),
                               MediaType.SECURITY_GROUPS)

    def update_security_group(self, id, security_group):
        LOG.info("update_security_group %r", security_group)
        return self.client.put(self.security_group_url(id),
                               MediaType.SECURITY_GROUP, security_group)

    def create_security_group_rule(self, security_group_rule):
        LOG.info("create_security_group_rule %r", security_group_rule)
        return self.client.post(self.security_group_rules_url(),
                                MediaType.SECURITY_GROUP_RULE,
                                body=security_group_rule)

    def create_security_group_rule_bulk(self, security_group_rules):
        LOG.info("create_security_group_rule_bulk entered")
        return self.client.post(self.security_group_rules_url(),
                                MediaType.SECURITY_GROUP_RULES,
                                body=security_group_rules)

    def delete_security_group_rule(self, id):
        LOG.info("delete_security_group_rule %r", id)
        self.client.delete(self.security_group_rule_url(id))

    def get_security_group_rule(self, id):
        LOG.info("get_security_group_rule %r", id)
        return self.client.get(self.security_group_rule_url(id),
                               MediaType.SECURITY_GROUP_RULE)
