from selenium import webdriver
from selenium.webdriver.common.by import By
import _thread
import asyncio
import time
from selenium.webdriver.chrome.service import Service

thislist = []

async def open_browser():
  for item in range(2):
      s=Service("/Users/kinglongkwan/Documents/GitHub/python/chromedriver")
      browser = webdriver.Chrome(service=s)
      browser.get("https://ticket.urbtix.hk/internet/zh_TW/eventDetail/43919") # 更改網址以前往不同網頁
      thislist.append(browser)
      open_addened_browser()

def open_addened_browser():
   for browser in thislist:
      element = browser.find_element(By.CLASS_NAME,"perf-purchase-img.cursor-pointer")

#thread1 = open_browser()
#thread2 = open_browser()
print("prepare to start thread")
try:
   loop = asyncio.new_event_loop()
   asyncio.set_event_loop(loop)
   loop.run_until_complete(open_browser())
   loop.close()
except:
   print ("Error: unable to start thread")

while 1:
   pass
