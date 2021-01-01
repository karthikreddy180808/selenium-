from selenium import webdriver
import selenium
import datetime
from selenium.common.exceptions import NoSuchElementException

hour = int(datetime.datetime.now().strftime("%H"))


class Automate:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome("chromedriver.exe")
        self.driver.get("http://ngitonline.com")
        self.classes = {}

    def login(self):
        try:
            print("Getting credentials from saved file...")
            with open("C:\\Users\\Public\\credentials.txt", "r") as f:
                creds = f.readline()
                UserName = creds[:8]
                PassWord = creds[8:]
            f.close()
        except FileNotFoundError:
            print("\n Its your first time using this console app, please enter your credentials below (needed only "
                  "once) they will be stored in Public user folder")
            with open("C:\\Users\\Public\\credentials.txt", "w") as f:
                UserName = input("Username: ")
                PassWord = input("Password: ")
                f.write(UserName)
                f.write(PassWord)
            f.close()

        username = self.driver.find_element_by_id("username")
        username.send_keys(UserName)  # your id
        password = self.driver.find_element_by_id("password")
        password.send_keys(PassWord)  # your password
        login_button = self.driver.find_element_by_id("loginbtn")
        login_button.click()

    def find_classes(self):
        for i in range(1, 30):
            try:
                path = "/html/body/div[2]/div/section/div/div/div/div[{}]/".format(i)
                if self.driver.find_element_by_xpath(path + "div[3]/a/span").text == "JOIN":
                    self.classes[self.driver.find_element_by_xpath(
                        path + "div[2]/header/h2").text] = \
                        [self.driver.find_element_by_xpath(path + "div[3]/a"),
                         int((self.driver.find_element_by_xpath(
                             "/html/body/div[2]/div/section/div/div/div/div[1]/div[2]/header/span/div/span[1]").text[-7]
                             ).strip())]

            except NoSuchElementException:
                pass

    def join_most_recent_class(self):
        if len(self.classes.keys()) > 1:
            priority_list = sorted(self.classes.items(), key=lambda x: hour - x[1][1])
            priority_list[0][1][0].click()
            return
        if len(self.classes.keys()) == 1:
            list(self.classes.items())[0][1][0].click()
        print("No classes found, please check manually otherwise just sleep ZZZZZZZZZZZZZZZZZZ")
