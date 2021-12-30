# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:47:13 2020

@author: chemuser
"""
import os
import sys
import glob
import fnmatch
import numpy as np
import pandas as pd
import matplotlib as pl


file = r'F:\NTO absorption differences for opus'

os.chdir(file)

cwd = os.getcwd()
print(cwd)

list = os.listdir(file)

for filename in list:
    print(filename)
    if fnmatch.fnmatch(filename,'*_da_xy.asc'):
        newfilename = filename.replace('_da_xy.asc','.dat_xy.asc')
        print(newfilename)
        os.rename(filename,newfilename)