import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(2)
driver.quit()
