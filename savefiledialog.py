#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

import tkinter as tk
from tkinter import filedialog
import shutil


def file_save(fileobj):

    print("function starts")
    print(type(fileobj))
    f = filedialog.asksaveasfile(mode='w', defaultextension=".fastq")
    print("after new file")
    print(type(f))
    print(type(fileobj))
    #fileobj.seek(0)
    
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        print("resturn")
        return
    
    while True:
        buffer = fileobj.read(8192)
        if not buffer:
            break
        f.write(buffer)

    fileobj.close()
    f.close()
    
    #shutil.copyfileobj(fileobj,f)
    #text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    #f.write(filetext)
    f.close()
    #fileobj.close() # `()` was missing.

