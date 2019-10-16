from CheckIsCompressed import isCompressed
from Bio import SeqIO

import gzip

def trim_primer(read, primer):
    r_str=""
    if read.seq.startswith(primer):
        r_str=r_str+str(read.id)+"\n"
        r_str=r_str+str(read.seq[len(primer):])+"\n"
        r_str=r_str+str(read.format("fastq").split("\n")[2])+"\n"
        r_str=r_str+str(read.format("fastq").split("\n")[3])+"\n"
        return r_str
    else:
        return str(read.format("fastq"))

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

