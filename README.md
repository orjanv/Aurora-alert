## About Planetary K-Index
The K-index, and by extension the *Planetary K-index*, are used to characterize the magnitude of geomagnetic storms. Kp is an excellent indicator of disturbances in the Earth's magnetic field and is used by SWPC to decide whether geomagnetic alerts and warnings need to be issued for users who are affected by these disturbances.

The principal users affected by geomagnetic storms are the electrical power grid, spacecraft operations, users of radio signals that reflect off of or pass through the ionosphere, and observers of the aurora.

It can therefore be useful to be alerted if the K-index reach 4, 5, 6, 7, 8, or 9.

![](http://services.swpc.noaa.gov/images/planetary-k-index.gif "Planetary K-Index at NOAA")

Read more at [NOAA](http://www.swpc.noaa.gov/products/planetary-k-index)s pages.

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
sudo ln -s /PATH/TO/Planetary-K-Index-alert/forecast.py /usr/bin/kp-forecast
```

Add to your crontab to run every hour with the following entry:

```bash
0 * * * *	/PATH/TO/check-kp.sh
```
