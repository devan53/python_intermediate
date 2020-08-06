import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = 'https://twitter.com'

        self.login()

    def login(self):
        self.driver.get('{}/login/'.format(self.base_url))
        time.sleep(5)
        a = self.driver.find_element_by_name("session[username_or_email]")
        a.clear()
        a.send_keys(self.username)
        ##a.send_keys(Keys.RETURN)
        b = self.driver.find_element_by_name("session[password]")
        b.clear()
        b.send_keys(self.password)
        b.send_keys(Keys.RETURN)
        # self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]").click()

    def nav_page(self, page):
        time.sleep(1)
        self.driver.get('{}/search?q=%23{}&src=recent_search_click&f=live'.format(self.base_url, page))

    def like_tweet(self, hastag):
        driver = self.driver
        self.nav_page(hastag)
        time.sleep(2)
        # pic_hrefs=[]
        tweet_hrefs = []
        for i in range(1, 4):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [ele.get_attribute('href') for ele in hrefs if '/status/' in ele.get_attribute('href')]
                [tweet_hrefs.append(href) for href in hrefs_in_view if href not in tweet_hrefs]
            except Exception:
                continue

        unique_tweets = len(tweet_hrefs)
        print("Unique tweets to like is %s" % str(unique_tweets))

        for tweet_href in tweet_hrefs:
            driver.get(tweet_href)
            time.sleep(1)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                time.sleep(2)
                ele = driver.find_element_by_css_selector(".r-rjfia:nth-child(3) .r-bztko3")
                attr = ele.get_attribute('aria-label')
                if (attr == 'Like'):
                    ele.click()
                    global like_count
                    like_count += 1

                # for second in reversed(range(0, random.randint(18, 28))):
                #     print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                #                     + " | Sleeping " + str(second))
                #     time.sleep(1)
            except Exception:
                time.sleep(2)

        driver.close()


if __name__ == '__main__':
    global like_count
    like_count = 0
    #'nutrients', 'VitaminC',
    hastags = ['VitaminD', 'hyderabad', 'healthylifestyle', 'KidsDeserveIt', 'indore',
               'HealthyLiving', 'vitamins', 'childnutrition', 'immunitybooster', 'fitness', 'nutrition', 'supplements',
               'HealthyEating']

    for hastag in hastags:
        tweeter_bot = TwitterBot('8962898046', 'dev12345')
        print("Currently running likes for %s" %hastag)
        tweeter_bot.like_tweet(hastag)
        time.sleep(100)

    print("total likes in this session are ", like_count)
