import time
import datetime

## get the current timestamp
timestamp = time.time()

# convert timestamp to datetime object
dt_object = datetime.datetime.fromtimestamp(timestamp)

def market_session():
    print(type(dt_object))
    print(type(timestamp))

market_session()