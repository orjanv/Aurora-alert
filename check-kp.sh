#!/bin/bash
# Script to be used in crontab
# part of https://github.com/orjanv/Planetary-K-Index-alert
# 
OUT=$(/usr/bin/aurora-forecast -f)
if (( $OUT )); then
    echo $OUT | mailx -s "Aurora warning" EMAILADDRESS;
fi
