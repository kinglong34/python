from selenium import webdriver

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome("/Users/kinglongkwan/Documents/GitHub/python/chromedriver")
driver.get("http://www.google.com") # 更改網址以前往不同網頁
# 定位搜尋框
element = driver.find_element_Id("input")
# 傳入字串
element.send_keys("Selenium Python")
#driver.close() # 關閉瀏覽器視窗