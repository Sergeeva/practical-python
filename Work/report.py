# #!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

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
        htypes = [str, int, float]
        #print(headers)
        for row in rows:
            #print(row)
            converted_row = [func(val) for func, val in zip (htypes,row)]
            d=dict(zip(headers, converted_row))
            #d[headers[0]] =  row[0]
            #d[headers[1]] =  int(row[1])
            #d[headers[2]] =  float(row[2])
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
    #row_count = 0

    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        #headers = next(rows)
        #print(headers)
        for i, row in enumerate (rows):
            #print(row)
            #row_count+=1
            try:
                prices[row[0]] = float(row[1])
            except:
                #IndexError
                print(f"Couldn't parse row {i}", row )
                pass
        
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


def make_report(portfolio, prices):
    '''
    Make list of tuples 
    with actual information 
    '''

    rep = []
    for item in portfolio:
        val_0 = item[1]*item[2]
        val_curr = item[1]*prices[item[0]]
        rep_item = (item[0], item[1], prices[item[0]], (val_curr - val_0))
        rep.append(rep_item)
        
    return rep
##


def print_report(r):
    '''
    Printing report table
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'---------- ---------- ---------- -----------')
    for name, shares, price, change in r:
        price_str = '$'+ str(round(price, 2))
        #print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')
    print(f'--------------------------------------------')

    return

portf = portfolio_read_1('Data/portfolio.csv')

portf_dict = portfolio_read_2('Data/portfolio.csv')
pprint(portf_dict)

prices = prices_read('Data/prices.csv')

#curr_val, val_0, profit = current_portfolio_value(portf, prices)
#print(f'''Current value: {curr_val:0.2f}
#          Value 0: {val_0:0.2f}
#          Profit: {profit:0.2f}''')

r = make_report(portf, prices)
print_report(r)
