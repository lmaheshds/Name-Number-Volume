# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:40:11 2020

@author: MAHESH.L
"""
##############################################################################################
# Problem
#  Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

# Solution
First_Name = input('Input your First Name = ')

Last_Name = input('Input your Last Name = ')

# Once the user types in the First and Last name, the last name
# and First name are printed with spaces as below
print('Hi' ' '+Last_Name,'',''+First_Name, 'is the name in reverse order')

###############################################################################################

###############################################################################################
# Problem
# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed 
# in a comma-separated sequence on a single line.

# Solution
# Step 1 Importing Libraries
import pandas as pd
import numpy as np

# Step 2 Let us create a list as shown below
Numbers = []

# Step 3 Now, Let us create a User defined function to find all numbers
# which are divisible by 7 but are not multiple of 5 between 2000 and 3200
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        Numbers.append(str(i))
Num = (','.join(Numbers))

# Step 4 Let us print the numbers which are divisible by 7 and not a multiple of 5
print (Num)
################################################################################################

################################################################################################
# Problem
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r^ 3

# Solution
# Importing the Libraries
import pandas as pd
import numpy as np

# Inputs
Diameter = 12

Radius = Diameter / 2

Pi = 22 / 7

Volume = 4 / 3 * Pi * Radius **3

print('The Volume of Sphere = ',Volume)
 
################################################################################################