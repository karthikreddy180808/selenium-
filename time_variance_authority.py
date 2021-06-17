from time import sleep
from datetime import datetime


def time_log():
    d = datetime.now()
    h, m = map(int, (d.strftime("%H"), d.strftime("%M")))
    print("Log at {} hours and {} minutes".format(h, m))


def get_time():
    d = datetime.now()
    return d.strftime("%H"), d.strftime("%M")


def nexus_checker(time):
    class_hour, class_minute, orig_hour, orig_minute = map(int, time)
    if class_hour < 9:
        class_hour += 12
    return abs((orig_hour * 60 + orig_minute) - (class_hour * 60 + class_minute))


def prune(time, status_code):
    hour, minute = map(int, time)
    status_messages = {404: "No classes found will keep checking again in 3 minutes",
                       212: "TVA is monitoring timelines, checking again in 40 minutes",
                       200: "All good, waiting for class to end"}
    if hour < 8 or hour >= 16:
        print(status_messages[212])
        sleep(2400)
        return 212
    elif 8 <= hour <= 9:
        print(status_messages[212])
        sleep(60 - minute)
        return 212
    if status_code == 404:
        print(status_messages[404])
        sleep(180)
        return 404
    elif status_code == 200:
        print(status_messages[200])
        if minute <= 40:
            sleep(40-minute)
        else:
            sleep(60-minute)
        return 200
