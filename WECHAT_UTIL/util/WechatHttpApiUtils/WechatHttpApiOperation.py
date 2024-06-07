import requests
import json


class WECHAT_HTTP_API_OP:
    @staticmethod
    def post_wechat_http_api(api,port,data=None):
        if data is None:
            data={}
        url = "http://127.0.0.1:{}/api/?type={}".format(port,api)
        resp = requests.post(url = url,data = json.dumps(data))
        return resp.json()

    @staticmethod
    def get_wechat_http_api(api,port,data=None):
        if data is None:
            data={}
        url = "http://127.0.0.1:{}/api/?type={}".format(port,api)
        resp = requests.get(url = url,params = data)
        return resp.json()