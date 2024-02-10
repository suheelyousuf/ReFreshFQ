#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

from CheckIsCompressed import isCompressed
from Bio import SeqIO
import shutil
import os
from tkinter import filedialog


import gzip

def cut_primer(handle, primer):
    count=0
    handle1=open("copy.fastq","w")
    for record in SeqIO.parse(handle, "fastq"):
        sequence = str(record.seq)
        if sequence.startswith(primer):
            rec=""
            
            trimmed_sequence = sequence[len(primer):]
            rec=str(record.id)+trimmed_sequence+"\n"+"+"+"\n"+record.letter_annotations['phred_quality']+"\n"
            
            record.seq = trimmed_sequence
            
            SeqIO.write(rec, handle1, "fastq")
            count += 1
        else:
            SeqIO.write(record,handle1,"fastq")
    f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
    
    shutil.copyfileobj(handle1,f)
            
                
    os.remove("copy.fastq")
    f.close()

    '''

def trimoffprimer(filename,primersequence):
    trim_str=""
    
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                trim_str=trim_str+str(trim_primer(read,primersequence))
    #return trim_str
                
    else:
        with open(filename, "rt") as handle:
            for read in SeqIO.parse(handle,"fastq"):
                trim_str=trim_str+str(trim_primer(read,primersequence))
    return trim_str
    
#print(trimoffprimer("t1.fastq.gz","AC"))

'''