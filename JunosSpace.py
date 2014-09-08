__author__ = 'Jason Nadeau'


class JunosSpace(object):
    URI = '/api'
    def __init__(self, hostname):


            self.__setHostname(hostname)
            print(self.URL)

    def __setHostname(self, hostname):
        '''This will set the hostname for the JunosSD object it will run __setURLPath to update URL to reflect new
        hostname'''
        self.hostname = hostname
        self.__setURLPath()

    def __setURLPath(self):
        '''This method will create the proper API URI stem for Junos Space or Space application if used by subclass'''
        urlPathStr = '''https://{hostname}{URI}'''
        urlDict = {'hostname': self.hostname,
                   'URI': self.URI}
        self.URL = urlPathStr.format(**urlDict)

    
class JunosSD(JunosSpace):
    URI = JunosSpace.URI + '/juniper/sd'
    def __init__(self,hostname):
        super(JunosSD, self).__init__(hostname)





