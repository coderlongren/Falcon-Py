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
    response = api.httpCall(
            CORP_API_TYPE['MESSAGE_SEND'],
            {
                "touser": "任赛龙",
                "agentid": 1000002,
                'msgtype' : 'text',
                'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'text' : {
                    'content':'哈哈',
                },
                'safe' : 0,
            })
    print response
except ApiException as e :
    print e.errCode, e.errMsg

