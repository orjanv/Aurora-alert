#!/bin/bash
# Script to be used in crontab, requires mailutils
# part of https://github.com/orjanv/Aurora-alert
#
OUT=$(/usr/bin/aurora-forecast -f)
if (( $OUT )); then
    echo $OUT | mailx -s "Aurora warning" EMAILADDRESS;
fi
