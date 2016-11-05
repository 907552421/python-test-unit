#!/usr/bin/env pythyon
#coding=utf-8

import urllib
import urllib2
import sys
import uuid
import datetime
import os
import logging
import logging.handlers

class Grabber(object):

    def __init__(self,path):
        now = datetime.datetime.now()
        sdate = now.strftime('%Y-%m-%d')
        log_path=os.path.join(path,sdate)
        self.log_file=log_path
        handler = logging.handlers.RotatingFileHandler(self.log_file,maxBytes = 1024*1024,backupCount =5)

        fmt = '[%(message)s] - [%(asctime)s] - [%(filename)s:%(lineno)s] - [%(name)s]'

        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        loggertemp = logging.getLogger('grabber')
        loggertemp.addHandler(handler)
        loggertemp.setLevel(logging.DEBUG)
        self.logger = loggertemp


    def grab(self,url):
        headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        try:
            request = urllib2.Request(url,headers = headers)
            result = urllib2.urlopen(request)
            result_data = result.read()
            filename = uuid.uuid1()
            #f = open('/root/practice/python_practice/python-test-unit/documents/%s' % filename,'w')
            f = open('/search/python_practice/python-test-unit/documents/%s' % filename,'w')
            f.write(url)
            f.write('\n')
            f.write(result_data)
            f.close()
            self.logger.info('[Success] [%s]'% url)
            return result_data
        except StandardError ,e:
            self.logger.error('[Failed] [%s] [%s]'% (url,e))
        finally:
            if 'f' is locals():
                f.close()


