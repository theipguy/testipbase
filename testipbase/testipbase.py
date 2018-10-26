"""Call the http//ipbase.co API from Python."""
import requests, json

class testipbase:
    base_url = 'http://ipbase.co/{ip}'
    #def __init__(self, apikey=None,language='en'):
    def __init__(self, apikey=None,language='en'):
        self.apikey = apikey
        self.language = language
        self.headers = {'user-agent': 'ipdata-pypi/2.4'}
    def lookup(self, ip):
        if self.apikey:
            self.headers ['api-key'] = self.apikey
#        r = requests.get(self.base_url.format(ip=ip, language=self.language), headers=self.headers)
        r = requests.get(self.base_url.format(ip=ip), headers=self.headers)
        if r.status_code==200:
            return {'status':r.status_code, 'response':r.json()}
        return {'status':r.status_code, 'response':r.text}
