from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://newtours.demoaut.com")
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.close()
