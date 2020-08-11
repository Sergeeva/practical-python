# #!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv


def portfolio_read_1(filename):
    '''
    read cvs file with 
    portfolio
    to list of tuples
    '''

    portfolio = []
    

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #print(headers)
        for row in rows:
            #print(row)
            t = (row[0], int(row[1]), float(row[2]))
            portfolio.append(t)
        
    return portfolio
##


def portfolio_read_2(filename):
    '''
    read cvs file with 
    portfolio
    to list of dictionaries
    '''

    portfolio = []
    

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #print(headers)
        for row in rows:
            #print(row)
            d={}
            d[headers[0]] =  row[0]
            d[headers[1]] =  int(row[1])
            d[headers[2]] =  float(row[2])
            portfolio.append(d)
        
    return portfolio
##


def prices_read(filename):
    '''
    read cvs file with 
    prices
    to dictionary
    '''

    prices = {}
    row_count = 0

    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        #headers = next(rows)
        #print(headers)
        for row in rows:
            #print(row)
            row_count+=1
            #try:
            val = float(row[1])
            #except ValueError:
                #print(f"Couldn't parse row {row_count}", row )
                
            prices[row[0]] = val 
        
    return prices
##

def current_portfolio_value(portfolio, prices):
    '''
    Compute current portfolio value
    and gain/loss 
    where
    portfolio is a list of tuples
    prices is 
    '''

    p_val_0 = 0.0
    p_val_curr = 0.0

    for item in portfolio:
        p_val_0 += item[1]*item[2]
        p_val_curr += item[1]*prices[item[0]]

    profit = p_val_curr - p_val_0
    return p_val_curr, p_val_0,  profit
##


portf = portfolio_read_1('Data/portfolio.csv')
prices = prices_read('Data/prices.csv')

curr_val, val_0, profit = current_portfolio_value(portf, prices)

print(f'''Current value: {curr_val:0.2f}
          Value 0: {val_0:0.2f}
          Profit: {profit:0.2f}''')
