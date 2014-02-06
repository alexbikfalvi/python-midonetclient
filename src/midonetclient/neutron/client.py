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

    def list_networks(self):
        LOG.info("list_networks")
        return self.client.get(self.networks_url(), MediaType.NETWORKS)

    def update_network(self, id, network):
        LOG.info("update_network %r", network)
        self.client.put(self.network_url(id), MediaType.NETWORK, network)

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

    def list_security_groups(self):
        LOG.info("list_security_groups")
        return self.client.get(self.security_groups_url(),
                               MediaType.SECURITY_GROUPS)

    def update_security_group(self, id, security_group):
        LOG.info("update_security_group %r", security_group)
        self.client.put(self.security_group_url(id), MediaType.SECURITY_GROUP,
                        security_group)

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
