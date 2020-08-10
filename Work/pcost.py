# #!/usr/bin/env python
# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row)
        total_cost+=int(row[1])*float(row[2])
##
print(total_cost)
