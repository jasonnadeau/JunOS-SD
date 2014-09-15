__author__ = 'Jason Nadeau'


class AddressBookObject(object):
    import xml.etree.ElementTree as ET
    xmltemplates =
    '''
    <address>
    <name></name>
    <address-type></address-type>
    <host-name></host-name>
    <edit-version />
    <members />
    <address-version></address-version>
    <definition-type></definition-type>
    <description></description>
    </address>
    '''

    def __init__(self):

        self.xmlBody = ET.fromstring(AddressBookObject.xmltemplates)

class IPAddress(AddressBookObject):
    ADDRESS_TYPE="IPADDRESS"
    AADDRESS_VERSION=None
    def __init__(self):
        super(self,IPAddress).__init__()
        addressTypeElement = self.xmlBody.find('address-type')
        addressTypeElement.text = self.ADDRESS_TYPE
        addressVersionElement = self.xmlBody.find('address-version')
        addressVersionElement.text = self.ADDRESS_VERSION
    def render(self):
        return ET.tostring(self.xmlBody)

class IPv4Address(IPAddress):
    ADDRESS_VERSION="IPV4"
    def __init__(self,name,ipaddress,description,**kwargs):
        super(self,IPv4Address).__init__()


        nameElement = self.xmlBody.find('name')
        nameElement.text = name
        ipaddressElement = self.xmlBody.find('ip-address')
        ipaddressElement.text = ipaddress
        descriptionElement = self.xmlBody.find('description')
        descriptionElement.text = description





class IPv6Address(IPAddress):
    ADDRESS_VERSION="IPV6"
    pass
