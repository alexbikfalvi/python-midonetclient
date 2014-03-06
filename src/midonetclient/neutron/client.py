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
from midonetclient.neutron import media_type

from midonetclient.httpclient import HttpClient

LOG = logging.getLogger(__name__)


class UrlProvider(object):

    def __init__(self):
        self.app = None
        self.neutron = None
        self.cache = {}

    def _get_application(self):
        if self.app is None:
            self.app = self.client.get(self.base_uri, media_type.APP)
        return self.app

    def _get_neutron(self):
        if self.neutron is None:
            app = self._get_application()
            self.neutron = self.client.get(app["neutron"], media_type.NEUTRON)
        return self.neutron


class L3(object):

    def router_url(self, id):
        return self._get_neutron()["router_template"].replace("{id}", id)

    def routers_url(self):
        return self._get_neutron()["routers"]

    def add_router_interface_url(self, router_id):
        return self._get_neutron()["add_router_interface_template"].replace(
            "{id}", router_id)

    def remove_router_interface_url(self, router_id):
        return self._get_neutron()["remove_router_interface_template"].replace(
            "{id}", router_id)

    def floating_ip_url(self, id):
        return self._get_neutron()["floating_ip_template"].replace("{id}", id)

    def floating_ips_url(self):
        return self._get_neutron()["floating_ips"]

    def create_router(self, router):
        LOG.info("create_router %r", router)
        return self.client.post(self.routers_url(), media_type.ROUTER,
                                body=router)

    def delete_router(self, id):
        LOG.info("delete_router %r", id)
        self.client.delete(self.router_url(id))

    def get_router(self, id):
        LOG.info("get_router %r", id)
        return self.client.get(self.router_url(id), media_type.ROUTER)

    def get_routers(self):
        LOG.info("get_routers")
        return self.client.get(self.routers_url(), media_type.ROUTERS)

    def update_router(self, id, router):
        LOG.info("update_router %r", router)
        return self.client.put(self.router_url(id), media_type.ROUTER, router)

    def add_router_interface(self, router_id, interface_info):
        LOG.info("add_router_interface %r %r", (router_id, interface_info))
        return self.client.put(self.add_router_interface_url(router_id),
                               media_type.ROUTER_INTERFACE, interface_info)

    def remove_router_interface(self, router_id, interface_info):
        LOG.info("remove_router_interface %r %r", (router_id, interface_info))
        return self.client.put(self.remove_router_interface_url(router_id),
                               media_type.ROUTER_INTERFACE, interface_info)

    def create_floating_ip(self, floating_ip):
        LOG.info("create_floating_ip %r", floating_ip)
        return self.client.post(self.floating_ips_url(),
                                media_type.FLOATING_IP, body=floating_ip)

    def delete_floating_ip(self, id):
        LOG.info("delete_floating_ip %r", id)
        self.client.delete(self.floating_ip_url(id))

    def get_floating_ip(self, id):
        LOG.info("get_floating_ip %r", id)
        return self.client.get(self.floating_ip_url(id),
                               media_type.FLOATING_IP)

    def get_floating_ips(self):
        LOG.info("get_floating_ips")
        return self.client.get(self.floating_ips_url(),
                               media_type.FLOATING_IPS)

    def update_floating_ip(self, id, floating_ip):
        LOG.info("update_floating_ip %r", floating_ip)
        return self.client.put(self.floating_ip_url(id),
                               media_type.FLOATING_IP,
                               floating_ip)


