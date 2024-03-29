from selenium import webdriver
import datetime
import time as t
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import requests
from discord import Webhook, RequestsWebhookAdapter

hour = int(datetime.datetime.now().strftime("%H"))
minute = int(datetime.datetime.now().strftime("%M"))
webhook = Webhook.from_url("https://discord.com/api/webhooks/854651909054398475/IDbosg2Z3zdngXZ2E8OSXWHwDuMaWabzW6_6CN2RGWV7T_TkY40b92Bg7Hsr6gwC0nmR" , adapter=RequestsWebhookAdapter())


class Automate:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=/Users/karthikreddy/Library/Application Support/Google/Chrome/Default')
        options.add_argument('--profile-directory=Default')
        self.driver = webdriver.Chrome("/Users/karthikreddy/PycharmProjects/pythonProject/classjoinator/chromedriver" , options= options)
        self.driver.get("http://ngitonline.com")
        self.classes = {}

    def nexus_checker(t):
        class_hour, class_minute, orig_hour, orig_minute = map(int, t)
        if class_hour < 9:
            class_hour += 12
        return abs((orig_hour * 60 + orig_minute) - (class_hour * 60 + class_minute))

    def login(self):
        try:
            print("Getting credentials from saved file...")
            with open("/Users/karthikreddy/PycharmProjects/pythonProject/classjoinator/credentiatls.txt", "r") as f:
                creds = f.readline()
                saved_username = creds[:8]
                saved_password = creds[8:]
            f.close()

        except FileNotFoundError:
            print("\n Its your first time using this console app, please enter your credentials below (needed only "
                  "once) they will be stored in Public user folder")
            with open("/Users/karthikreddy/PycharmProjects/pythonProject/classjoinator/credentiatls.txt", "w") as f:
                new_username = input("Username: ")
                new_password = input("Password: ")
                f.write(new_username)
                f.write(new_password)
                saved_username, saved_password = new_username, new_password
            f.close()

        username = self.driver.find_element_by_id("username")
        username.send_keys(saved_username)  # your id
        password = self.driver.find_element_by_id("password")
        password.send_keys(saved_password)  # your password
        login_button = self.driver.find_element_by_id("loginbtn")
        login_button.click()

    def find_classes(self):
        def collector():
            self.classes[self.driver.find_element_by_xpath(
                path + "div[2]/header/h2").text] = \
                [self.driver.find_element_by_xpath(path + "div[3]/a"),
                 self.driver.find_element_by_xpath(
                     path + "div[2]/header/span/div/span[1]"
                            "").text[-8:-3].strip().split(":")]

        for i in range(1, 30):
            path = "/html/body/div[2]/div/section/div/div/div/div[{}]/".format(i)
            try:
                if self.driver.find_element_by_xpath(path + "div[3]/a/span").text == "JOIN":
                    collector()
            except NoSuchElementException:
                try:
                    if self.driver.find_element_by_xpath(path + "div[3]/form/a/span").text == "JOIN":
                        collector()
                except NoSuchElementException:
                    pass


    def join_most_recent_class(self):
        if len(self.classes.keys()) > 1:
            priority_list = sorted(self.classes.items(),
                                   key=lambda x: nexus_checker(
                                       (x[1][1][0], x[1][1][1], hour, minute)
                                   ))
            priority_list[0][1][0].click()
            webhook.send("Joined {} class, now don't doze off!!".format(priority_list[0][0]))
            sleep(300)
            self.driver.quit()
            sleep(2000)
            return

        elif len(self.classes.keys()) == 1:
            list(self.classes.items())[0][1][0].click()
            webhook.send("Joined {} class, now don't doze off!!".format(list(self.classes.keys())[0]))
            sleep(300)
            self.driver.quit()
            sleep(2000)
            return
        else:
            webhook.send("no classes at present. maybe i'm malfunctioning check manually!")
            sleep(5)
            self.driver.quit()
            return
