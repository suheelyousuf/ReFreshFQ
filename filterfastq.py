#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

from Bio import SeqIO
#from savefiledialog import file_save
import gzip
from tkinter import filedialog
import shutil
import os


#from CheckIsCompressed import isCompressed



def filter_file(handle,radio1,radio2,size,range_l,range_u):
    
    
    if radio1==0:
        #print(str(radio1)+"imhere")
        fetch_all_reads(handle,radio2)
        f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
        with open("copy.fastq","r") as old:
            shutil.copyfileobj(old,f)
            
                
        os.remove("copy.fastq")
        f.close()
       # str_file.close()
        

    elif radio1==1:
        fetch_head_reads_only(handle,radio2)
        f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
        with open("copy.fastq","r") as old:
            shutil.copyfileobj(old,f)
            
                
        os.remove("copy.fastq")
        f.close()
    elif radio1==2:
        fetch_bottam_reads_only(handle,radio2)
        f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
        with open("copy.fastq","r") as old:
            shutil.copyfileobj(old,f)
            
                
        os.remove("copy.fastq")
        f.close()
    else:
        #print("")
        fetch_inrange_reads_only(handle,radio2,size,range_l,range_u)
        f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
        with open("copy.fastq","r") as old:
            shutil.copyfileobj(old,f)
            
                
        os.remove("copy.fastq")
        f.close()
    #return str_file
       


def fetch_all_reads(handle,option):
    if option==0:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                SeqIO.write(SeqIO.parse(handle, "fastq"), destination_fastq, "fastq")
                return destination_fastq
        
        except Exception as e:
            print(f"Error: {e}")

    elif option == 1:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                for record in SeqIO.parse(handle, "fastq"):
                    destination_fastq.write(f"{record.seq}\n")
                return destination_fastq
        except Exception as e:
            print(f"Error: {e}")

    elif option == 2:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for record in SeqIO.parse(handle,"fastq"):
                    destination_fastq.write(f">{record.id}\n")
                return destination_fastq
        except Exception as e:
            print(f"Error: {e}")

    elif option == 3:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for recod in SeqIO.parse(handle,"fastq"):
                    destination_fastq.write(record.letter_annotations["phred_quality"]+"\n")
                return destination_fastq
        except Exception as e:
            print(f"Error: {e}")

    elif option == 4:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for record in SeqIO.parse(handle,'fastq'):
                    destination_fastq.write(f">{record.id}\n{record.seq}\n")
                return destination_fastq
            
        except Exception as e:
            print(e)


        


    '''filter_str=""
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
    return filter_str'''


def fetch_head_reads_only(handle,option):

    count=0
    if option==0:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                for record in SeqIO.parse(handle,"fastq"):
                    destination_fastq.write(recod.format("fastq"))
                    count=count+1
                    if count >=10:
                        return destination_fastq
                
        
        except Exception as e:
            print(f"Error: {e}")

    elif option == 1:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                for record in SeqIO.parse(handle, "fastq"):
                    destination_fastq.write(f"{record.seq}\n")
                    count=count+1
                    if count >=10:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 2:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for record in SeqIO.parse(handle,"fastq"):
                    destination_fastq.write(f">{record.id}\n")
                    count=count+1
                    if count >=10:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 3:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for recod in SeqIO.parse(handle,"fastq"):
                    destination_fastq.write(record.letter_annotations["phred_quality"]+"\n")
                    count=count+1
                    if count >=10:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 4:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                for record in SeqIO.parse(handle,'fastq'):
                    destination_fastq.write(f">{record.id}\n{record.seq}\n")
                    count=count+1
                    if count >=10:
                        return destination_fastq
                            
        except Exception as e:
            print(e)

    '''filter_str=""
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
    return filter_str'''


def fetch_bottam_reads_only(handle,option,size):

    if option==0:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if count >=size-10:
                        destination_fastq.write(recod.format("fastq"))
                        count=count+1
                    count=count+1
                    if count ==size:
                        return destination_fastq
                
        
        except Exception as e:
            print(f"Error: {e}")

    elif option == 1:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if count >=size-10:
                        destination_fastq.write(f"{record.seq}\n")
                        count=count+1
                    count=count+1
                    if count ==size:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 2:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if count >=size-10:
                        destination_fastq.write(f">{record.id}\n")
                        count=count+1
                    count=count+1
                    if count ==size:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 3:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if count >=size-10:
                        destination_fastq.write(record.letter_annotations["phred_quality"]+"\n")
                        count=count+1
                    count=count+1
                    if count ==size:
                        return destination_fastq
                
        except Exception as e:
            print(f"Error: {e}")

    elif option == 4:
        try:
            with open("copy.fastq",'w') as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if count >=size-10:
                        destination_fastq.write(f">{record.id}\n{record.seq}\n")
                        count=count+1
                    count=count+1
                    if count ==size:
                        return destination_fastq
                            
        except Exception as e:
            print(e)





    
    
    '''
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
    return filter_str'''



def fetch_inrange_reads_only(handle,option,size,l_range,u_range):


    if u_range>l_range or l_range<0 or u_range>size-1:
        return
    if option==0:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if l_range <= count + 1 <= u_range:
                       
                       SeqIO.write(record, destination_fastq, "fastq")
                       if count + 1 >= u_range:
                           return destination_fastq
    
                  
        
        except Exception as e:
            print(f"Error: {e}")

    if option == 1:
        try:
            with open("copy.fastq", "w") as destination_fastq:
                count=0
                for record in SeqIO.parse(handle,"fastq"):
                    if l_range <= count + 1 <= u_range:
                       
                       SeqIO.write(record, destination_fastq, "fastq")
                       if count + 1 >= u_range:
                           return destination_fastq
    
                  
        
        except Exception as e:
            print(f"Error: {e}")

    
    


    

    '''
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
    return filter_str'''
            
           

