#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
#Other imports here
import os
import wget

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome('D:/Software/python/chromedriver_win32/chromedriver_win32/chromedriver.exe', options=options)
driver.get('https://www.instagram.com/')

username = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys("username")
password.send_keys("Password")

log_in = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# avatar = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[1]/div[2]/div/div/div/div/ul/li[3]/div""").click()

time.sleep(3)

explore = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/a/div"""))).click()

i = 0
while i <= 100:
    explore = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[1]/div[2]"""))).click()
    time.sleep(3)
    like = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"""))).click()
    time.sleep(3)
    Next = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"""))).click()
    time.sleep(3)
    # puse = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/header/div[2]/div[2]/button[1]"""))).click()
    # time.sleep(10)
    # like = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[2]/span/button"""))).click()
    # Next = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]"""))).click()
    # time.sleep(3)
    # i += 1
    i = i + 1