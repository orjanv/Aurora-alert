#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://github.com/orjanv/Planetary-K-Index-alert

import urllib2
from datetime import datetime

USER_AGENT = 'Python3/Python CLI Planetary K-Index Alert App/0.1'
URL = 'http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt'

if __name__ == '__main__':

    # Download the datafile from noaa.gov
    response = urllib2.urlopen(URL)
    everything = response.readlines()

    # We only need the last line
    last_line = everything[-1]

    # Extract the date we are interested in
    today = last_line[0:10]
    forecastdate = datetime.strptime(today, '%Y %m %d')

    # Extract the last numbers, which is the planetary K-indices
    # in three ours intervals and add to a list
    ki = last_line[-17:]
    print ki #debug
    fc = []
    for i in range(0, len(ki)):
        k = ki[i]
        if k == '-':
            break
        elif k != ' ':
            fc.append(k)

    # Determine if the level is four or more and output an alert message
    for i in fc:
        print i
        hour = 3
        if i >= '4':
            print 'The Planetary K-Index value:', str(i),
            ('was estimated today at', str(hour) + ':30 UTC time')
        else:
            pass
