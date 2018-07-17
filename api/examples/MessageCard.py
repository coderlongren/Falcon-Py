#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../src/")

import random

from CorpApi import *
from TestConf import * 

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try :
##
    href = ""
    response = api.httpCall(
            CORP_API_TYPE['MESSAGE_SEND'],
            {
                   "touser" : "@all",
                   "toparty" : "",
                   "totag" : "",
                   "msgtype" : "news",
                   "agentid" : 1000002,
                   "news" : {
                       "articles" : [
                           {
                               "title" : "大大的警告",
                               "description" : "赶紧维修",
                               "url" : "URL",
                               "picurl" : "http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E8%AD%A6%E5%91%8A%20%E5%9B%BE%E7%89%87&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2107656704,2995307201&os=4194235631,2235798714&simid=3531675448,452590362&pn=0&rn=1&di=54149405200&ln=1933&fr=&fmq=1531841772131_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&hs=2&objurl=http%3A%2F%2Fpic.58pic.com%2F58pic%2F15%2F62%2F00%2F19B58PICXF5_1024.png&rpstart=0&rpnum=0&adpicid=0",
                               "btntxt":"更多"
                           }
                        ]
                   }
           }
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg

