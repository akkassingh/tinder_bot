from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        privacy_policy_btn = self.driver.find_element(By.XPATH, '//*[@id="s-522567612"]/div/div[2]/div/div/div[1]/div[1]/button')
        privacy_policy_btn.click()

        main_login_btn = self.driver.find_element(By.XPATH, '//*[@id="s-522567612"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
        main_login_btn.click()

        fb_login_btn = self.driver.find_element(By.XPATH, '//*[@id="s2044018608"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        fb_login_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to.window(self.driver.window_handles[1])
        
        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_in.send_keys('akkassingh@gmail.com')

        pwd_in = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pwd_in.send_keys('Password')

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="u_0_0_fm"]')
        login_btn.click()