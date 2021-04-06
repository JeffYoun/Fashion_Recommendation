from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import os
import time
import urllib.request

# String that you want an image of
imageName = str()
pathName = str()
MAX_IMAGE_NUM = int()

def crawl():
    # Make directory to gather download images, in this case make folder with name SEARCH_STRING in Downloads folder
    try:
        dirName = pathName + "/" + imageName
        os.makedirs(dirName)
    except OSError as error:
        print("Directory already exists")

    # Set Chromedriver Path
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)
    driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))

    # Open Chrome and search image you want
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(imageName)
    elem.send_keys(Keys.RETURN)

    # Scroll down to the bottom so you load all the images beforehand
    scrollCount = 0
    maxScroll = MAX_IMAGE_NUM / 40
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight") # Get scroll bar height
    while scrollCount < maxScroll:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down to bottom
        time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
        new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height and compare with last scroll height
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
                scrollCount += 1
            except:
                break
        last_height = new_height

    # download images
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 0
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
