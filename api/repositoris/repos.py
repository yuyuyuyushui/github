from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_url_path, **kwargs):
        super(Repos, self).__init__(api_url_path, **kwargs)

    def list_your_repositories(self,**kwargs):
        """
        请求登录用户的库
        :param kwargs:
        :return:
        """
        return self.get("/user/repos", **kwargs)

    def list_user_repositories(self, username, **kwargs):
        """
        请求其他用户的库
        :param username: 用户名
        :param kwargs: 传入get的param参数
        :return:
        """
        return self.get("/users/{}/repos".format(username),**kwargs)

    def list_organization_repositories(self, org, **kwargs):
        """
        列出指定组织的库
        :param org:
        :param kwargs:
        :return:
        """
        return self.get("/orgs/{}/repos".format(org), **kwargs)

    def list_all_public_repositories(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-your-repositories
        :param kwargs:
        :return:
        """
        return self.get("/repositories",**kwargs)

    def crete_repositories(self, **kwargs):
        """
        创建已验证用户的库
        :param kwargs:
        :return:
        """
        return self.post('/user/repos', **kwargs)

    def crete_organization_repositories(self, org, **kwargs):
        """
        创建组织的库
        :param org:
        :param kwargs:
        :return:
        """
        return self.post('/orgs/{}/repos'.format(org), **kwargs)

    def Get(self, org, repo, **kwargs):
        """
        获取库
        :param org:
        :param repo:
        :param kwargs:
        :return:
        """
        return self.get('/repos/{}/{}'.format(org, repo), **kwargs)

    def edict(self, owner, repo, **kwargs):

        return self.patch('/repos/{}/{}'.format(owner, repo), **kwargs)