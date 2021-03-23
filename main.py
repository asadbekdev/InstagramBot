from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        PATH = "./chromedriver"
        
        self.bot = webdriver.Chrome(PATH)

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        info = bot.find_element_by_class_name('yWX7d').click()
        time.sleep(3)
        notify = bot.find_element_by_class_name('HoLwm').click()
    
    def searchHashtags(self,hashtag):
        bot = self.bot
        bot.get('https://instagram.com/explore/tags/' + hashtag)

    def like_Posts(self,likeNums):
        bot = self.bot
        bot.find_element_by_class_name('v1Nh3').click()
        
        i = 0
        while i <= likeNums:
            time.sleep(2)
            bot.find_element_by_class_name('fr66n').click()
            time.sleep(3)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i += 1

        bot.get('https://instagram.com/' + self.username)
        
asadbek = InstagramBot("username","password")
asadbek.login()
asadbek.searchHashtags('python') #hashtag
asadbek.like_Posts(5) #number of posts you want to like