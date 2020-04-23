#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
browser = webdriver.Chrome("C:\chromedriver")  #set the path to chrome-driver
browser.get("https://www.google.com")  #this will open the url

# elem= browser.find_element_by_link_text("Download")   this will find all the links in the website
#elem.click()


# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("C:\chromedriver") 
browser.get("https://web.whatsapp.com/")
wait=WebDriverWait(browser,600)
target='"Jaggu"'    #replace the EXACT name of your What's app contact name. 
string="alright"    #this will be your message you want to send
x_arg= '//span[contains(@title, ' +target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box= browser.find_element_by_class_name('_1Plpp')
for i in range(150):
    input_box.send_keys(string+Keys.ENTER)


# In[ ]:




