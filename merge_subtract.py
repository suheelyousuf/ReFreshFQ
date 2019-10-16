from Bio import SeqIO
import itertools
import sys
import os
import gzip
from CheckIsCompressed import isCompressed

def merge_fastq(fastq_path1, fastq_path2):
    combine_str=""
    if isCompressed(fastq_path1):
        with gzip.open(fastq_path1, "rt") as handle1:
            for read in SeqIO.parse(handle1,"fastq"):
                combine_str=combine_str+str(read.format("fastq"))
            if isCompressed(fastq_path2):
                with gzip.open(fastq_path1, "rt") as handle2:
                    for read in SeqIO.parse(handle2,"fastq"):
                        combine_str=combine_str+str(read.format("fastq"))
            else:
                with open(fastq_path2,"rt") as handle2:
                    for read in SeqIO.parse(handle2,"fastq"):
                        combine_str=combine_str+str(read.format("fastq"))

                                  
                
    else:
        with open(fastq_path1, "rt") as handle1:
            for read in SeqIO.parse(handle1,"fastq"):
                combine_str=combine_str+str(read.format("fastq"))
                
            if isCompressed(fastq_path2):
                with gzip.open(fastq_path2, "rt") as handle2:
                    for read in SeqIO.parse(handle2,"fastq"):
                        combine_str=combine_str+str(read.format("fastq"))
            else:
                with open(fastq_path2,"rt") as handle2:
                    for read in SeqIO.parse(handle2,"fastq"):
                        combine_str=combine_str+str(read.format("fastq"))

                     
    return combine_str

def subtract_fastq(fastq_path1,fastq_path2):
    results = ""
    seen = set()
    subtract_str=""
    for s in SeqIO.parse(fastq_path1,"fastq"):
        seen.add(str(s.seq))

    for s in SeqIO.parse(fastq_path2,"fastq"):
        if str(s.seq) not in seen:
            results=results+s.format("fastq")
    
    subtract_str=str(results)
    #print(subtract_str)

    #output_handle = open("DIFF.fastq","w")
    #SeqIO.write(results,output_handle,"fastq")
    #output_handle.close()
    return subtract_str


#print(subtract_fastq("test.fastq","trimmed.fastq"))