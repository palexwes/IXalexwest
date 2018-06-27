# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
- For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
"""


def babynames(name):
    boycount = 0
    girlcount = 0
    for num in range(1900, 2018) :
        num = str(num)
        x = "data/names_" + num +".txt"
        file = open(x, 'r')
        mostpopline = file.readline()
        xy = mostpopline.split('|')
        if xy[1] == name:
            boycount+=1
        if xy[2] == name:
            girlcount+=1
    print(name)
    print("Boy : " + str(boycount))
    print("Girl : " + str(girlcount))
    
print(babynames("John"))



    
    
    