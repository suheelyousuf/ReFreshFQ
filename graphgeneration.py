#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani


from Bio import SeqIO
from Bio.SeqUtils import GC
from matplotlib import pyplot
import matplotlib.backends.backend_pdf


def plot_all_graphs(filename,c1,c2):
    if c1==1:
        sizes = [len(rec) for rec in SeqIO.parse(filename, "fastq")]
        pyplot.hist(sizes, bins=20)
        pyplot.title("Histograph \n Total Sequences %i \n %i to %i" % (len(sizes),min(sizes),max(sizes)))
        pyplot.xlabel("Sequence length (bp)")
        pyplot.ylabel("Count")      
        pyplot.show()

    if c2==1:
        gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse(filename, "fastq"))
        pyplot.plot(gc_values)
        pyplot.title("Sequence GC Percentage \n Total Sequences %i \n GC%% %0.1f to %0.1f" \
            % (len(gc_values),min(gc_values),max(gc_values)))
        pyplot.xlabel("Genes")
        pyplot.ylabel("GC%")
        pyplot.show()
        

