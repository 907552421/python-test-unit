#!/usr/bin/env python
#coding=utf-8

import logging
import logging.handlers

class Test(object):

    def __init__(self):
        self.log_file = 'test-class-log'
        handler = logging.handlers.RotatingFileHandler(self.log_file,maxBytes = 1024*1024,backupCount =5)

        fmt = '[%(message)s] - [%(asctime)s] - [%(filename)s:%(lineno)s] - [%(name)s]'

        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        logger = logging.getLogger('test')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        self.logger = logger

    def test(self):
        self.logger.info('test class log')


if __name__ == '__main__':
    t = Test()
    t.test()

