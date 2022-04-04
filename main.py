from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service('/Users/shakayahaya/Desktop/chromedriver')
driver = webdriver.Chrome(service=s)
URL = "https://www.linkedin.com/jobs/search/?currentJobId=2549682805&f_LF=f_AL&geoId=90009606&keywords=python" \
      "%20developer&location=Stockholm%20Metropolitan%20Area "
driver.get(URL)


def sign_in_linkedin():
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, 'Sign in').click()
    email = driver.find_element(By.NAME, 'session_key')
    password = driver.find_element(By.NAME, 'session_password')
    email.send_keys('shakayahaya4@gmail.com')
    password.send_keys('childofgod1')


sign_in_linkedin()


def easy_apply():
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'form button').click()
    time.sleep(3)
    next_two = driver.find_elements(By.CSS_SELECTOR, 'form button')
    time.sleep(3)
    next_two[3].click()


easy_apply()
