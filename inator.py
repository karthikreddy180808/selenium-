from selenium import webdriver
import selenium
import datetime
from selenium.common.exceptions import NoSuchElementException

hour = int(datetime.datetime.now().strftime("%H"))


class Automate:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome("C:\\Users\\saish\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://ngitonline.com")
        self.classes = {}

    def login(self):
        username = self.driver.find_element_by_id("username")
        username.send_keys("")  # your id
        password = self.driver.find_element_by_id("password")
        password.send_keys("")  # your password
        login_button = self.driver.find_element_by_id("loginbtn")
        login_button.click()

    def find_classes(self):
        for i in range(1, 30):
            try:
                path = "/html/body/div[2]/div/section/div/div/div/div[{}]/".format(i)
                # print(path)
                # /html/body/div[2]/div/section/div/div/div/div[1]/div[3]/a/span
                print(self.driver.find_element_by_xpath(path + "div[3]/a/span").text)
                if self.driver.find_element_by_xpath(path + "div[3]/a/span").text == "JOIN":
                    self.classes[self.driver.find_element_by_xpath(
                        path + "div[2]/header/h2").text] = \
                        [self.driver.find_element_by_xpath(path + "div[3]/a"),
                         int((self.driver.find_element_by_xpath(
                             "/html/body/div[2]/div/section/div/div/div/div[1]/div[2]/header/span/div/span[1]").text[-7]
                             ).strip())]

            except NoSuchElementException:
                pass

    def display(self):  # Note: TO BE DEPRECATED
        print(self.classes.keys())

    def join_class(self, class_name):  # Note: TO BE DEPRECATED
        for i in self.classes.keys():
            if class_name in i:
                self.classes[i].click()

    def join_all_possible_classes(self):  # Note: TO BE DEPRECATED
        for i in self.classes.keys():  # Note: Include a standard process rather than click all software.
            self.classes[i].click()

    def join_most_recent_class(self):
        if len(self.classes.keys()) > 1:
            priority_list = sorted(self.classes.items(), key=lambda x: hour - x[1][1])
            priority_list[0][1][0].click()
            return
        list(self.classes.items())[0][1][0].click()

# Below lines: TO BE DEPRECATED
# a1 = Automate()
# a1.login()
# a1.find_classes()
# a1.join_most_recent_class()
# a1.display()
