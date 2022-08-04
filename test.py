#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

from Bio import SeqIO
records = list(SeqIO.parse("test.fastq", "fastq"))
#with open("test.fastq", "rt") as handle:
        #for read in SeqIO.parse(handle,"fastq"):
            #print(read.format("fastq"))
            #break
            
        
print(len(records))