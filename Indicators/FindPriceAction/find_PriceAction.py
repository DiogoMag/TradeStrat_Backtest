import datetime

now = datetime.datetime.now().time()


# _________________________________________________________ FUNCTIONS #

def find_marketsession(stamp):
    # Convert timestamp to datetime object
    dt = datetime.datetime.fromtimestamp(stamp)
    now = dt.time()

    # Define session start and end times in GMT
    tokyo_start = datetime.time(0, 0)
    tokyo_end = datetime.time(9, 0)

    london_start = datetime.time(8, 0)
    london_end = datetime.time(17, 0)

    newyork_start = datetime.time(13, 0)
    newyork_end = datetime.time(22, 0)

    # Identify the current session
    if tokyo_start <= now < tokyo_end:
        return "Tokyo session"
    elif london_start <= now < london_end:
        return "London session"
    elif newyork_start <= now < newyork_end:
        return "New York session"
    else:
        return "Gap or dead zone"


def find_reversal():
    print('this is a reversal')