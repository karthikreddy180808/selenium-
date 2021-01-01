import inator
print("Thank you for using ClassJoinInator, \n\
please give your feedback at https://docs.google.com/forms/d/e/1FAIpQLSdPCX6swB7Xsg6HsimZZGxsI8Ink1Lj3VqZ4pky3TzCD6yvew/viewform?usp=sf_link \n\n\n")

print("Initiated automation software...")
a1 = inator.Automate()
print("Trying to login...")
a1.login()
print("Login Confirmed.....")
print("Searching for available classes...")
a1.find_classes()
print("Trying to join the most recently opened class (if any)...")
a1.join_most_recent_class()
print("Have a nice day 😊")
