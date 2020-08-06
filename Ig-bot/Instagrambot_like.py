from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        b.send_keys(Keys.RETURN)
        # self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        
    def nav_page(self, page):
        time.sleep(1)
        self.driver.get('{}/explore/tags/{}/'.format(self.base_url, page))


    def like_photo(self,hastag):
        driver = self.driver
        self.nav_page(hastag)
        time.sleep(4)
        pic_hrefs=[]
        for i in range(1,4):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [ele.get_attribute('href') for ele in hrefs if'.com/p/' in ele.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue
            
        unique_photos = len(pic_hrefs)
        print("Unique pics count for ", hastag, str(unique_photos))

        
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                # time.sleep(1)
                ele = driver.find_element_by_css_selector(".fr66n ._8-yf5")
                attr = ele.get_attribute('aria-label')
                if (attr=='Like'):
                    ele.click()
                    global like_count
                    like_count += 1
                
                # for second in reversed(range(0, random.randint(18, 28))):
                #     print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                #                     + " | Sleeping " + str(second))
                #     time.sleep(1)

            except Exception as e:
                time.sleep(2)
            

         
if __name__ == '__main__':
    global like_count
    like_count = 0

    ig_bot=InstaBot('info@fhplusnutrition.in','dev12345')
    #
    hastags = ['healthylifestyle', 'healthylifestyle', 'HealthyLiving', 'vitamins', 'fitness', 'nutrition',
               'supplements', 'indore', 'nutrients', 'VitaminC', 'VitaminD', 'childcare', 'hyderabad']


    for hastag in hastags:
        print("Currently liking content for: ", hastag)
        ig_bot.like_photo(hastag)

    print("total likes in this session are ", like_count)

