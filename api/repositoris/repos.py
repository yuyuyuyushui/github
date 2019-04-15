from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Repos, self).__init__(api_url_path, **kwargs)

    def get_list(self):
        return self.get("/user/repos")

