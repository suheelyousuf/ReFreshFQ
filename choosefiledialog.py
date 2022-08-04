#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# By Suheel Yousuf Wani

import tkinter as tk
from tkinter import filedialog
import os
file_path=""

def choosefile():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path
#choosefile()
#print(file_path)
#print(type(file_path))
#print(os.path.basename(file_path))