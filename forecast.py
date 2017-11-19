#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# https://github.com/orjanv/Planetary-K-Index-alert

import urllib2
import argparse
#from datetime import datetime

USER_AGENT = 'Python-urllib/2.1'

def kpIndex():
    ''' Get the geomagnetic indices from NOAA and report the last forecast
    '''
    url = 'http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt'
    # Download the datafile from noaa.gov
    response = urllib2.urlopen(url)
    everything = response.readlines()

    # We only need the last line
    last_line = everything[-1]

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

    return fc[-1]


def bzValue():
    ''' Go online and get the magnetic sensor report from NOAA 
    and extract the Bz value which we are looking at
    '''
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
            bz = last_line[57:61]
            break
        else:
            line_number = line_number - 1
    return bz


def windSpeed():
    ''' Go online and grab the solar wind speed report from NOAA and
    grab the last line with a valid reading and pick the solar wind 
    speed
    '''
    url = 'ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_swepam_1m.txt'
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
            #today = last_line[0:16]
            #forecastdate = datetime.strptime(today, '%Y %m %d  %H%M')
            speed = last_line[54:59]
            break
        else:
            line_number = line_number - 1
    return speed
    
def main():
    ''' Main function
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--kpindex", help="Planetary K-Index",
        action="store_true")
    parser.add_argument("-w", "--windspeed", help="Solar Wind Speed",
        action="store_true")
    parser.add_argument("-b", "--bz", help="Magnetic Bz Value",
        action="store_true")
    parser.add_argument("-a", "--all", help="Show all values (default)",
        action="store_true")
    parser.add_argument("-f", "--forecast", help="Evaluate the chance of aurora",
        action="store_true")
    args = parser.parse_args()

    # Get all the values
    print "Downloading data...\n"
    kpi = kpIndex()
    bz = bzValue()
    wind = windSpeed()    

    if args.kpindex:
        print "KP-Index (NOAA):", kpi

    if args.windspeed:
        print "Wind speed (ACE):", wind
        
    if args.bz:
        print "Bz value (ACE):", bz    

    if args.all:   
        print "ACE-values are 1 hour away from earth, KP-index three hour forecast\n"     
        print "KP-Index (NOAA):", kpi
        print "Bz value (ACE):", bz
        print "Wind speed (ACE):", wind

    if args.forecast:
        # If bz is negative and kpi >= 4, chance of aurora
        if kpi >= 4 and bz < 0:
            print "KP-Index (NOAA):", kpi
            print "Bz value (ACE):", bz
            print "Wind speed (ACE):", wind

    else:
        print "ACE-values are 1 hour away from earth, KP-index three hour forecast\n"
        print "KP-Index (NOAA):", kpi
        print "Bz value (ACE):", bz
        print "Wind speed (ACE):", wind

if __name__ == '__main__':
    main()
