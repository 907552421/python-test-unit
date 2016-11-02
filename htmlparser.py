#!/usr/bin/env pyton
#coding:utf-8

from HTMLParser import HTMLParser
import urllib2
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links=[]

    def handle_starttag(self,tag,attrs):
        if tag == "a":
            if len(attrs) == 0:pass
            else:
                for(variable,value) in attrs:
                    if variable == "href":
                        self.links.append(value)

if __name__=="__main__":
    headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    url=sys.argv[1]
    req = urllib2.Request(url,headers = headers)
    #print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    hp = MyHTMLParser()
    hp.feed(res)
    hp.close()
    print(len(hp.links))
    print(hp.links)

