# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Route(ResourceBase):

    def create(self, router_uuid, type, srcNetworkAddr, srcNetworkLength,
                        dstNetworkAddr, dstNetworkLength, weight,
                        nextHopPort=None, nextHopGateway=None ):

        uri =  self.cl.midonet_uri + 'routers/%s/routes' % router_uuid
        data ={ "type": type,
                "srcNetworkAddr": srcNetworkAddr,
                "srcNetworkLength": srcNetworkLength, #int
                "dstNetworkAddr": dstNetworkAddr,
                "dstNetworkLength": dstNetworkLength, #int
                "weight": weight } #int

        if type == 'Normal':
            data["nextHopPort"] = nextHopPort
        if nextHopGateway:
            data["nextHopGateway"] = nextHopGateway

        return self.cl.post(uri, data)


    def list(self, router_uuid):
        uri = self.cl.midonet_uri + 'routers/%s/routes' % router_uuid
        return self.cl.get(uri)

