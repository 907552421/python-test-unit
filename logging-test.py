#!/usr/bin/env python
#coding=utf-8

import logging
import logging.handlers

LOG_FILE='test.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE,maxBytes = 1024*1024,backupCount =5)

fmt = '[%(message)s] - [%(asctime)s] - [%(filename)s:%(lineno)s] - [%(name)s]'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('test')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

url='http://develop/test.html'

#logger.info('[sucess] [%s]',url)
logger.info('[sucess] [%s]' %url)
#logger.debug('first debug message')
