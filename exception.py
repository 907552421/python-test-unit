#!/usr/bin/env python
#coding=utf-8

try:
    b = 10/0
#except BaseException , e:
except StandardError , e:
    print e
