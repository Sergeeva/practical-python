# #!/usr/bin/env python
# bounce.py
#
# Exercise 1.5

height_curr = 100.0
bounce_counter = 0

while bounce_counter<10:
    bounce_counter+=1
    height_curr = 3*height_curr/5
    print(bounce_counter, height_curr, round(height_curr,4))

##
