import datetime

def identify_session(tempo_str):
    # convert tempo_str to datetime.time object
    try:
        tempo = datetime.datetime.strptime(tempo_str, '%H:%M:%S').time()
    except ValueError:
        tempo = datetime.datetime.strptime(tempo_str, '%H:%M').time()

    # define time ranges and corresponding session values
    time_ranges = [
        (datetime.time(hour=13), datetime.time(hour=22), 'NewYork'),
        (datetime.time(hour=7), datetime.time(hour=16), 'London'),
        (datetime.time(hour=0), datetime.time(hour=9), 'Tokyo'),
        (datetime.time(hour=0), datetime.time(hour=6), 'Sidney'),
    ]
    
    # initialize session to an empty string
    session = ""
    
    # check if the tempo is within any of the time ranges and concatenate session values if needed
    for start_time, end_time, session_val in time_ranges:
        if start_time <= tempo <= end_time:
            if session == "":
                session = session_val
            else:
                session += f",{session_val}"
    
    return session




print(identify_session('08:00:00'))