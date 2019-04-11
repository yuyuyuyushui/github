from core import rest_client
from api.repositoris.repos import Repos
class Github():
    def __init__(self,**kwargs):
        self.path = 'http://api.github.com'
        self.repo = Repos(self.path,**kwargs)
Github(name='luo',password='123')