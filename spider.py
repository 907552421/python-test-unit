#!/usr/bin/env python
#coding=utf-8

import Queue
import grabber
import pageAnalyzer

class Spider(object):
    def __init__(self):
        self.seedurls=['http://www.cnblogs.com/']
        self.logpath='/root/practice/python_practice/python-test-unit/grab-log'
        self.urlQueue = Queue.Queue()
        for url in self.seedurls:
            self.urlQueue.put(url)


    def grab_from_seed(self):
        grabberInstance = grabber.Grabber(self.logpath)
        parser = pageAnalyzer.HTMLParserLinksHandler()
        pa =  pageAnalyzer.PageAnalyzer(parser,self.logpath)
        i = 0
        s = set([])
        #while (self.urlQueue.qsize() < 10 and  (not self.urlQueue.empty())):
        while (i<50 and  (not self.urlQueue.empty())):
            current_url = self.urlQueue.get()
            result_html = grabberInstance.grab(current_url)
            links =  pa.getLinks(result_html,current_url)
            #print(links)
            i+=1
            print('grab no %d html'% i)
            if (not links is None):
                for link in links:
                    if (not link in s):
                        s.add(link)
                        print link
                        self.urlQueue.put(link)
