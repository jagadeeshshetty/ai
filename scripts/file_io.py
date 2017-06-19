# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:20:41 2017

@author: jagadeesh
"""

name = ['Name1', 'Name2', 'Name3']
age = [10, 20, 30]
company = ['a', 'b', 'c']

file = open('sample_text.csv', 'w')

for i in range(3):  
    file.write('%s, %s, %s\n' %(name[i], age[i], company[i]))
    
file.close()


