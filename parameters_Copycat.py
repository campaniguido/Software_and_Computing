# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:54:33 2022

@author: Guido
"""

import os


file_position='https://raw.githubusercontent.com/campaniguido/Software_and_Computing/main/roadnet-ca.txt'
number_of_edge=5000
name_simulation='Copycat'+str(number_of_edge)
path_to_save_data=os.getcwd()+'\\'+name_simulation

file_to_plot=os.getcwd()+'\\'+name_simulation
save_fig=True
extention='png'
nstep=50

seed=3
