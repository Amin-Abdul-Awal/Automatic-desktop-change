"""
this is not done, this will be continues when I have more knowledge on selenium.
"""

from selenium import webdriver
import time


class MessageSender:

    def __init__(self, contact, message):
        self.message = message
        self.contact = contact
        self.driver = webdriver.Chrome("chromedriver.exe")

    def WriteMessage(self):
        self.driver.get("https://web.whatsapp.com/")

        try:
            xPath=f'//span[@title = "{self.contact}"]'
            user =self.driver.find_element_by_xpath(xPath)
            user.click()

        except:
            self.Writemessage()

        textBox=self.driver.find_element_by_class_name("DuUXI")
        textBox.click()
        textBox.send_keys(self.message,1)
        
        time.sleep(1)

        #button = self.driver.find_element_by_class_name("_2Ujuu")
        #button.click()
        self.driver.close()





    def sendmessage(self, counter):
        print("write message")
        self.WriteMessage()
        time.sleep(1)
        print("message sent")


time.sleep(5)
message=MessageSender("+44 7419 362308","testing 1\n")
message.sendmessage(1)





