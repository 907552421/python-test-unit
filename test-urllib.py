#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import sys


#由于没有head，某些服务器只能看到请求，得不到client agent信息，会禁止该请求403（比如为了防止爬虫爬取内容)
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
url=sys.argv[1]
req = urllib2.Request(url,headers = headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res