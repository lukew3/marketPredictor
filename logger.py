import requests
import json
import csv
import threading
import sched, time

s = sched.scheduler(time.time, time.sleep)

def main():
    with open('bitcoinEachMinute.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Datetime", "Price", "Delta"])
    s.enter(0, 1, add_price, argument=(0,))
    s.run()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())



def add_price(lastPrice):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = response.json()['bpi']['USD']['rate_float']
    fetchTime = response.json()['time']['updated']

    if lastPrice == 0:
        delta = 0
    else:
        delta = lastPrice - price
    lastPrice = price

    print(price)
    print(fetchTime)

    with open('bitcoinEachMinute.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([fetchTime, price, delta])

    s.enter(60, 1, add_price,argument=(lastPrice,)) #run function again in 1 minute

if __name__ == "__main__":
    main()
