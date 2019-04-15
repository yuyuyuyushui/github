from core import rest_client
from api.repositoris.repos import Repos
class Github():
    def __init__(self, **kwargs):
        self.path = 'http://api.github.com'
        self.repo = Repos(self.path, **kwargs)


if __name__=="__main__":
    x = Github(token='d7eada18baee4ae9f04118d04b72f1de4bdd2cfd').repo.get_list()
    print(x,x.text)