class SecurityGroup(object):

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

    def create_security_group(self, security_group):
        LOG.info("create_security_group %r", security_group)
        return self.client.post(self.security_groups_url(),
                                media_type.SECURITY_GROUP,
                                body=security_group)

    def create_security_group_bulk(self, security_groups):
        LOG.info("create_security_group_bulk entered")
        return self.client.post(self.security_groups_url(),
                                media_type.SECURITY_GROUPS,
                                body=security_groups)

    def delete_security_group(self, id):
        LOG.info("delete_security_group %r", id)
        self.client.delete(self.security_group_url(id))

    def get_security_group(self, id):
        LOG.info("get_security_group %r", id)
        return self.client.get(self.security_group_url(id),
                               media_type.SECURITY_GROUP)

    def get_security_groups(self):
        LOG.info("get_security_groups")
        return self.client.get(self.security_groups_url(),
                               media_type.SECURITY_GROUPS)

    def update_security_group(self, id, security_group):
        LOG.info("update_security_group %r", security_group)
        return self.client.put(self.security_group_url(id),
                               media_type.SECURITY_GROUP, security_group)

    def create_security_group_rule(self, security_group_rule):
        LOG.info("create_security_group_rule %r", security_group_rule)
        return self.client.post(self.security_group_rules_url(),
                                media_type.SECURITY_GROUP_RULE,
                                body=security_group_rule)

    def create_security_group_rule_bulk(self, security_group_rules):
        LOG.info("create_security_group_rule_bulk entered")
        return self.client.post(self.security_group_rules_url(),
                                media_type.SECURITY_GROUP_RULES,
                                body=security_group_rules)

    def delete_security_group_rule(self, id):
        LOG.info("delete_security_group_rule %r", id)
        self.client.delete(self.security_group_rule_url(id))

    def get_security_group_rule(self, id):
        LOG.info("get_security_group_rule %r", id)
        return self.client.get(self.security_group_rule_url(id),
                               media_type.SECURITY_GROUP_RULE)


class Loadbalancer(object):

    def vip_url(self, id):
        return self._get_neutron()["vip_template"].replace("{id}", id)

    def vips_url(self):
        return self._get_neutron()["vips"]

    def pool_url(self, id):
        return self._get_neutron()["pool_template"].replace("{id}", id)

    def pools_url(self):
        return self._get_neutron()["pools"]

    def member_url(self, id):
        return self._get_neutron()["member_template"].replace("{id}", id)

    def members_url(self):
        return self._get_neutron()["members"]

    def health_monitor_url(self, id):
        return self._get_neutron()["health_monitor_template"].replace(
            "{id}", id)

    def health_monitors_url(self):
        return self._get_neutron()["health_monitors"]

    def pool_health_monitors_url(self, pool_id):
        return self._get_neutron()[
            "pool_health_monitors_template"].replace("{pool_id}", pool_id)

    def pool_health_monitor_url(self, pool_id, health_monitor_id):
        return self._get_neutron()[
            "pool_health_monitor_template"].replace(
            "{pool_id}", pool_id).replace(
            "{health_monitor_id", health_monitor_id)

    def create_vip(self, vip):
        LOG.info("create_vip %r", vip)
        return self.client.post(self.vips_url(), media_type.VIP, body=vip)

    def delete_vip(self, id):
        LOG.info("delete_vip %r", id)
        self.client.delete(self.vip_url(id))

    def get_vip(self, id):
        LOG.info("get_vip %r", id)
        return self.client.get(self.vip_url(id), media_type.VIP)

    def get_vips(self):
        LOG.info("get_vips")
        return self.client.get(self.vips_url(), media_type.VIPS)

    def update_vip(self, id, vip):
        LOG.info("update_vip %r", vip)
        return self.client.put(self.vip_url(id), media_type.VIP, vip)

    def create_pool(self, pool):
        LOG.info("create_pool %r", pool)
        return self.client.post(self.pools_url(), media_type.POOL, body=pool)

    def delete_pool(self, id):
        LOG.info("delete_pool %r", id)
        self.client.delete(self.pool_url(id))

    def get_pool(self, id):
        LOG.info("get_pool %r", id)
        return self.client.get(self.pool_url(id), media_type.POOL)

    def get_pools(self):
        LOG.info("get_pools")
        return self.client.get(self.pools_url(), media_type.POOLS)

    def update_pool(self, id, pool):
        LOG.info("update_pool %r", pool)
        return self.client.put(self.pool_url(id), media_type.POOL, pool)

    def create_member(self, member):
        LOG.info("create_member %r", member)
        return self.client.post(self.members_url(), media_type.MEMBER,
                                body=member)

    def delete_member(self, id):
        LOG.info("delete_member %r", id)
        self.client.delete(self.member_url(id))

    def get_member(self, id):
        LOG.info("get_member %r", id)
        return self.client.get(self.member_url(id), media_type.MEMBER)

    def get_members(self):
        LOG.info("get_members")
        return self.client.get(self.members_url(), media_type.MEMBERS)

    def update_member(self, id, member):
        LOG.info("update_member %r", member)
        return self.client.put(self.member_url(id), media_type.MEMBER, member)

    def create_health_monitor(self, health_monitor):
        LOG.info("create_health_monitor %r", health_monitor)
        return self.client.post(self.health_monitors_url(),
                                media_type.HEALTH_MONITOR,
                                body=health_monitor)

    def delete_health_monitor(self, id):
        LOG.info("delete_health_monitor %r", id)
        self.client.delete(self.health_monitor_url(id))

    def get_health_monitor(self, id):
        LOG.info("get_health_monitor %r", id)
        return self.client.get(self.health_monitor_url(id),
                               media_type.HEALTH_MONITOR)

    def get_health_monitors(self):
        LOG.info("get_health_monitors")
        return self.client.get(self.health_monitors_url(),
                               media_type.HEALTH_MONITORS)

    def update_health_monitor(self, id, health_monitor):
        LOG.info("update_health_monitor %r", health_monitor)
        return self.client.put(self.health_monitor_url(id),
                               media_type.HEALTH_MONITOR, health_monitor)

    def create_pool_health_monitor(self, health_monitor, pool_id):
        LOG.info("create_pool_health_monitor %r", health_monitor)
        return self.client.post(self.pool_health_monitors_url(pool_id),
                                media_type.HEALTH_MONITOR_POOL,
                                body=health_monitor)

    def delete_pool_health_monitor(self, health_monitor_id, pool_id):
        LOG.info("delete_pool_health_monitor %r", id)
        return self.client.delete(self.pool_health_monitor_url(
            pool_id, health_monitor_id))


