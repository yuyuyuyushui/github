import requests

class RestClient():
    def __init__(self,api_url_path):
        self.api_url_path = api_url_path
        self.session = requests.session()

    def request(self,url, methd, data=None,json=None,**kwargs):
        methds = ['post','get','option', 'head']
        url = self.api_url_path + url
        # if methd=='post':
        #     return  self.session.post(url,data,json,**kwargs)
        # if methd=='get':
        #     return self.session.get(url, **kwargs)
        if methd in  methds:
            return self.session.request(methd, url, **kwargs)

    def get(self, url, **kwargs):
        return self.session.request(url, 'get', **kwargs)

    def post(self, url, **kwargs):
        return self.session.request('post', url, **kwargs)

r=RestClient('https://github.com/').get('')
print(r.text)