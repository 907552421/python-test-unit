#!/usr/bin/env python
#coding=utf-8

from HTMLParser import HTMLParser
import datetime
import os
import logging
import logging.handlers


class HTMLParserLinksHandler(HTMLParser):
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

class PageAnalyzer(object):
    def __init__(self,p_htmlParserLinksHandler,path):
        self.htmlParserLinksHandler = p_htmlParserLinksHandler;
        now = datetime.datetime.now()
        sdate = now.strftime('%Y-%m-%d')
        log_path=os.path.join(path,sdate)
        self.log_file=log_path
        handler = logging.handlers.RotatingFileHandler(self.log_file,maxBytes = 1024*1024,backupCount =5)

        fmt = '[%(message)s] - [%(asctime)s] - [%(filename)s:%(lineno)s] - [%(name)s]'

        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        logger = logging.getLogger('pageAnalyzer')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        self.logger = logger

    def getLinks(self,document_data,url):
        try:
            self.htmlParserLinksHandler.feed(document_data)
            self.htmlParserLinksHandler.close()
            return self.htmlParserLinksHandler.links
        except StandardError , e:
            self.logger.error('[Faild] [%s] [%s]'% (url,e))
        finally:
            self.htmlParserLinksHandler.close()

