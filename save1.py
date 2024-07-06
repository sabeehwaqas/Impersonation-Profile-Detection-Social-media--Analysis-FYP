from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

import time





def enter_user(user,depth):
    options = Options()
    time1 = 3
    time2=5
    options.headless = True
    path = 'C:\chromedriver.exe'
    depth=depth+1
    userr1 = user #input("enter username: ")
#    browser=utils.init_driver(headless=True)
    browser = webdriver.Chrome(path,options = options)
    
    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    
    for i in range(1,depth):
        try:
            time.sleep(time1)
            #print("========================================")
            follo = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div')))
            following = follo.text
        except Exception as e:
                print("oiushfiafhbfaoiahoiahioadfhvoiroiuGADIFOVBI")
                ass=1
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        with open('new.txt','a',encoding="utf-8") as g:
            g.write(following)

    
    browser.close()
    browser.quit()
    
    
    g.close()
   


