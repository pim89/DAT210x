# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')


curdir = os.path.dirname(__file__)
filename = os.path.join(curdir,'Datasets','students.data')
student_dataset = pd.read_csv(filename, index_col = 0)