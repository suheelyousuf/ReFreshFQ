#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

def isCompressed(filename):
    if filename.endswith('.gz'):
        return True
    else:
        return False

#filename="t1.fastq"
#print(isCompressed(filename))