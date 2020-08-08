# #!/usr/bin/env python
# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment_0 = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0.0
month_counter = 0


while principal > 0:
    month_counter +=1
    if (month_counter>=extra_payment_start_month) and (month_counter<=extra_payment_end_month):
        payment = payment_0 + extra_payment
    else:
        payment = payment_0
    if ((principal * (1+rate/12)) <= payment):
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month_counter, total_paid, principal)
    
print('Total paid', total_paid)
print('month count', month_counter)


