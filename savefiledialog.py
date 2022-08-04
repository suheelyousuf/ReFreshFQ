#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

import tkinter as tk
from tkinter import filedialog

def file_save(filetext):
    f = filedialog.asksaveasfile(mode='w', defaultextension=".fasta")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    #text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(filetext)
    f.close() # `()` was missing.

