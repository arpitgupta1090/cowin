# cowin

A simple python function thats calls Govenment's ApiSethu Cowin portal to get available vaccine slots near you.
It takes a list of pincode and age(18/45) as input and provides a list of hospital and number of slots available for that age group in the area mentioned in pincodes.
It also generated a alarm sound whenever there is availability. 

## Usage

```python
import requests
import json
import datetime
import time

from playsound import playsound
today = datetime.datetime.today()
nextDay = datetime.datetime.today() + datetime.timedelta(days=1)
date_time_today = today.strftime("%d-%m-%Y")
date_time_nextDay = nextDay.strftime("%d-%m-%Y")

while True:
    pin_codes = ["400703", "400705", "400710", "400614", "400701"]
    print(date_time_nextDay)
    for pin in pin_codes:
        find_slot(pin, date_time_nextDay, 18)
    time.sleep(120)
```

