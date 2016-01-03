## Install

1. If you don't have ```bash git``` installed, install it as well as the ```bash mailx``` command from ```bash mailutils``` package using your distributions package management.
2. Make sure the program is executable:
```bash
sudo chmod a+x forecast.py
``` 
3. Make a symbolic link to the program
```bash
sudo ln -s /PATH_TO_Planetary-K-Index-alert/forecast.py /usr/bin/kp-forecast
```
4. Add to your crontab to run every hour with the following entry:

```bash
0 * * * *	if OUT="$(kp-forecast)"; then echo $OUT | mailx -s "Planetary K-Index Alert" orjanv@gmail.com; fi
```
