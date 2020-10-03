#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("C:\chromedriver") #set the path to chromedriver(wherever it is located) 
browser.get("https://web.whatsapp.com/")   #opens whats app in the browser , scan the QR CODE TO PROCEED.
wait=WebDriverWait(browser,600)     #leave it as it is
target='"my_friend_name"'    #replace the EXACT name of your What's app contact name. 
string="retype your message here"    #this will be your message you want to send
x_arg= '//span[contains(@title, ' +target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box= browser.find_element_by_class_name('_1Plpp')
for i in range(150):    #the number of messages (the message will be sent 150 times)
    input_box.send_keys(string+Keys.ENTER)
