#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani


'''
Module      : Main algorithm
Description : The main entry point for the program.
Copyright   : (c) Suheel Yousuf Wani, 29 july 2022 
License     : MIT 
Maintainer  : suheelhamdani@gmail.com 
'''

import sys
import os
from tkinter import *
from tkinter import messagebox
from Bio import SeqIO


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import fqgui_support

from choosefiledialog import choosefile

import basicstatistics
from searchsequence import search
from savefiledialog import file_save
from filterfastq import filter_file
from trimprimer import trimoffprimer
from merge_subtract import merge_fastq
from merge_subtract import subtract_fastq
from trimquality import trim_quality
from graphgeneration import plot_all_graphs
from validatefastq import isFastq


#global filepath1


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    #print("rest in peace")
    global val, w, root
    root = tk.Tk()
    #global filepath1
    fqgui_support.set_Tk_var()
    top = Toplevel1 (root)
    fqgui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    fqgui_support.set_Tk_var()
    top = Toplevel1 (w)
    fqgui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    #global filepath1
        #def loadfile(self):
                #filepath=choosefiledialog.choosefile()
    def loadfile(self):
            global filepath1
            filepath1=choosefile()
            #print(filepath1)
            self.lb_filename.configure(text=os.path.basename(filepath1))
            self.bt_process.configure(state="normal")
    def processfile(self):
            #print(filepath1)
            if len(filepath1)<1:
                    messagebox.showinfo("Error", "Please choose a Fastq file")
                    return

            if isFastq(filepath1)==False:
                    messagebox.showinfo("Error", "Not a Fastq file")
                    return
            for r in range(7):
                    self.notebook.tab(r, state="normal")
            
            self.txt_stat.insert(tk.END,"\n"+" File Name = "+os.path.basename(filepath1)+"\n")
            self.txt_stat.insert(tk.END,"\n"+" File Path = "+filepath1+"\n")
            stat=basicstatistics.statistics(filepath1)
            self.txt_stat.insert(tk.END,"\n"+" File Type = "+stat[2]+"\n")
            self.txt_stat.insert(tk.END,"\n"+" Total Sequences= "+str(stat[0])+"\n")
            self.txt_stat.insert(tk.END,"\n"+" Sequence Length="+str(stat[1])+"\n")
            self.txt_stat.insert(tk.END,"\n"+" GC % ="+str(stat[3])+"\n")
    def searchfastq(self):
            sequence=self.txt_sequence.get("1.0")
            print(len(sequence))
            if len(sequence)<=1:
                    messagebox.showinfo("Error", "Please enter a sequence")
                    return

            matchreads=search(filepath1,sequence)
            file_save(matchreads)
            return

    def selected(self):
            return self.var_system.get()
    def selected1(self):
            return self.var_system1.get()
    def trim_primer(self):
            primer=self.txt_primer.get()
            trimed_data=trimoffprimer(filepath1,primer)
            file_save(trimed_data)
            


    def browse_file_for_merge(self):
            global filepath2
            #print("hello im here")
            filepath2=choosefile()
            #print(filepath2)
            self.lb_filename2.configure(text=os.path.basename(filepath2))
            return

    def mergetwofiles(self):
            #str_m=""
            #print("im in main yes")
            str_m=merge_fastq(filepath1,filepath2)
            #print(str_m+"im in main")
            file_save(str_m)
            return
    def subtractfiles(self):
            str_s=""
            str_s=subtract_fastq(filepath1,filepath2)
            file_save(str_s)
            return
    def trim_quality(self):
            limit=int(self.txt_quality.get())
            str_qt=trim_quality(filepath1,limit)
            file_save(str_qt)
            return
    def plotgraphs(self):
            #print("hello")
            #print(self.check1.get(),self.check2.get())
            #print(filepath1)
            plot_all_graphs(filepath1,self.check1.get(),self.check2.get())
            return


                   

    def vew_filtered_file(self):
            rb1=self.selected()
            rb2=self.selected1()
            print(rb1,rb2)
            l=self.txt_from.get()
            u=self.txt_to.get()
            refine_data=""
            if rb1 == 3:
                if len(l)<1 or len(u)<1:
                    messagebox.showinfo("Error", "Please enter proper range")
                    return

                l=int(l)
                u=int(u)
                print(l,u)
                record_length = len(list(SeqIO.parse(filepath1, "fastq")))
                if l>=u and l<0 and u>=record_length:
                        messagebox.showinfo("Wrong Arguments", "Invalid Upper/Lower range arugumets")
                        return
                
            refine_data=filter_file(filepath1,rb1,rb2,l,u)
            file_save(refine_data)
            return


   
        



    
       



                
                    
            

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        #print("rest im here")
        self.var_system=IntVar()
        self.var_system1=IntVar()
        self.check1=IntVar()
        self.check2=IntVar()
        #self.check3=IntVar()
        #self.check4=IntVar()
        self.var_system1.set(0)
        
        #var.set(1)
        #var1.set(1)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 1 -overstrike 0"
        font13 = "-family {DejaVu Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("723x525+337+157")
        top.title("ReFreshFQ")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.221, rely=0.019, height=49, width=386)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {DejaVu Sans} -size 18 -weight bold")
        self.Label1.configure(text='''ReFreshFQ''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.152, rely=0.095, height=39, width=476)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font="-family {DejaVu Sans} -size 14 -slant italic")
        self.Label2.configure(text='''A GUI based tool for preprocessing of Fastq files''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.014, rely=0.171, relwidth=0.968)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.055, rely=0.21, height=29, width=266)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font="-family {DejaVu Sans} -size 11")
        self.Label3.configure(text='''Load FastQ file( .fastq, .fastq.gz )''')

        self.bt_browse = tk.Button(top)
        self.bt_browse.place(relx=0.415, rely=0.19, height=39, width=119)
        self.bt_browse.configure(activebackground="#f9f9f9")
        self.bt_browse.configure(font="-family {DejaVu Sans} -size 12")
        self.bt_browse.configure(justify='right')
        self.bt_browse.configure(text='''Browse...''')
        self.bt_browse.configure(command=self.loadfile)

        self.lb_filename = tk.Label(top)
        self.lb_filename.place(relx=0.581, rely=0.21, height=19, width=136)
        self.lb_filename.configure(activebackground="#f9f9f9")
        self.lb_filename.configure(font="-family {DejaVu Sans} -size 11 -slant italic")
        self.lb_filename.configure(justify='left')
        self.lb_filename.configure(text='''No file selected''')

        self.bt_process = tk.Button(top)
        self.bt_process.place(relx=0.373, rely=0.286, height=39, width=169)
        self.bt_process.configure(activebackground="#f9f9f9")
        self.bt_process.configure(font="-family {DejaVu Sans} -size 12 -weight bold")
        self.bt_process.configure(text='''Process File''')
        self.bt_process.configure(command=self.processfile)
        self.bt_process.configure(state="disabled")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.0, rely=0.381, relwidth=0.996)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.notebook = ttk.Notebook(top)
        self.notebook.place(relx=0.055, rely=0.4, relheight=0.579
                , relwidth=0.918)
        self.notebook.configure(takefocus="")
        #self.notebook.configure(state="DISABLED")
        self.notebook_t0 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t0, padding=3)
        self.notebook.tab(0, text="Statistics / Validate", compound="left", state="disabled"
                ,underline="-1", )
        self.notebook_t1 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t1, padding=3)
        self.notebook.tab(1, text="Search",compound="none",underline="-1",state="disabled")
        self.notebook_t2 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t2, padding=3)
        self.notebook.tab(2, text="View",compound="none",underline="-1",state="disabled")
        self.notebook_t3 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t3, padding=3)
        self.notebook.tab(3, text="Trim Primer", compound="none", underline="-1"
                ,state="disabled")
        self.notebook_t4 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t4, padding=3)
        self.notebook.tab(4, text="Compare / Merge", compound="none"
                ,underline="-1",state="disabled" )
        self.notebook_t5 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t5, padding=3)
        self.notebook.tab(5, text="Q-Trim",compound="none",underline="-1",state="disabled")
        self.notebook_t6 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t6, padding=3)
        self.notebook.tab(6, text="Plot Graphs", compound="none", underline="-1"
                ,state="disabled")

        self.txt_stat = tk.Text(self.notebook_t0)
        self.txt_stat.place(relx=0.03, rely=0.036, relheight=0.914
                , relwidth=0.946)
        self.txt_stat.configure(background="white")
        self.txt_stat.configure(font=font12)
        self.txt_stat.configure(selectbackground="#c4c4c4")
        self.txt_stat.configure(wrap="word")

        self.Label4 = tk.Label(self.notebook_t1)
        self.Label4.place(relx=0.03, rely=0.179, height=29, width=176)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='sw')
        self.Label4.configure(font="-family {DejaVu Sans} -size 12 -slant italic")
        self.Label4.configure(justify='left')
        self.Label4.configure(text='''Enter the Sequence:''')

        self.bt_search = tk.Button(self.notebook_t1)
        self.bt_search.place(relx=0.363, rely=0.786, height=49, width=189)
        self.bt_search.configure(activebackground="#f9f9f9")
        self.bt_search.configure(font="-family {DejaVu Sans} -size 12 -weight bold")
        self.bt_search.configure(text='''Search''')
        self.bt_search.configure(command=self.searchfastq)

        self.txt_sequence = tk.Text(self.notebook_t1)
        self.txt_sequence.place(relx=0.015, rely=0.286, relheight=0.45
                , relwidth=0.961)
        self.txt_sequence.configure(background="white")
        self.txt_sequence.configure(font="TkTextFont")
        self.txt_sequence.configure(selectbackground="#c4c4c4")
        self.txt_sequence.configure(wrap="word")

        self.Labelframe1 = tk.LabelFrame(self.notebook_t2)
        self.Labelframe1.place(relx=0.03, rely=0.071, relheight=0.625
                , relwidth=0.347)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(text='''Limit Options''')

        self.rb_first = tk.Radiobutton(self.Labelframe1,value=1,command=self.selected)
        self.rb_first.place(relx=0.0, rely=0.343, relheight=0.12, relwidth=0.53
                , bordermode='ignore')
        self.rb_first.configure(activebackground="#f9f9f9")
        self.rb_first.configure(anchor='sw')
        self.rb_first.configure(justify='left')
        self.rb_first.configure(text='''First 10 Reads''')
        self.rb_first.configure(variable=self.var_system)

        self.rb_last = tk.Radiobutton(self.Labelframe1,value=2,command=self.selected)
        self.rb_last.place(relx=0.0, rely=0.514, relheight=0.12, relwidth=0.53
                , bordermode='ignore')
        self.rb_last.configure(activebackground="#f9f9f9")
        self.rb_last.configure(anchor='sw')
        self.rb_last.configure(justify='left')
        self.rb_last.configure(text='''Last 10 Reads''')
        self.rb_last.configure(variable=self.var_system)

        self.txt_from = tk.Entry(self.Labelframe1)
        self.txt_from.place(relx=0.522, rely=0.686, height=21, relwidth=0.157
                , bordermode='ignore')
        self.txt_from.configure(background="white")
        self.txt_from.configure(font="TkFixedFont")
        self.txt_from.configure(selectbackground="#c4c4c4")

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.696, rely=0.686, height=19, width=16
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''to''')

        self.txt_to = tk.Entry(self.Labelframe1)
        self.txt_to.place(relx=0.783, rely=0.686, height=21, relwidth=0.157
                , bordermode='ignore')
        self.txt_to.configure(background="white")
        self.txt_to.configure(font="TkFixedFont")
        self.txt_to.configure(selectbackground="#c4c4c4")

        

        self.rb_allreads = tk.Radiobutton(self.Labelframe1,value=0,command=self.selected)
        self.rb_allreads.place(relx=0.0, rely=0.171, relheight=0.12
                , relwidth=0.443, bordermode='ignore')
        self.rb_allreads.configure(activebackground="#f9f9f9")
        self.rb_allreads.configure(anchor='sw')
        self.rb_allreads.configure(justify='left')
        self.rb_allreads.configure(text='''All Reads''')
        self.rb_allreads.configure(variable=self.var_system)
        self.rb_allreads.select()
        
        
        
        #self.rb_allreads.select()

        self.rb_range = tk.Radiobutton(self.Labelframe1,value=3,command=self.selected)
        self.rb_range.place(relx=0.0, rely=0.686, relheight=0.12, relwidth=0.487
                , bordermode='ignore')
        self.rb_range.configure(activebackground="#f9f9f9")
        self.rb_range.configure(anchor='sw')
        self.rb_range.configure(justify='left')
        self.rb_range.configure(text='''Reads from''')
        self.rb_range.configure(variable=self.var_system)
        
        

        self.Labelframe2 = tk.LabelFrame(self.notebook_t2)
        self.Labelframe2.place(relx=0.498, rely=0.071, relheight=0.625
                , relwidth=0.363)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(text='''Show Options''')

        self.rb_fourlines = tk.Radiobutton(self.Labelframe2,value=0,command=self.selected1)
        self.rb_fourlines.place(relx=0.0, rely=0.171, relheight=0.12
                , relwidth=0.592, bordermode='ignore')
        self.rb_fourlines.configure(activebackground="#f9f9f9")
        self.rb_fourlines.configure(anchor='sw')
        self.rb_fourlines.configure(justify='left')
        self.rb_fourlines.configure(text='''Reads( 4 Lines)''')
        self.rb_fourlines.configure(variable=self.var_system1)

        self.rb_sequencedata = tk.Radiobutton(self.Labelframe2,value=1,command=self.selected1)
        self.rb_sequencedata.place(relx=0.0, rely=0.343, relheight=0.12
                , relwidth=0.633, bordermode='ignore')
        self.rb_sequencedata.configure(activebackground="#f9f9f9")
        self.rb_sequencedata.configure(anchor='sw')
        self.rb_sequencedata.configure(justify='left')
        self.rb_sequencedata.configure(text='''Sequence Data Only''')
        self.rb_sequencedata.configure(variable=self.var_system1)

        self.rb_headerdata = tk.Radiobutton(self.Labelframe2,value=2,command=self.selected1)
        self.rb_headerdata.place(relx=0.0, rely=0.514, relheight=0.12
                , relwidth=0.55, bordermode='ignore')
        self.rb_headerdata.configure(activebackground="#f9f9f9")
        self.rb_headerdata.configure(anchor='sw')
        self.rb_headerdata.configure(justify='left')
        self.rb_headerdata.configure(text='''Header Data Only''')
        self.rb_headerdata.configure(variable=self.var_system1)

        self.rb_qualitydata = tk.Radiobutton(self.Labelframe2,value=3,command=self.selected1)
        self.rb_qualitydata.place(relx=0.0, rely=0.686, relheight=0.12
                , relwidth=0.717, bordermode='ignore')
        self.rb_qualitydata.configure(activebackground="#f9f9f9")
        self.rb_qualitydata.configure(anchor='sw')
        self.rb_qualitydata.configure(justify='left')
        self.rb_qualitydata.configure(text='''Quality Data Only''')
        self.rb_qualitydata.configure(variable=self.var_system1)

        self.rb_fasta = tk.Radiobutton(self.Labelframe2,value=4,command=self.selected1)
        self.rb_fasta.place(relx=0.0, rely=0.857, relheight=0.12, relwidth=0.717
                , bordermode='ignore')
        self.rb_fasta.configure(activebackground="#f9f9f9")
        self.rb_fasta.configure(anchor='sw')
        self.rb_fasta.configure(justify='left')
        self.rb_fasta.configure(text='''View in FASTA formate''')
        self.rb_fasta.configure(variable=self.var_system1)

        self.bt_view = tk.Button(self.notebook_t2)
        self.bt_view.place(relx=0.317, rely=0.75, height=49, width=159)
        self.bt_view.configure(activebackground="#f9f9f9")
        self.bt_view.configure(font="-family {DejaVu Sans} -size 12 -weight bold")
        self.bt_view.configure(text='''View''')
        self.bt_view.configure(command=self.vew_filtered_file)

        self.Label6 = tk.Label(self.notebook_t3)
        self.Label6.place(relx=0.181, rely=0.071, height=19, width=416)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(font="-family {DejaVu Sans} -size 14")
        self.Label6.configure(text='''Trimming Off Primer Sequences''')

        self.Label7 = tk.Label(self.notebook_t3)
        self.Label7.place(relx=0.03, rely=0.286, height=19, width=206)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='ne')
        self.Label7.configure(font="-family {DejaVu Sans} -size 12")
        self.Label7.configure(text='''Enter Primer Sequence''')

        self.TSeparator3 = ttk.Separator(self.notebook_t3)
        self.TSeparator3.place(relx=0.242, rely=0.143, relwidth=0.514)

        self.txt_primer = tk.Entry(self.notebook_t3)
        self.txt_primer.place(relx=0.347, rely=0.25,height=41, relwidth=0.583)
        self.txt_primer.configure(background="white")
        self.txt_primer.configure(font="TkFixedFont")
        self.txt_primer.configure(selectbackground="#c4c4c4")

        self.Label8 = tk.Label(self.notebook_t3)
        self.Label8.place(relx=0.65, rely=0.214, height=23, width=4)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(font="-family {DejaVu Sans} -size 12")

        self.bt_trim = tk.Button(self.notebook_t3)
        self.bt_trim.place(relx=0.332, rely=0.5, height=39, width=179)
        self.bt_trim.configure(activebackground="#f9f9f9")
        self.bt_trim.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.bt_trim.configure(text='''Trim''')
        self.bt_trim.configure(command=self.trim_primer)

        self.Label9 = tk.Label(self.notebook_t4)
        self.Label9.place(relx=0.015, rely=0.107, height=19, width=226)
        self.Label9.configure(anchor='se')
        self.Label9.configure(font=font9)
        self.Label9.configure(text='''Select FastQ File''')

        self.bt_browse2 = tk.Button(self.notebook_t4)
        self.bt_browse2.place(relx=0.363, rely=0.071, height=39, width=119)
        self.bt_browse2.configure(activebackground="#f9f9f9")
        self.bt_browse2.configure(font="-family {DejaVu Sans} -size 12")
        self.bt_browse2.configure(justify='right')
        self.bt_browse2.configure(text='''Browse...''')
        self.bt_browse2.configure(command=self.browse_file_for_merge)

        self.lb_filename2 = tk.Label(self.notebook_t4)
        self.lb_filename2.place(relx=0.544, rely=0.107, height=19, width=136)
        self.lb_filename2.configure(activebackground="#f9f9f9")
        self.lb_filename2.configure(font="-family {DejaVu Sans} -size 11 -slant italic")
        self.lb_filename2.configure(justify='left')
        self.lb_filename2.configure(text='''No file selected''')

        self.bt_merge = tk.Button(self.notebook_t4)
        self.bt_merge.place(relx=0.287, rely=0.393, height=39, width=109)
        self.bt_merge.configure(font=font13)
        self.bt_merge.configure(text='''Merge''')
        self.bt_merge.configure(command=self.mergetwofiles)

        self.bt_subtract = tk.Button(self.notebook_t4)
        self.bt_subtract.place(relx=0.483, rely=0.393, height=39, width=109)
        self.bt_subtract.configure(activebackground="#f9f9f9")
        self.bt_subtract.configure(font=font13)
        self.bt_subtract.configure(text='''Subtract''')
        self.bt_subtract.configure(command=self.subtractfiles)

        self.Label10 = tk.Label(self.notebook_t5)
        self.Label10.place(relx=0.227, rely=0.036, height=29, width=326)
        self.Label10.configure(font=font10)
        self.Label10.configure(text='''Quality Trim''')

        self.TSeparator4 = ttk.Separator(self.notebook_t5)
        self.TSeparator4.place(relx=0.332, rely=0.179, relwidth=0.302)

        self.Label11 = tk.Label(self.notebook_t5)
        self.Label11.place(relx=0.106, rely=0.25, height=29, width=236)
        self.Label11.configure(anchor='ne')
        self.Label11.configure(font=font9)
        self.Label11.configure(text='''Trim Reads with Quality <=''')

        self.txt_quality = tk.Entry(self.notebook_t5)
        self.txt_quality.place(relx=0.468, rely=0.25,height=21, relwidth=0.069)
        self.txt_quality.configure(background="white")
        self.txt_quality.configure(font="TkFixedFont")

        self.bt_trimquality = tk.Button(self.notebook_t5)
        self.bt_trimquality.place(relx=0.423, rely=0.464, height=29, width=119)
        self.bt_trimquality.configure(font=font11)
        self.bt_trimquality.configure(text='''Trim''')
        self.bt_trimquality.configure(command=self.trim_quality)

        self.bt_plot = tk.Button(self.notebook_t6)
        self.bt_plot.place(relx=0.378, rely=0.643, height=29, width=129)
        self.bt_plot.configure(font=font13)
        self.bt_plot.configure(text='''Plot''')
        self.bt_plot.configure(command=self.plotgraphs)

        self.cb_histogram = tk.Checkbutton(self.notebook_t6)
        self.cb_histogram.place(relx=0.302, rely=0.179, relheight=0.095
                , relwidth=0.443)
        self.cb_histogram.configure(anchor='nw')
        self.cb_histogram.configure(font=font9)
        self.cb_histogram.configure(justify='left')
        self.cb_histogram.configure(text='''Histogram Of Sequence Lengths''')
        self.cb_histogram.configure(variable=self.check1)

        self.cb_gc = tk.Checkbutton(self.notebook_t6)
        self.cb_gc.place(relx=0.302, rely=0.286, relheight=0.095, relwidth=0.443)

        self.cb_gc.configure(activebackground="#f9f9f9")
        self.cb_gc.configure(anchor='nw')
        self.cb_gc.configure(font="-family {DejaVu Sans} -size 12")
        self.cb_gc.configure(justify='left')
        self.cb_gc.configure(text='''Sequence GC%''')
        self.cb_gc.configure(variable=self.check2)
        

        '''self.cb_nucleotide = tk.Checkbutton(self.notebook_t6)
        self.cb_nucleotide.place(relx=0.302, rely=0.393, relheight=0.075
                , relwidth=0.443)
        self.cb_nucleotide.configure(activebackground="#f9f9f9")
        self.cb_nucleotide.configure(anchor='nw')
        self.cb_nucleotide.configure(font="-family {DejaVu Sans} -size 12")
        self.cb_nucleotide.configure(justify='left')
        self.cb_nucleotide.configure(text='Nucleotide Dot Plots')
        self.cb_nucleotide.configure(variable=self.check3)

        self.cb_quality = tk.Checkbutton(self.notebook_t6)
        self.cb_quality.place(relx=0.302, rely=0.5, relheight=0.075
                , relwidth=0.443)
        self.cb_quality.configure(activebackground="#f9f9f9")
        self.cb_quality.configure(anchor='nw')
        self.cb_quality.configure(font="-family {DejaVu Sans} -size 12")
        self.cb_quality.configure(justify='left')
        self.cb_quality.configure(text=''Quality Scores')
        self.cb_quality.configure(variable=self.check4)'''

if __name__ == '__main__':
    vp_start_gui()





