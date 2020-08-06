from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.base_url = 'https://www.instagram.com'

        self.login()

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(5)
        a= self.driver.find_element_by_name("username")
        a.clear()
        a.send_keys(self.username)
        a.send_keys(Keys.RETURN)
        b= self.driver.find_element_by_name("password")
        b.clear()
        b.send_keys(self.password)
        ##b.send_keys(Keys.RETURN)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        
    def nav_user(self,user):
        time.sleep(5)
        self.driver.get('{}/{}/'.format(self.base_url,user))

    def follow_user(self,user):

        self.nav_user(user)
        follow = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")
        print(follow)
        follow[0].click()


         
if __name__ == '__main__':
    ig_bot=InstaBot('singhdk2007','dev@12345')
    ig_bot.follow_user('alluarjunonline')