class Firewall(object):

    def firewall_url(self, id):
        return self._get_neutron()["firewall_template"].replace("{id}", id)

    def firewalls_url(self):
        return self._get_neutron()["firewalls"]

    def fw_rule_url(self, id):
        return self._get_neutron()["fw_rule_template"].replace("{id}", id)

    def fw_rules_url(self):
        return self._get_neutron()["fw_rules"]

    def fw_policy_url(self, id):
        return self._get_neutron()["fw_policy_template"].replace("{id}", id)

    def fw_policies_url(self):
        return self._get_neutron()["fw_policies"]

    def fw_insert_rule_url(self, firewall_policy_id):
        return self._get_neutron()["fw_insert_rule_template"].replace(
            "{firewall_policy_id}", firewall_policy_id)

    def fw_remove_rule_url(self, firewall_policy_id):
        return self._get_neutron()["fw_remove_rule_template"].replace(
            "{firewall_policy_id}", firewall_policy_id)

    def create_firewall(self, firewall):
        LOG.info("create_firewall %r", firewall)
        return self.client.post(self.firewalls_url(), media_type.FIREWALL,
                                body=firewall)

    def delete_firewall(self, id):
        LOG.info("delete_firewall %r", id)
        self.client.delete(self.firewall_url(id))

    def get_firewall(self, id):
        LOG.info("get_firewall %r", id)
        return self.client.get(self.firewall_url(id), media_type.FIREWALL)

    def get_firewalls(self):
        LOG.info("get_firewalls")
        return self.client.get(self.firewalls_url(), media_type.FIREWALLS)

    def update_firewall(self, id, firewall):
        LOG.info("update_firewall %r", firewall)
        return self.client.put(self.firewall_url(id), media_type.FIREWALL,
                               firewall)

    def create_firewall_policy(self, firewall_policy):
        LOG.info("create_firewall_policy %r", firewall_policy)
        return self.client.post(self.firewall_policys_url(),
                                media_type.FIREWALL_POLICY,
                                body=firewall_policy)

    def delete_firewall_policy(self, id):
        LOG.info("delete_firewall_policy %r", id)
        self.client.delete(self.firewall_policy_url(id))

    def get_firewall_policy(self, id):
        LOG.info("get_firewall_policy %r", id)
        return self.client.get(self.firewall_policy_url(id),
                               media_type.FIREWALL_POLICY)

    def get_firewall_policies(self):
        LOG.info("get_firewall_policies")
        return self.client.get(self.firewall_policies_url(),
                               media_type.FIREWALL_POLICIES)

    def update_firewall_policy(self, id, firewall_policy):
        LOG.info("update_firewall_policy %r", firewall_policy)
        return self.client.put(self.firewall_policy_url(id),
                               media_type.FIREWALL_POLICY,
                               firewall_policy)

    def create_firewall_rule(self, firewall_rule):
        LOG.info("create_firewall_rule %r", firewall_rule)
        return self.client.post(self.firewall_rules_url(),
                                media_type.FIREWALL_RULE,
                                body=firewall_rule)

    def delete_firewall_rule(self, id):
        LOG.info("delete_firewall_rule %r", id)
        self.client.delete(self.firewall_rule_url(id))

    def get_firewall_rule(self, id):
        LOG.info("get_firewall_rule %r", id)
        return self.client.get(self.firewall_rule_url(id),
                               media_type.FIREWALL_RULE)

    def get_firewall_policies(self):
        LOG.info("get_firewall_rules")
        return self.client.get(self.firewall_policies_url(),
                               media_type.FIREWALL_RULES)

    def update_firewall_rule(self, id, firewall_rule):
        LOG.info("update_firewall_rule %r", firewall_rule)
        return self.client.put(self.firewall_rule_url(id),
                               media_type.FIREWALL_RULE,
                               firewall_rule)

    def insert_rule(self, firewall_policy_id, rule_info):
        LOG.info("insert_rule %r", rule_info)
        return self.client.put(self.fw_insert_rule_url(firewall_policy_id),
                               media_type.FW_INSERT_RULE,
                               body=rule_info)

    def remove_rule(self, firewall_policy_id, rule_info):
        LOG.info("remove_rule %r", rule_info)
        return self.client.put(self.fw_remove_rule_url(firewall_policy_id),
                               media_type.FW_REMOVE_RULE,
                               body=rule_info)


