#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:56:07 2018

@author: alexwest
"""

import pandas as pd

def load_data():
    """loads the dataset"""
    df = pd.read_csv("..data/airbnb.csv")
    df.head()

    
def information(neighbourhood):
    """ functionality 1"""
  
    pass

def search():
    """ functionality 2"""
    pass

def parse_arguments():
    """ parses the arguments"""
    pass

def main(arguments):
    """main entrypoint"""
    pass

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
    load_data();