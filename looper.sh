#!/bin/bash

while true; do
	echo "`date`: Running check"
	python scraper.py
	sleeptime=$(shuf -i 500-1000 -n 1)
	echo "Will sleep for $sleeptime seconds..."
	sleep $sleeptime
done
