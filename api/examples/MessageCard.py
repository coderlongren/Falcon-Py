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
                   "msgtype" : "textcard",
                   "agentid" : 1,
                   "textcard" : {
                    "title" : "警告通知",
                    "description" : "<div class=\"gray\">2016年9月26日</div> <div class=\"normal\">机器坏了</div><div class=\"highlight\">请即使排查错误</div>",
                    "url" : "URL",
                    "btntxt":"更多"
           }
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg

