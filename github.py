from core import rest_client
from api.repositoris.repos import Repos
class Github():
    def __init__(self, **kwargs):
        self.path = 'http://api.github.com'
        self.repo = Repos(self.path, **kwargs)
        # self.user = "yuyuyuyushui"
        # self.owner = 'yuyuyuyushui'


if __name__=="__main__":
    import json
    data = {
        "name": "test2",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
}
    x = Github(token='04c6afc4e571e34730940c386861dc71ced2889b').repo
    # y = x.crete_response(json=data)
    # print(y.status_code)
    # print(x.get_list())
    # z = x.crete_organization_repositories(org='yuyuyuyushui11', json=data)
    # print(z.status_code)
    # t = x.Get('yuyuyuyushui', 'github')
    # print(t.url)
    paragram = {
        "visibility":"all"

    }
    # respose = x.list_organization_repositories('yuyuyuyushuiorg')
    # print(respose.text)
    # respose2 = x.list_all_public_repositories()
    # print(respose2.text)
    respose3 = x.Get('zhangting85','Hello-World')
    print(respose3.text)
    for i in json.loads(respose3.text):
       print(i['name'])