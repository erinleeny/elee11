# Erin Lee (with May Hathaway and Victoria Gao—Team Burgers) 
# SoftDev
# K07 — StI/O: Divine your Destiny! Returning an occupation based on the percentage.
# 2020-10-02

"""
Our approach: We created a dictionary with an interval's end number as the keys and occupations as the values.
We generated a random number from 0 to 99.8, and based on which interval it lied in, we returned the occupation 
corresponding to that interval.
-----------------------------------------------
Dictionary:                                     |Intervals:
{6.1: 'Management',                             | [0,6.1)
 11.1:'Business and Financial operations',      | [6.1,11.1)
 ...,                                           |  ...
 93.3: 'Production',                            | [87.2,93.3)
 99.8: 'Transportation and material moving'     | [93.3,99.8)
}
If an occupation has 5% chance, its corresponding dictionary key is the previous occupation's interval end number + 5%.
We used a for loop to iterate through the dictionary:
If the random number is less than a key, return the occupation (dictionary value).
If not, check if the random number is less than the next dictionary key.
"""

import csv
import random

occupations = open("occupations.csv", "r")
data = occupations.readlines()
occupations.close()
current_total = 0
percent_dict = {}
for i in range(1, len(data)-1):
    if data[i][0] == '"': 
        data_set = data[i].split('",')
        title = data_set[0][1:]
    else:
        data_set = data[i].split(",")
        title = data_set[0]
    percent = float(data_set[1]) 
    percent_dict[round(percent + current_total, 1)] = title
    current_total = current_total + percent

def return_occupation():
    rand_num = random.randrange(0,998) / 10.0 
    for percent in percent_dict:
        if rand_num <= percent:
            return(percent_dict[percent])

print(return_occupation())