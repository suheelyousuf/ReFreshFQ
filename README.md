# ReFreshFQ: A GUI based tool for the preprocessing of FastQ files

An essential procedure of sequence data is required in Next Generation Sequencing (NGS)  before these sequences are used for research in various tools or pipelines. 
These operations or preprocessing activities include discovering a particular sequence pattern, altering file format, data statistics, merging files, per-read quality control (QC), adapter trimming, quality filtering, and per-read quality cutting among others.
To make these activities more manageable, we created a software package with a graphical user interface (GUI) that would immediately assist scientists and researchers in manipulating FASTQ data. ReFreshFQ is a containerized solution that is simple to install and use.

## ReFreshFQ can do following tasks on fastq files.

•	Basic file statistics like count FASTQ file reads, average FASTQ read lengths, GC% etc.

•	Find FASTQ reads containing specific sequences.

•	Viewing FASTQ files offer a variety of choices, including the ability to examine the first 10 reads, the last 10 reads, reads within a range, sequence data just, header data alone, quality data only, and fasta format.

•	Trimming off primer sequences.

•	Merge two fastq files.

•	Subtract one fastq file from another fastq file.

•	Trim reads that have a low-quality score.

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

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture1.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture2.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture3.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture4.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture5.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture6.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture7.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture8.PNG)

![Home Screen](https://github.com/suheelyousuf/ReFreshFQ/blob/master/screens/Capture9.PNG)
