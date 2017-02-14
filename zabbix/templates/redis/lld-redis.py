#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'pdd'
__date__ = '2016/11/28'

''' redis db low level discovery '''

import re
import json
import redis

def discovery(host, port, password):
    client = redis.StrictRedis(host=host, port=port, password=password)
    server_info = client.info()
    dbs = [('db%d' % x) for x in range(0,16) if ('db%d' % x) in server_info]  # redis默认15个db
    data = [{"{#DBNAME}": db} for db in dbs]
    print(json.dumps({"data": data}, indent=4))

if __name__=='__main__':
    host = '192.168.0.49'
    port = 6379
    password = 'hogesoft'
    discovery(host, port, password)
