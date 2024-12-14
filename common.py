import requests


class Common(object):
    def __init__(self, url_root):
        self.url_root = url_root

    def get(self, uri, params=''):
        if params:
            url = self.url_root + uri + '?' + params
        else:
            url = self.url_root + uri
        res = requests.get(url)
        return res

    def post(self, uri, params=''):
        url = self.url_root + uri
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Connection': 'Keep-Alive',
                   'xmjzsign': 'test',
                   'Content-Encoding':'gzip',
                   'xmjzchannel':'xiongmaoxitong',
                   'User_Agent':'okhttp/4.9.0'
        }
        if len(params) > 0:
            res = requests.post(url, data=params, headers=headers)
        else:
            res = requests.post(url, headers=headers)
        return res