from core.rest_client import RestClient
class Repos(RestClient):
    def __init__(self,api_url_path,**kwargs):
        super(RestClient,self).__init__(self,api_url_path,**kwargs)

s = Repos()
