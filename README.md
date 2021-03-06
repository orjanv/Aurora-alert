## About the forecast script

The ACE satellite is positioned between the Earth and the Sun and are able to give us a heads up using its sensors onboard and a radiolink to ground stations on our planet.

The constant Solar wind coming from the Sun will need at daytime about an hour traveltime before it possibly collide and sneak into our atmosphere, which might end up as visible auroras. At nighttime it can take up to two hours traveltime.

This script looks at the constant data coming from the ACE-satellite, recorded in textfiles hosted by the NOAA organization. What we are looking for when evaluating a chance of northern lights is if the magentic field of the solar wind is an opposite of the Earths magnetic field, kind of like two magnets attracting of repel each other when holding them in hour hands. If they attract, it means that the solar winds Bz value is negative and this is what we are looking for.

In addition to that, the solar wind speed will help the chance of more visible auroras, but not as crucial as the magnetic Bz vector. 

Once the magnetic field of hour planet is disturbed by the constant wind blowing from the Sun, magnetometers around the globe will measure the impact and together give an indicator of the disturbances. 

### Planetary K-Index

The K-index, and by extension the *Planetary K-index*, are used to characterize the magnitude of geomagnetic storms. Kp is an excellent indicator of disturbances in the Earth's magnetic field and is used by SWPC to decide whether geomagnetic alerts and warnings need to be issued for users who are affected by these disturbances.

The principal users affected by geomagnetic storms are the electrical power grid, spacecraft operations, users of radio signals that reflect off of or pass through the ionosphere, and observers of the aurora.

It can therefore be useful to be alerted if the K-index reach 4, 5, 6, 7, 8, or 9.

**Data source**: http://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt

Read more at

* http://www.swpc.noaa.gov/products/planetary-k-index)

### Solar wind speed

Higher solar wind speeds and strong south pointing (negative) interplanetary 
magnetic field are associated with geomagnetic disturbances on earth.

* **Data source**: ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_swepam_1m.txt
* **Alternativ source**: http://services.swpc.noaa.gov/products/summary/solar-wind-speed.json

Read more at 

* http://www.sws.bom.gov.au/Solar/1/4
* http://aurorasaurus.org/storm-tracker

### Negative or positive Bz

Higher solar wind speeds and strong south pointing (negative) interplanetary 
magnetic field are associated with geomagnetic disturbances on earth.

* **Data source**: ftp://ftp.swpc.noaa.gov/pub/lists/ace/ace_mag_1m.txt
* **Alternativ source**: http://services.swpc.noaa.gov/products/summary/solar-wind-mag-field.json


## Installation
If you don't have `git` installed, install it first using your distributions package management. If you want to use crontab to email you warnings, install the `mailx` command from `mailutils` package.

Clone into the repository:

```bash
git clone https://gitlab.com/orjanv/Aurora-alert.git
```

Make sure the program is executable:
```bash
sudo chmod a+x forecast.py
``` 


## Running the script

Using the `-f` argument will give you an output if bz is negative and kpi >= 4, 
or if there is a good negative Bz value, which means that there is a chance of aurora.

### Command line arguments

```bash
usage: forecast.py [-h] [-k] [-w] [-b] [-y] [-a] [-r] [-f] [region]

positional arguments:
  region           region in Norway, use -r to show all. Defaults to
                   'Nordland'

optional arguments:
  -h, --help       show this help message and exit
  -k, --kpindex    Planetary K-Index
  -w, --windspeed  Solar Wind Speed
  -b, --bz         Magnetic Bz Value
  -y, --yr         YR data for Nordland
  -a, --all        Show all data
  -r, --regions    Show all available regions, used with -y
  -f, --forecast   Evaluate the chance of aurora
```

### Setup automatic schedule runs with crontab

Make a symbolic link to the program
```bash
sudo ln -s /PATH/TO/Aurora-alert/forecast.py /usr/bin/aurora-forecast
```

Add to your crontab with `crontab -e` to run every whole hour with the following entry:

```bash
0 * * * *	/PATH/TO/check-kp.sh
```

The content of check-kp.sh script run the program with `-f` argument and sends an email (require mailx)

```bash
OUT=$(/usr/bin/aurora-forecast -f)
if (( $OUT )); then
    echo $OUT | mailx -s "Aurora warning" EMAILADDRESS;
fi
``` 

Remember to change the email address in the bash script `check-kp.sh`.
