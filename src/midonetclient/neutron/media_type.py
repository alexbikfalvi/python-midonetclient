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
LB_VIP = "application/vnd.org.midonet.neutron.lb.Vip-v1+json"
LB_VIPS = "application/vnd.org.midonet.neutron.lb.Vips-v1+json"
LB_POOL = "application/vnd.org.midonet.neutron.lb.Pool-v1+json"
LB_POOLS = "application/vnd.org.midonet.neutron.lb.Pools-v1+json"
LB_MEMBER = "application/vnd.org.midonet.neutron.lb.Member-v1+json"
LB_MEMBERS = "application/vnd.org.midonet.neutron.lb.Members-v1+json"
LB_HEALTH_MONITOR = \
    "application/vnd.org.midonet.neutron.lb.HealthMonitor-v1+json"
LB_HEALTH_MONITORS = \
    "application/vnd.org.midonet.neutron.lb.HealthMonitors-v1+json"
LB_HEALTH_MONITOR_POOL = \
    "application/vnd.org.midonet.neutron.lb.HealthMonitorPool-v1+json"

# Firewall
FIREWALL = "application/vnd.org.midonet.neutron.Firewall-v1+json"
FIREWALLS = "application/vnd.org.midonet.neutron.Firewalls-v1+json"
FW_RULE = "application/vnd.org.midonet.neutron.fw.Rule-v1+json"
FW_RULES = "application/vnd.org.midonet.neutron.fw.Rules-v1+json"
FW_INSERT_RULE = \
    "application/vnd.org.midonet.neutron.fw.InsertRule-v1+json"
FW_REMOVE_RULE = \
    "application/vnd.org.midonet.neutron.fw.RemoveRule-v1+json"
FW_POLICY = "application/vnd.org.midonet.neutron.fw.Policy-v1+json"
FW_POLICIES = "application/vnd.org.midonet.neutron.fw.Policies-v1+json"

# VPN
VPN_SERVICE = "application/vnd.org.midonet.neutron.VpnService-v1+json"
VPN_SERVICES = "application/vnd.org.midonet.neutron.VpnServices-v1+json"
VPN_IKE_POLICY = "application/vnd.org.midonet.neutron.vpn.IkePolicy-v1+json"
VPN_IKE_POLICIES = \
    "application/vnd.org.midonet.neutron.vpn.IkePolicies-v1+json"
VPN_IPSEC_POLICY = \
    "application/vnd.org.midonet.neutron.vpn.IpsecPolicy-v1+json"
VPN_IPSEC_POLICIES = \
    "application/vnd.org.midonet.neutron.vpn.IpsecPolicies-v1+json"
VPN_IPSEC_SITE_CONNECTION = \
    "application/vnd.org.midonet.neutron.vpn.IpsecSiteConnection-v1+json"
VPN_IPSEC_SITE_CONNECTIONS = \
    "application/vnd.org.midonet.neutron.vpn.IpsecSiteConnections-v1+json"

# Metering
METERING_LABEL =\
    "application/vnd.org.midonet.neutron.metering.Label-v1+json"
METERING_LABELS = \
    "application/vnd.org.midonet.neutron.metering.Labels-v1+json"
METERING_LABEL_RULE = \
    "application/vnd.org.midonet.neutron.metering.LabelRule-v1+json"
METERING_LABEL_RULES = \
    "application/vnd.org.midonet.neutron.metering.LabelRules-v1+json"
