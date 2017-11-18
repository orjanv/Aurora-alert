#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://github.com/orjanv/Planetary-K-Index-alert

import urllib2
from datetime import datetime

USER_AGENT = 'Python3/Python CLI Planetary K-Index Alert App/0.1'

kpIndex():
    url = 'http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt'
    # Download the datafile from noaa.gov
    response = urllib2.urlopen(url)
    everything = response.readlines()

    # We only need the last line
    last_line = everything[-1]

    # Extract the date we are interested in
    today = last_line[0:16]
    forecastdate = datetime.strptime(today, '%Y %m %d  %H%M')

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

    return fc[-1], forecastdate
    # Determine if the level is four or more and output an alert message
    #for i in fc:
        #print i
        #hour = 3
        #if i >= '4':
            #print 'The Planetary K-Index value:', str(i),
            #('was estimated today at', str(hour) + ':30 UTC time')
        #else:
            #pass

bzValue():
    url = 'ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_mag_1m.txt'
    # Download the datafile from noaa.gov
    response = urllib2.urlopen(url)
    everything = response.readlines()

    # We only need the last line, but if last line has corrupt data, 
    # grab the previous, and so on..    
    data_status = 9
    line_number = -1
    while True:
        last_line = everything[line_number]
        data_status = last_line[36:37]
        # Check the status of the data (bad or corrupt)
        if data_status == '0':
            # Extract the data we are interested in and stop
            today = last_line[0:16]
            forecastdate = datetime.strptime(today, '%Y %m %d  %H%M')
            bz = last_line[57:61]
            break
        else:
            line_number = line_number - 1

    return bz, forecastdate
    

if __name__ == '__main__':
    kpi = kpIndex()
    bz = bzValue()

    print kpi
    print bz
