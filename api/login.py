from core.rest_client import RestClient
class Login(RestClient):
    def __init__(self,api_url_path,loginname=None,password=None,token=None,**kwargs):
        super(RestClient,self).__init__(api_url_path,**kwargs)
        if token is None:
            if loginname and password:
                self.session.auth(loginname, password)
        if loginname is None and password is None:
            if token == True:
                self.session.headers["Authorization"] = "token {}".format(token)
        else:
            print('输入有误')