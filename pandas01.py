#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:41:54 2024

@author: thobekile
"""

import pandas

file = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/country_data.csv")

file1 = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/housing_data.csv")

file2 = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/diab_data.csv")

file3 = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/insurance_data.csv", skiprows=[0,1, 2, 3, 4])

file4 = pandas.read_csv("/home/thobekile/gitrepo/CHPC_Coding_Summer_School_2024/data_01/iris.csv")






print(file)
print(file.info())
print(file.describe())

print("\nHello Thobie")




z= 100
y= 50
x = 60

print(x+y+z**2)



density = 1000

Density = 900

mass_kg = 50

volume = 30



water_level_m_above_sea_level = 14.48

asteroid_orbit_type = "apollo"

print("housing")

print(file1)
print(file1.info())
print(file1.describe())

"""

"""
print(file2)
print(file2.info())
print(file2.describe())



print(file4)
print(file4.info())
print(file4.describe())



print(file3)
print(file3.info())
print(file3.describe())





