from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.close()
