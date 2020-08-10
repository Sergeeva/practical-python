# #!/usr/bin/env python
# pcost.py
#
# Exercise 1.27

import sys
import csv

def pcost(filename):
    '''
    compute total cost
    of portfolio
    '''
    total_cost = 0.0
    
#    try:
#        f = open(filename, 'rt')
#    except ValueError:
#       print("File error")
    with open(filename, 'rt') as f: 
        headers = next(f).split(',')
        print(headers)
        for line in f:
            row = line.split(',')
            print(row)
            total_cost+=int(row[1])*float(row[2])
#    f.close()

##
    return total_cost



def pcost_csv(filename):
    '''
    compute total cost
    of portfolio
    with using csv module
    '''
    total_cost = 0.0
    
#    try:
#        f = open(filename, 'rt')
#    except ValueError:
#       print('File error')

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for row in rows:
            print(row)
            total_cost+=int(row[1])*float(row[2])
            
    #f.close()
    ##
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

tc = pcost(filename)

tc1 = pcost_csv(filename)


print(tc, tc1)
