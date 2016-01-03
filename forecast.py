#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, urllib2
from datetime import datetime

# Download the datafile from noaa.gov
url = "http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt"
response = urllib2.urlopen(url)
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
    if k == "-":
        break
    elif k != " ":
        fc.append(k)

# Determine if the level is four or more
hour = 3
for i in fc:
    if i >= "4":
        print ("The Planetary K-Index value:"), (str(i)), 
        ("was estimated today at"), (str(hour)) + (":30 UTC time")
    hour += 3
