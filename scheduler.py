import datetime
hour_play_begin = 15 
hour_play_end = 21

def time_to_play():
    hour = int(datetime.datetime.now().strftime("%H"))
    day = datetime.datetime.now().strftime("%a")
    if day == 'Fri': 
        if hour >= 15:
            return True
    if day == 'Sat':
        return True
    if day == 'Sun':
        if hour < 21:
            return True
    return False

if __name__ == "__main__":
    print(time_to_play())