#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

from CheckIsCompressed import isCompressed
from Bio import SeqIO
import gzip

def trim_quality(filename,limit):
    r_str=""
    
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
               if min(read.letter_annotations["phred_quality"]) >= limit:
                   r_str=r_str+str(read.id)+"\n"
                   r_str=r_str+str(read.seq)+"\n"
                   r_str=r_str+str(read.format("fastq").split("\n")[2])+"\n"
                   r_str=r_str+str(read.format("fastq").split("\n")[3])+"\n"
                
    else:
        with open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                if min(read.letter_annotations["phred_quality"]) >= limit:
                   r_str=r_str+str(read.id)+"\n"
                   r_str=r_str+str(read.seq)+"\n"
                   r_str=r_str+str(read.format("fastq").split("\n")[2])+"\n"
                   r_str=r_str+str(read.format("fastq").split("\n")[3])+"\n"
    return r_str

def ccc():
    return