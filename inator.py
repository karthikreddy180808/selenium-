from selenium import webdriver
import datetime
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from discord import Webhook, RequestsWebhookAdapter
from time_variance_authority import nexus_checker

hour = int(datetime.datetime.now().strftime("%H"))
minute = int(datetime.datetime.now().strftime("%M"))


class Automate:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=C:\\Users\\saish\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        options.add_argument("--profile-directory=Default")
        self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        self.driver.get("http://ngitonline.com")
        self.classes = {}
        self.message = ""
        self.status_code = 0
        self.discord_webhook = Webhook.from_url(url="https://discord.com/api/webhooks/854680810758340608"
                                                    "/lFaIFitzQPQnf1P_ar8UiAeBPzb_06ImAoA_JMRIY7Ll2MgoV74FaiWCi_jT3Q_ik603",
                                                adapter=RequestsWebhookAdapter())

    def login(self):
        try:
            print("    Getting credentials from saved file...")
            with open("C:\\Users\\Public\\credentials.txt", "r") as f:
                creds = f.readline()
                saved_username = creds[:8]
                saved_password = creds[8:]
            f.close()

        except FileNotFoundError:
            print("\n Its your first time using this console app, please enter your credentials below (needed only "
                  "once) they will be stored in Public user folder")
            with open("C:\\Users\\Public\\credentials.txt", "w") as f:
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
            self.message = "Joined {} class, now don't doze off!!".format(priority_list[0][0])
            self.status_code = 200
        elif len(self.classes.keys()) == 1:
            list(self.classes.items())[0][1][0].click()
            self.message = "Joined {} class, now don't doze off!!".format(list(self.classes.keys())[0])
            self.status_code = 200
        else:
            self.message = "No classes found, please check manually or just sleep ZZZZZZZZZZ"
            self.status_code = 404

        self.discord_webhook.send(self.message)
        sleep(10)
        # self.driver.quit() // To be deprecated
        return self.status_code
