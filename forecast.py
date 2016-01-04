#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://github.com/orjanv/Planetary-K-Index-alert

import requests
from datetime import datetime

USER_AGENT = 'Python3/Python CLI Planetary K-Index Alert App/0.1'

# Download the datafile from noaa.gov

url = 'http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt'
headers = {'User-Agent': USER_AGENT}
response = requests.get(url, headers=headers)
everything = response.readlines()

# We only need the last line

last_line = everything[-1]

# Extract the date we are interested in

today = last_line[0:10]
forecastdate = datetime.strptime(today, '%Y %m %d')

# Extract the last numbers, which is the planetary K-indices
# in three ours intervals and add to a list

ki = last_line[-17:]
fc = []
for i in range(0, len(ki)):
    k = ki[i]
    if k == '-':
        break
    elif k != ' ':
        fc.append(k)

# Determine if the level is four or more and output an alert message

hour = 3
for i in fc:
    if i >= '4':
        print 'The Planetary K-Index value:', str(i),
        ('was estimated today at', str(hour) + ':30 UTC time')
    hour += 3
