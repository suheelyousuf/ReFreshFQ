#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani
from Bio import SeqIO
#from savefiledialog import file_save
import gzip
from CheckIsCompressed import isCompressed
def search(filename,sequence):
    filesearch=""
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                if(sequence in read.seq):
                   filesearch=str(filesearch+read.id+"\n"+read.seq+"\n")
        return filesearch
              
    else:
        with open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                if sequence in read.seq:
                    filesearch=str(filesearch+read.id+"\n"+read.seq+"\n")
        return filesearch
  
    

#a=search("t1.fastq.gz","CCGC")
#print(a)
#print(type(a))
#file_save(a)