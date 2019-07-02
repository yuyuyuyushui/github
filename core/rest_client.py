import requests


class RestClient():
    def __init__(self, api_url_path, username=None,password=None,token=None,**kwargs):
        self.session = requests.session()

        if token is None:
            if username and password:
                self.session.auth(username, password)
        if username is None and password is None:
            if token:
                s =self.session.headers["Authorization"] = "token {}".format(token)
                print(s)
        else:
                print('输入有误')
        self.api_url_path = api_url_path

    def get(self, url, **kwargs):
        url = self.api_url_path + url
        return self.session.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        url = self.api_url_path + url
        return self.session.request('post', url, **kwargs)

    def patch(self,url,**kwargs):
        url = self.api_url_path +url
        return self.session.request('patch', url, **kwargs)

