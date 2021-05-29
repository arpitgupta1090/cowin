import requests
import json
import datetime
import time
from playsound import playsound


def find_slot(pin_code, date_time, age=18):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" \
          + pin_code + "&date=" + date_time
    headers = {
        "Accept-Language": "en_US",
        "accept": "application/json"
    }
    res = requests.get(url, headers=headers)
    resp = res.text
    resp = json.loads(resp)
    centers = resp['centers']

    if (len(centers)) == 0:
        print("No Slots for next 7 days")
        return False
    for i in centers:
        for j in i['sessions']:
            if j['min_age_limit'] == age:
                print("Number of Slot at", i['name'], "are", j['available_capacity'])
                if j['available_capacity'] > 0:
                    playsound('sound.wav')


today = datetime.datetime.today()
nextDay = datetime.datetime.today() + datetime.timedelta(days=1)
date_time_today = today.strftime("%d-%m-%Y")
date_time_nextDay = nextDay.strftime("%d-%m-%Y")

while True:
    pin_codes = ["400703", "400705", "400710", "400614", "400701"]
    print(date_time_today)
    for pin in pin_codes:
        find_slot(pin, date_time_nextDay, 18)
    time.sleep(120)
