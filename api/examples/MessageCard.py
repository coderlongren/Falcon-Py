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
                               "title" : "中秋节礼品领取",
                               "description" : "今年中秋节公司有豪礼相送",
                               "url" : "URL",
                               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
                               "btntxt":"更多"
                           }
                        ]
                   }
           }
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg

