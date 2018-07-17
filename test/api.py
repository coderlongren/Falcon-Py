import random
import requests
import sys
import os
import re
import  json
class abstractApi(object):
    def __init__(self):
        return

    def getAcc(self):
        raise NotImplementedError


class API(abstractApi):
    def getAcc(self):
        return "ssss"
    def appendArgs(self, url, args):
        if args is None:
            return url
        for key, value in args.items():
            if '?' in url:
                url += ('&' + key + "=" + value)
            else:
                url += ("?" + key + "=" + value)

        return url
main = API()

url = "/cgi-bin/message/send?access_token=ACCESS_TOKEN"
args = {
                "touser": "@all",
                "agentid": '1000002',
                'msgtype' : 'text',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'text' : {
                    'content':'哈哈',
                },
                'safe' : '0',
        }
data = json.dumps(args).decode('unicode-escape').encode("utf-8")

# print(main.appendArgs(url, args))