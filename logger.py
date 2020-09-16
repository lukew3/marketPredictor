import requests
import json
import csv
import threading
import sched, time
from db import BTCUSDT, session

s = sched.scheduler(time.time, time.sleep)

def main():
    s.enter(0, 1, add_price, argument=(0,))
    s.run()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

def add_price(lastPrice):
    response = requests.get("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m")

    fetchTime = response.json()[0][0]
    openPrice = response.json()[0][1]
    highPrice = response.json()[0][2]
    lowPrice = response.json()[0][3]
    closePrice = response.json()[0][4]
    volume = response.json()[0][5]

    print(closePrice)

    newentry = BTCUSDT(
        datetime=fetchTime,
        open=openPrice,
        close=closePrice,
        low=lowPrice,
        high=highPrice,
        volume=volume
    )
    session.add(newentry)
    session.commit()

    s.enter(60, 1, add_price,argument=(lastPrice,)) #run function again in 1 minute

if __name__ == "__main__":
    main()
