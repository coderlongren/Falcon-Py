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
                               "title" : "热水器警报",
                               "description" : "",
                               "url" : "URL",
                               "picurl" : "",
                               "btntxt":"点击查看更多信息"
                           }
                        ]
                   }
           }
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg

