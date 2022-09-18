from selenium import webdriver
from selenium.webdriver.common.by import By

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
thislist = []

# 定位搜尋框
for item in range(3):
    driver = webdriver.Chrome("/Users/kinglongkwan/Documents/GitHub/python/chromedriver")
    driver.get("https://ticket.urbtix.hk/internet/zh_TW/eventDetail/43919") # 更改網址以前往不同網頁
    thislist.append(driver)

for driver in thislist:
    element = driver.find_element(By.CLASS_NAME,"perf-purchase-img.cursor-pointer")
# 傳入字串
    element.send_keys("pornhub")
    element.submit()
#driver.close() # 關閉瀏覽器視窗