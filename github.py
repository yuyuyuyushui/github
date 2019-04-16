from core import rest_client
from api.repositoris.repos import Repos
class Github():
    def __init__(self, **kwargs):
        self.path = 'http://api.github.com'
        self.repo = Repos(self.path, **kwargs)
        # self.user = "yuyuyuyushui"
        # self.owner = 'yuyuyuyushui'


if __name__=="__main__":
    data = {
        "name": "test",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
}
    x = Github(token='51e8340c7fd9b47d02bb26cb7d44698de0f658f5').repo
    # y = x.crete_response(json=data)
    # print(y.status_code)
    # print(x.get_list())
    z = x.crete_owner_respose(org='yuyuyuyushui11', json=data)
    print(z.status_code)
    t = x.get_owner_respose('yuyuyuyushui', 'github')
    print(t.url)