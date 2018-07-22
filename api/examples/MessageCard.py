#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
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
    time1 = datetime.datetime.now()
    time = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
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
                               "title" : "热水器警报" +":" +  time,
                               "description" : "",
                               "url" : "http://water.megatech.xyz",
                               "btntxt":"点击查看更多信息"
                           }
                        ]
                   }
           }
            )
    print response
except ApiException as e :
    print e.errCode, e.errMsg

