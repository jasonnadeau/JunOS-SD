__author__ = 'Jason Nadeau'

class JunosSession(object):
    
    def __init__(self, server, user):
        """

        :type self: object
        """
        self.User = user
        self.Server = server

    def buildRequest(self,uri=None):
        import urllib2
        if uri==None:
            uri=self.Server.URL
        request = urllib2.Request(uri)
        request.add_header('Authorization',self.buildAuthentication())
        return request

    def buildAuthentication(self):
        import base64
        encodedCreds = base64.encodestring('%s:%s'
                                           %(self.User.getUsername(),self.User.getPassword())
                                           )
        encodedCreds = encodedCreds.replace('\n','')
        headerStr = 'Basic {}'
        return headerStr.format(encodedCreds)
        

    
