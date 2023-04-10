import datetime
import pytz
import os


os.system('cls')

def find_marketsession(stamp):
    
    # Convert timestamp to datetime object in UTC
    dt_utc = datetime.datetime.utcfromtimestamp(stamp)

    # Convert UTC datetime object to London timezone datetime object
    london_tz = pytz.timezone('Europe/London')
    dt_london = dt_utc.replace(tzinfo=pytz.utc).astimezone(london_tz)

    # Define session start and end times in London timezone

    newyork_start = datetime.time(13, 0)
    newyork_end = datetime.time(22, 0)

    london_start = datetime.time(8, 0)
    london_end = datetime.time(17, 0)

    asia_start = datetime.time(1, 0)
    asia_end = datetime.time(9, 0)

    sidney_start = datetime.time(22, 0)
    sidney_end = datetime.time(7, 0)

    deadzone_start = datetime.time(22, 0)
    deadzone_end = datetime.time(1, 0)

    # Determine which market sessions the timestamp falls within
    session_list = []
    if newyork_start <= dt_london.time() <= newyork_end:
        session_list.append("New York")
    if london_start <= dt_london.time() <= london_end:
        session_list.append("London")
    if asia_start <= dt_london.time() <= asia_end:
        session_list.append("Asia")
    if sidney_start <= dt_london.time() <= datetime.time(23, 59, 59) or dt_london.time() <= sidney_end:
        session_list.append("Sydney")
    if deadzone_start <= dt_london.time() <= datetime.time(23, 59, 59) or dt_london.time() <= deadzone_end:
        session_list.append("Dead Zone")

    return session_list


def find_reversal():
    print('this is a reversal')
