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


APP = "application/vnd.org.midonet.Application-v3+json"
NEUTRON = "application/vnd.org.midonet.neutron.Neutron-v1+json"
NETWORK = "application/vnd.org.midonet.neutron.Network-v1+json"
NETWORKS = "application/vnd.org.midonet.neutron.Networks-v1+json"
SUBNET = "application/vnd.org.midonet.neutron.Subnet-v1+json"
SUBNETS = "application/vnd.org.midonet.neutron.Subnets-v1+json"
PORT = "application/vnd.org.midonet.neutron.Port-v1+json"
PORTS = "application/vnd.org.midonet.neutron.Ports-v1+json"

# L3 Service
ROUTER = "application/vnd.org.midonet.neutron.Router-v1+json"
ROUTERS = "application/vnd.org.midonet.neutron.Routers-v1+json"
ROUTER_INTERFACE = \
    "application/vnd.org.midonet.neutron.RouterInterface-v1+json"
FLOATING_IP = "application/vnd.org.midonet.neutron.FloatingIp-v1+json"
FLOATING_IPS = "application/vnd.org.midonet.neutron.FloatingIps-v1+json"

# Security groups
SECURITY_GROUP = \
    "application/vnd.org.midonet.neutron.SecurityGroup-v1+json"
SECURITY_GROUPS = \
    "application/vnd.org.midonet.neutron.SecurityGroups-v1+json"
SECURITY_GROUP_RULE = \
    "application/vnd.org.midonet.neutron.SecurityGroupRule-v1+json"
SECURITY_GROUP_RULES = \
    "application/vnd.org.midonet.neutron.SecurityGroupRules-v1+json"

# Load balancer
VIP = "application/vnd.org.midonet.neutron.Vip-v1+json"
VIPS = "application/vnd.org.midonet.neutron.Vips-v1+json"
POOL = "application/vnd.org.midonet.neutron.Pool-v1+json"
POOLS = "application/vnd.org.midonet.neutron.Pools-v1+json"
MEMBER = "application/vnd.org.midonet.neutron.Member-v1+json"
MEMBERS = "application/vnd.org.midonet.neutron.Members-v1+json"
HEALTH_MONITOR = \
    "application/vnd.org.midonet.neutron.HealthMonitor-v1+json"
HEALTH_MONITORS = \
    "application/vnd.org.midonet.neutron.HealthMonitors-v1+json"
HEALTH_MONITOR_POOL = \
    "application/vnd.org.midonet.neutron.HealthMonitorPool-v1+json"

# Firewall
FIREWALL = "application/vnd.org.midonet.neutron.Firewall-v1+json"
FIREWALLS = "application/vnd.org.midonet.neutron.Firewalls-v1+json"
FW_RULE = "application/vnd.org.midonet.neutron.FirewallRule-v1+json"
FW_RULES = "application/vnd.org.midonet.neutron.FirewallRules-v1+json"
FW_INSERT_RULE = \
    "application/vnd.org.midonet.neutron.InsertFirewallRule-v1+json"
FW_REMOVE_RULE = \
    "application/vnd.org.midonet.neutron.RemoveFirewallRule-v1+json"
FW_POLICY = "application/vnd.org.midonet.neutron.FirewallPolicy-v1+json"
FW_POLICIES = "application/vnd.org.midonet.neutron.FirewallPolicies-v1+json"
