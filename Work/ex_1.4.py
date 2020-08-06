# #!/usr/bin/env python
# Exercise 1.4

import urllib.request as ur
u = ur.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)
##
