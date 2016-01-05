#!/bin/bash
# Script to be used in crontab
# part of https://github.com/orjanv/Planetary-K-Index-alert
# 
OUT=$(/usr/bin/kp-forecast)
if (( $OUT )); then
    echo $OUT | mailx -s "Planetary K-Index Alert" user@host.com;
fi
