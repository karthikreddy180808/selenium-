import discord
import inator
import time
import datetime
import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("https://discord.com/api/webhooks/854651909054398475/IDbosg2Z3zdngXZ2E8OSXWHwDuMaWabzW6_6CN2RGWV7T_TkY40b92Bg7Hsr6gwC0nmR" , adapter=RequestsWebhookAdapter())
flag = True

with open("time_table_II-2.png", "rb") as f:
    tt = discord.File(f)
    f.close()

webhook.send("Initiated automation software at {}".format(datetime.datetime.now()))

webhook.send("cross check with time table" , file = tt)

while(flag):
    hour = int(datetime.datetime.now().strftime("%H"))
    if(hour > 9 and hour < 14): pass
    else: break
    a1 = inator.Automate()
    a1.login()
    webhook.send("Login Confirmed!")
    a1.find_classes()
    a1.join_most_recent_class()
    time.sleep(180)

webhook.send("automation stopped at {}".format(datetime.datetime.now()))

