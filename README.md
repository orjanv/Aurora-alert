## About the forecast script

### Planetary K-Index

The K-index, and by extension the *Planetary K-index*, are used to characterize the magnitude of geomagnetic storms. Kp is an excellent indicator of disturbances in the Earth's magnetic field and is used by SWPC to decide whether geomagnetic alerts and warnings need to be issued for users who are affected by these disturbances.

The principal users affected by geomagnetic storms are the electrical power grid, spacecraft operations, users of radio signals that reflect off of or pass through the ionosphere, and observers of the aurora.

It can therefore be useful to be alerted if the K-index reach 4, 5, 6, 7, 8, or 9.

Data source: http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt

Read more at

* http://www.swpc.noaa.gov/products/planetary-k-index)

### Solar wind speed

Higher solar wind speeds and strong south pointing (negative) interplanetary 
magnetic field are associated with geomagnetic disturbances on earth.

Data source: ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_swepam_1m.txt

Read more at 

* http://www.sws.bom.gov.au/Solar/1/4
* http://aurorasaurus.org/storm-tracker

### Negative or positive Bz

Data source: ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_mag_1m.txt

Read more at [NOAA](http://www.swpc.noaa.gov/products/planetary-k-index)s pages.

### Alternative sources for Solar wind and Bz

* http://services.swpc.noaa.gov/products/summary/solar-wind-speed.json
* http://services.swpc.noaa.gov/products/summary/solar-wind-mag-field.json


## Installation
If you don't have `git` installed, install it as well as the `mailx` command from `mailutils` package using your distributions package management.

Clone into the repository:

```bash
git clone https://github.com/orjanv/Planetary-K-Index-alert.git
```

Make sure the program is executable:
```bash
sudo chmod a+x forecast.py
``` 

Make a symbolic link to the program
```bash
sudo ln -s /PATH/TO/Planetary-K-Index-alert/forecast.py /usr/bin/aurora-forecast
```

Add to your crontab to run every whole hour with the following entry:

```bash
crontab -e
0 * * * *	/PATH/TO/check-kp.sh
```

Remember to change the email address in the bash script `check-kp.sh`.

## Running the script

python forecast.py will give you an output if bz is negative and kpi >= 4, 
which means that there is a chance of aurora.

### Command line arguments

```bash
usage: forecast.py [-h] [-k] [-w] [-b] [-a] [-f]

optional arguments:
  -h, --help       show this help message and exit
  -k, --kpindex    Planetary K-Index
  -w, --windspeed  Solar Wind Speed
  -b, --bz         Magnetic Bz Value
  -a, --all        Show all values (default)
  -f, --forecast   Evaluate the chance of aurora
```
