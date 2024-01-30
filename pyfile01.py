#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:16:20 2024

@author: thobekile
"""

#Storing data in python
"""
1. Lists
2. Dictionaries

"""

import pandas

file = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/country_data.csv")

print(file)
age = [30, 25, 29, 46, 22]

print(age[0])

#first element starts at 0


print(max(age))


avg = sum(age)/len(age)
print(avg)

g1 = "M"
g2 ="F"
g3 ="M"

gender = ["M", "F","M"]



"""

Data frames 


"""



