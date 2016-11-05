#!/usr/bin/env python
#coding=utf-8

import Queue
import grabber
import pageAnalyzer
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider(object):
    def __init__(self):
        self.seedurls=['http://www.cnblogs.com/']
        self.logpath='/search/python_practice/python-test-unit/grab-log'
        #self.logpath='/root/practice/python_practice/python-test-unit/grab-log'
        self.urlQueue = Queue.Queue()
        for url in self.seedurls:
            self.urlQueue.put(url)


    def grab_from_seed(self,num):
        grabberInstance = grabber.Grabber(self.logpath)
        parser = pageAnalyzer.HTMLParserLinksHandler()
        pa =  pageAnalyzer.PageAnalyzer(parser,self.logpath)
        i = 0
        s = set([])
        pattern = re.compile(r'^http[s]?://')
        pattern_relative = re.compile(r'^/[^.]*$')
        pattern_remove_last = re.compile(r'/[^/]*$')
        #while (self.urlQueue.qsize() < 10 and  (not self.urlQueue.empty())):
        while ( i<num and  (not self.urlQueue.empty())):
            current_url = self.urlQueue.get()
            result_html = grabberInstance.grab(current_url)
            links =  pa.getLinks(result_html,current_url)
            #print(links)
            i+=1
            print('grab no %d html'% i)
            if (not links is None):
                for link in links:
                    if (not link in s):
                        match = pattern.search(link)
                        if match:
                            s.add(link)
                            print(link)
                            self.urlQueue.put(link)
                        else:
                            match_relative = pattern_relative.search(link)
                            if match_relative:
                                match_remove_last = pattern_remove_last.search(current_url)
                                if match_remove_last:
                                    try:
                                        print current_url
                                        print link
                                        new_url = '%s%s' %(current_url[:match_remove_last.start()],link)
                                        s.add(new_url)
                                        print new_url
                                        self.urlQueue.put(new_url)
                                    except StandardError , e:
                                        print current_url
                                        print e
