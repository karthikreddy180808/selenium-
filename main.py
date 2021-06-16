import datetime
from time_variance_authority import prune, get_time, time_log
import inator
status_code = 212
time_log()
print("Log:")
print("Initiating automation software...")
while True:
    status_code = prune(get_time(), status_code)
    if status_code == 212:
        continue
    a1 = inator.Automate()
    time_log()
    print("    Trying to login...")
    a1.login()
    print("    Login Confirmed.....")
    print("    Searching for available classes...")
    a1.find_classes()
    print("    Trying to join the most recently opened class (if any)...")
    status_code = a1.join_most_recent_class()
    print("    Have a nice day 😊")
    status_code = prune(get_time(), status_code)
