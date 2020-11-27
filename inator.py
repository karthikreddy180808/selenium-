from selenium import webdriver
import selenium
import datetime

day = datetime.datetime.now().strftime("%d")


class Automate:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome("C:\\Users\\saish\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://ngitonline.com")
        self.classes = {}

    def login(self):
        username = self.driver.find_element_by_id("username")
        username.send_keys(19733020)  # your id
        password = self.driver.find_element_by_id("password")
        password.send_keys("6pZQJehB")  # your password
        login_button = self.driver.find_element_by_id("loginbtn")
        login_button.click()

    def find_classes(self):
        for i in range(1, 30):
            try:
                path = "/html/body/div[2]/div/section/div/div/div/div[{}]/".format(i)
                # print(path)
                self.classes[self.driver.find_element_by_xpath(
                    path + "div[2]/header/h2".format(
                        i)).text] = self.driver.find_element_by_xpath(
                    path + "div[3]/form/a")
            except:  # TODO: find reasonable exception pass i.e A type for exception
                pass

    def display(self):
        print(self.classes.keys())

    def join_class(self, class_name):
        for i in self.classes.keys():
            if class_name in i:
                self.classes[i].click()

    def join_all_possible_classes(self):  # FIXME: TO BE DEPRECATED
        for i in self.classes.keys():     # Note: Include a standard process rather than click all software.
            self.classes[i].click()


class Process:
    def __init__(self) -> None:
        self.a1 = Automate()
        self.a1.login()
        self.l_classes = 0

    def search(self):
        self.a1.find_classes()
        l1 = list(self.a1.classes)
        l1 = list(enumerate(l))
        self.l_classes = l1

    def join_class(self, class_name):
        self.a1.join_class(class_name=class_name)

    def join_all_classes(self):
        self.a1.join_all_possible_classes()
# TODO: A segregation system based on time and date.
