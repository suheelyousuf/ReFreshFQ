#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

from CheckIsCompressed import isCompressed
from Bio import SeqIO

import gzip


def isFastq(filename):
    #status=True 
    if isCompressed(filename):
        try:
            with gzip.open(filename, "rt") as handle:
                read=SeqIO.parse(handle,"fastq")
                return any(read)
        except:
            return False
                
    else:
        try:
            with open(filename, "rt") as handle:
                read=SeqIO.parse(handle,"fastq")
                return any(read)
        except:
            return False

print(isFastq("test.fastq"))