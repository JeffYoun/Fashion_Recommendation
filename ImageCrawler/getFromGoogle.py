from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib.request

# String that you want an image of
SEARCH_STRING = input("I want images of : ")

# Make directory to gather download images, in this case make folder with name SEARCH_STRING in Downloads folder
try:
    dirName = "C:/Users/Jeff/Downloads/" + SEARCH_STRING
    os.makedirs(dirName)
except OSError as error:
    print("Directory already exists")

# Open Chrome and search image you want
driver = webdriver.Chrome("C:/Users/Jeff/Documents/selenium/chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(SEARCH_STRING)
elem.send_keys(Keys.RETURN)

# # Scroll down to the bottom so you load all the images beforehand
# scrollCount = 0;
# maxScroll = 5;
# SCROLL_PAUSE_TIME = 2
# last_height = driver.execute_script("return document.body.scrollHeight") # Get scroll bar height
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down to bottom
#     time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
#     new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height and compare with last scroll height
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height

# download images
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
MAX_IMAGE_NUM = 5 # Number of maximum images you want to download
for image in images:
    if count < MAX_IMAGE_NUM:
        try:
            image.click()
            time.sleep(3)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            urllib.request.urlretrieve(imgUrl, dirName+"/"+str(count)+".jpg")
            count += 1
        except:
            count += 1
            pass
    else:
        break

driver.close()
