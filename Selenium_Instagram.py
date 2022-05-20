# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#Warnings settings
import warnings
warnings.filterwarnings("ignore")


# %%
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/tom-w/Tools/chromedriver_win32/chromedriver.exe')

#open the webpage
driver.get("http://www.instagram.com")

#Deny Cookies
cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nur erforderliche Cookies erlauben")]'))).click()


# %%
#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("willetho3114")
password.clear()
password.send_keys("Projektarbeit2022$")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

print('Login successfull!')


# %%
#Login-Inoformationen speichern, Button "Jetzt nicht" 
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Jetzt nicht")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Jetzt nicht")]'))).click()


# %%
import time

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Suchen']")))
searchbox.clear()

#search for the hashtag
keyword = "#DevOps"
searchbox.send_keys(keyword)
 
# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)


# %%
#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

print('Number of scraped images: ', len(images))


# %%
#first we'll create a new folder for our images somewhere on our computer.
#then, we'll save all the images there.

import os
import wget

path = os.getcwd()
path = os.path.join(path, keyword[1:])

#create the directory
os.mkdir(path)

path


# %%
#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1