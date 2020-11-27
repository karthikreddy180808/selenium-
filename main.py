import inator
import time_watcher
from collections import namedtuple
print("Thank you for using ClassJoinInator, \n\
please give your feedback at https://docs.google.com/forms/d/e/1FAIpQLSdPCX6swB7Xsg6HsimZZGxsI8Ink1Lj3VqZ4pky3TzCD6yvew/viewform?usp=sf_link \n\n\n")

print("Initiated automation software...")
p1 = inator.Process()
print("Searching for available classes...")
p1.search()
# print("{} classes found".format(len(p1.l_classes)))
# if len(p1.l_classes()) > 0:
#     for i in p1.l_classes:
#         print("{}: {}".format(i[0], i[1]))
#     n = input("Enter class number you want to join: ")
#     try:
#         p1.join_class(p1.l_classes[n][1])
#     except:
#         print("Invalid Option")
p1.join_all_classes()  # FIXME: TO BE DEPRECATED.
# TODO: Implement some control using time_watcher.py file...
# Time = namedtuple("Time", ["Hours, Minutes"])
input("Press Enter to exit.........")
# print("")
# TODO: complete integrations
