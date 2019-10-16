from Bio import SeqIO
#from savefiledialog import file_save
import gzip
from CheckIsCompressed import isCompressed

def filter_file(filename,radio1,radio2,range_l,range_u):
    str_file=""
    if radio1==0:
        print(str(radio1)+"imhere")
        str_file=fetch_all_reads(filename,radio2)
    elif radio1==1:
        str_file=fetch_head_reads_only(filename,radio2)
    elif radio1==2:
        str_file=fetch_bottam_reads_only(filename,radio2)
    else:
        print("")
        str_file=fetch_inrange_reads_only(filename,radio2,range_l,range_u)
    return str_file
       


def fetch_all_reads(filename,option):
    filter_str=""
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq"))
                    break
            elif option==1:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.seq)+"\n"
            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
            else:

                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    filter_str=filter_str+str(read.seq)+"\n"
                
    else:
        with open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq"))
                    print("im in option 0")
                    #print(filter_str)
                    
            elif option==1:
                for read in SeqIO.parse(handle,"fastq"):
                    print("im in option 1")
                    filter_str=filter_str+str(read.seq)+"\n"
            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    filter_str=filter_str+str(read.seq)+"\n"
    return filter_str


def fetch_head_reads_only(filename,option):
    filter_str=""
    count=0
    #record_length = len(list(SeqIO.parse("test.fastq", "fastq")))
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    
                    filter_str=filter_str+str(read.format("fastq"))
                    count=count+1
                    if count >= 10:
                        break


                        
            elif option==1:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.seq)+"\n"
                    if count >= 10:
                        break
            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    if count >= 10:
                        break
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                    if count >= 10:
                        break
            else:

                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    filter_str=filter_str+str(read.seq)+"\n"
                    if count >= 10:
                        break
                
    else:
        with open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq"))
                    count=count+1
                    print(count)
                    if count >= 10:
                        break
                        
            elif option==1:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.seq)+"\n"
                    if count >= 10:
                        break
            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    if count >= 10:
                        break
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                    if count >= 10:
                        break
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    filter_str=filter_str+str(read.id)+"\n"
                    filter_str=filter_str+str(read.seq)+"\n"
                    if count >= 10:
                        break
    return filter_str


def fetch_bottam_reads_only(filename,option):
    filter_str=""
    count=0
    record_length = len(list(SeqIO.parse("test.fastq", "fastq")))
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.format("fastq"))
                            count=count+1
                        else:
                            count=count+1

                    
                    


                        
            elif option==1:
                 for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.seq)+"\n"
                            count=count+1
                        else:
                            count=count+1

            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.id)+"\n"
                            count=count+1
                        else:
                            count=count+1
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                            count=count+1
                        else:
                            count=count+1
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.id)+"\n"
                            filter_str=filter_str+str(read.seq)+"\n"
                            count=count+1
                        else:
                            count=count+1
                                           
                    else:
                        filter_str=filter_str+str(read.id)+"\n"
                        filter_str=filter_str+str(read.seq)+"\n"

                
    else:
        with open(filename, "rt") as handle:
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.format("fastq"))
                            count=count+1
                        else:
                            count=count+1

                    
                    


                        
            elif option==1:
                 for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.seq)+"\n"
                            count=count+1
                        else:
                            count=count+1

            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.id)+"\n"
                            count=count+1
                        else:
                            count=count+1
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                            count=count+1
                        else:
                            count=count+1
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    if record_length>10:
                        if count>=record_length-10:
                            filter_str=filter_str+str(read.id)+"\n"
                            filter_str=filter_str+str(read.seq)+"\n"
                            count=count+1
                        else:
                            count=count+1
                                           
                    else:
                        filter_str=filter_str+str(read.id)+"\n"
                        filter_str=filter_str+str(read.seq)+"\n"
    return filter_str



def fetch_inrange_reads_only(filename,option,l_range,u_range):
    filter_str=""
    count=0
    print("hello")
    print(l_range,u_range)
    record_length = len(list(SeqIO.parse("test.fastq", "fastq")))
    if isCompressed(filename):
        with gzip.open(filename, "rt") as handle:
            #filterstr=""
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                        filter_str=filter_str+str(read.format("fastq"))
                        count=count+1
                    count=count+1 

                    
                    


                        
            elif option==1:
                 for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.seq)+"\n"
                       count=count+1
                    count=count+1

            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.id)+"\n"
                       count=count+1
                    count=count+1
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                       count=count+1
                    count=count+1
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.id)+"\n"
                       filter_str=filter_str+str(read.seq)+"\n"
                       count=count+1
                    count=count+1

                
    else:
        with open(filename, "rt") as handle:
            if option==0:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                        filter_str=filter_str+str(read.format("fastq"))
                        count=count+1
                    count=count+1

                    
                    


                        
            elif option==1:
                 for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.seq)+"\n"
                       count=count+1
                    count=count+1

            elif option==2:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.id)+"\n"
                       count=count+1
                    count=count+1
            elif option==3:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.format("fastq").split("\n")[3])+"\n"
                       count=count+1
                    count=count+1
            else:
                for read in SeqIO.parse(handle,"fastq"):
                    if count>=l_range-1 and count<=u_range+1:
                       filter_str=filter_str+str(read.id)+"\n"
                       filter_str=filter_str+str(read.seq)+"\n"
                       count=count+1
                    count=count+1
    return filter_str
            
           

