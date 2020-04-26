# ReFreshFQ: A GUI based tool for the preprocessing of FastQ files

In Next Generation Sequencing (NGS) data analyses, some primary preprocessing of sequences data is needed before these sequences go for analysis in different tools or pipelines. These manipulations or preprocessing tasks includes finding a particular sequence pattern, changing file format , statistics of data within files, merging of files, per read quality control(QC), adapter trimming, quality filtering, per-read quality cutting etc. To ease these tasks, we developed a Graphical User Interface (GUI) based software suite that will help the scientists and researchers in manipulations of FASTQ files with ease. The ReFreshFQ is a containerized tool that makes it easy-to-install and easy-to-run. 

## ReFreshFQ can do following tasks on fastq files.

•	Basic file statistics like count FASTQ file reads, average FASTQ read lengths, GC% etc.

•	Find FASTQ reads containing specific sequences.

•	View FASTQ files with different options like show first ten reads, show last ten reads, show reads within range, show sequence data only, show header data only, show quality data only, view in fasta format.

•	Trimming off primer sequences.

•	Merge two fastq files.

•	Subtract one fastq file from another fastq file.

•	Trim reads that has low quality score.

•	Explain statistics of fastq files by generating graphs. 

•	Validate fastq file.

## Installation

ReFreshFQ requirs BioPython library installed,

To install BioPython in your system, type "pip install biopython"

If BioPython is already installed, building can be performed similar to the following:

git clone https://github.com/suheelyousuf/ReFreshFQ.git
cd ReFreshFQ
And to run the tool,
python fqgui.py
