from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Repos, self).__init__(api_url_path, **kwargs)

    def get_list(self):
        return self.get("/user/repos")

    def crete_response(self, **kwargs):
        return self.post('/user/repos', **kwargs)

    def crete_owner_respose(self, org, **kwargs):
        return self.post('/orgs/{}/repos'.format(org), **kwargs)

    def get_owner_respose(self, owner,  repo, **kwargs):
        return self.get('/repos/{}/{}'.format(owner, repo), **kwargs)

    def edict(self, owner, repo, **kwargs):
        return self.patch('/repos/{}/{}'.format(owner, repo), **kwargs)