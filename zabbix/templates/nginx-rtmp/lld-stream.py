#!/usr/bin/python
# -*- coding: utf-8 -*-
# date 2016/11/10 author pdd

'''
    http://127.0.0.1:2881/control/get/all_streams
'''

import os
import json
import urllib2

def Live(url):

    try:
        r = urllib2.urlopen(url, timeout=1)
    except urllib2.URLError, e:
        exit(1)  # 异常退出
    else:
        stream = json.loads(r.read())
        channels = stream["servers"][0]["applications"][0]["pushes"]  # 选择推流模式数据
        data = [{"{#CHANNELNAME}": channel["name"]} for channel in channels]
        print(json.dumps({"data": data}, indent=4))

if __name__ == "__main__":
    url = "http://192.168.0.55:2881/control/get/all_streams"  # 直播频道流状态值url
    status = Live(url)
