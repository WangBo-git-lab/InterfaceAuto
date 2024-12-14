import requests
from websocket import create_connection

class Common(object):
    def __init__(self, url_root, api_type):
        '''
        :param api_type:接口类似当前支持http，ws，http就是http协议，ws是Websocket协议
        :param url_root: 被测系统的跟路由
        '''
        if api_type == 'ws':
            self.ws = create_connection(url_root)
        elif api_type == 'http':
            self.ws = 'null'
            self.url_root = url_root

    def send(self, params):
        '''
        :param params: websocket接口的参数
        :return: 访问接口的返回值
        '''

        self.ws.send(params)
        res = self.ws.recv()
        return res

    def __del__(self):
        '''
        :return:
        '''
        if self.ws != 'null':
            self.ws.close()

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

    def put(self,uri,params=None):
        url = self.url_root + uri
        if params is not None:
            res = requests.put(url,data=params)
        else:
            res = requests.put(url)
        return res

    def delete(self,uri,params=None):
        url = self.url_root + uri
        if params is not None:
            res = requests.delete(url, data=params)
        else:
            res = requests.delete(url)
        return res
