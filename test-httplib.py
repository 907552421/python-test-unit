#!/usr/bin/env python

import httplib

httpClient = None
try:
    httpClient = httplib.HTTPConnection('www.jb51.net',80,timeout=30)
    httpClient.request('GET','http://www.jb51.net/article/66763.htm')

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
