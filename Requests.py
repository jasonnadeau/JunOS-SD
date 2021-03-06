__author__ = 'Jason Nadeau'

class Request(object):
    def __init__(self,uri,session):
        isinstance(session,Session.JunosSession)
        self.requestObj = session.buildRequest(uri=uri)


class IPAddressRequest(Request):


class IPv4AddressRequest(IPAddressRequest):
    VERSION="IPV4"
    def addAddressObject(self,name,ipAddress,description=None):

class IPv6AddressRequest(IPAddressRequest):
    pass

