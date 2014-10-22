__author__ = 'Jason Nadeau'

class JunOSObject(object):
    def __init__(self):
        import xml.etree.ElementTree as ET
        self.xmlBody = ET.fromstring(self.xmltemplate)

class AddressBookObject(JunOSObject):
    import xml.etree.ElementTree as ET
    xmltemplate ='''
    <address>
    <name></name>
    <address-type></address-type>
    <ip-address></ip-address>
    <host-name></host-name>
    <edit-version />
    <members />
    <address-version></address-version>
    <definition-type></definition-type>
    <description></description>
    </address>
    '''

    def __init__(self):

        super(AddressBookObject,self).__init__()




class IPAddress(AddressBookObject):
    ADDRESS_TYPE="IPADDRESS"

    def __init__(self):
        super(IPAddress, self).__init__()
        IpAddressDict={'address-type':self.ADDRESS_TYPE,
                       'address-version':self.ADDRESS_VERSION}
        self.installValues(IpAddressDict)
    def render(self):
        import xml.etree.ElementTree as ET
        return ET.tostring(self.xmlBody)

    def installValues(self,aDict):
        '''I expect a dictionary of keys that match XML node names,
        For each node name match I will install the value as the node text'''
        for each in aDict.keys():
            if each =='other':
                self.installValues(aDict.get('other'))
            else:
                tempElement = self.xmlBody.find(each)
                if tempElement is not None:
                    tempElement.text = aDict.get(each)
                else:
                    import xml.etree.ElementTree as ET
                    tempElement = ET.SubElement(self.xmlBody,each)
                    tempElement.text = aDict.get(each)


class IPv4Address(IPAddress):
    ADDRESS_VERSION="IPV4"
    def __init__(self,name,ipaddress,description,**kwargs):
        super(IPv4Address, self).__init__()
        #kwargs['address-version']=self.ADDRESS_VERSION
        initVarDict = {'name':name,
                       'ip-address':ipaddress,
                       'description':description,
                       'other':kwargs}
        self.installValues(initVarDict)







class IPv6Address(IPAddress):
    ADDRESS_VERSION="IPV6"
    def __init__(self,name,ipaddress,description,**kwargs):
        super(IPv6Address, self).__init__()

        initVarDict = {'name':name,
                       'ip-address':ipaddress,
                       'description':description,
                       'other':kwargs}
        self.installValues(initVarDict)



s=IPv4Address('test-item','10.2.2.2','test-description')
