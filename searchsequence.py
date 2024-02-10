#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani
from Bio import SeqIO
#from savefiledialog import file_save
import gzip

def search(handle, target_sequence):
    print(target_sequence)
    print(type(handle))
    print(SeqIO)
    try:
            
        for record in SeqIO.parse(handle, "fastq"):
            print("hello")
            message="hello"
            if target_sequence in str(record.seq):
                message=message+"Sequence found in FASTQ record:"+"\n"
                message=message+f"Header: {record.id}"+"\n"
                message=message+f"Sequence: {record.seq}"+"\n"
                message=message+f"Quality scores: {record.letter_annotations['phred_quality']}"+"\n"
                print(message)
                return message
    except Exception as e:
        print("Error")
        return "No match"
                

        
 
    

#a=search("t1.fastq.gz","CCGC")
#print(a)
#print(type(a))
#file_save(a)