class MidonetClient(UrlProvider, L3, SecurityGroup, Loadbalancer, Firewall):

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri
        self.client = HttpClient(base_uri, username, password,
                                 project_id=project_id)
        super(MidonetClient, self).__init__()

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

    def create_network(self, network):
        LOG.info("create_network %r", network)
        return self.client.post(self.networks_url(), media_type.NETWORK,
                                body=network)

    def create_network_bulk(self, networks):
        LOG.info("create_network_bulk entered")
        return self.client.post(self.networks_url(), media_type.NETWORKS,
                                body=networks)

    def delete_network(self, id):
        LOG.info("delete_network %r", id)
        self.client.delete(self.network_url(id))

    def get_network(self, id, fields=None):
        LOG.info("get_network %r", id)
        return self.client.get(self.network_url(id), media_type.NETWORK)

    def get_networks(self, filters=None, fields=None,
                     sorts=None, limit=None, marker=None,
                     page_reverse=False):
        LOG.info("get_networks")
        return self.client.get(self.networks_url(), media_type.NETWORKS)

    def update_network(self, id, network):
        LOG.info("update_network %r", network)
        return self.client.put(self.network_url(id), media_type.NETWORK,
                               network)

    def create_subnet(self, subnet):
        LOG.info("create_subnet %r", subnet)
        return self.client.post(self.subnets_url(), media_type.SUBNET,
                                body=subnet)

    def create_subnet_bulk(self, subnets):
        LOG.info("create_subnet_bulk entered")
        return self.client.post(self.subnets_url(), media_type.SUBNETS,
                                body=subnets)

    def delete_subnet(self, id):
        LOG.info("delete_subnet %r", id)
        self.client.delete(self.subnet_url(id))

    def get_subnet(self, id):
        LOG.info("get_subnet %r", id)
        return self.client.get(self.subnet_url(id), media_type.SUBNET)

    def get_subnets(self):
        LOG.info("get_subnets")
        return self.client.get(self.subnets_url(), media_type.SUBNETS)

    def update_subnet(self, id, subnet):
        LOG.info("update_subnet %r", subnet)
        return self.client.put(self.subnet_url(id), media_type.SUBNET, subnet)

    def create_port(self, port):
        LOG.info("create_port %r", port)
        return self.client.post(self.ports_url(), media_type.PORT, body=port)

    def create_port_bulk(self, ports):
        LOG.info("create_port_bulk entered")
        return self.client.post(self.ports_url(), media_type.PORTS, body=ports)

    def delete_port(self, id):
        LOG.info("delete_port %r", id)
        self.client.delete(self.port_url(id))

    def get_port(self, id):
        LOG.info("get_port %r", id)
        return self.client.get(self.port_url(id), media_type.PORT)

    def get_ports(self):
        LOG.info("get_ports")
        return self.client.get(self.ports_url(), media_type.PORTS)

    def update_port(self, id, port):
        LOG.info("update_port %r", port)
        return self.client.put(self.port_url(id), media_type.PORT, port)
