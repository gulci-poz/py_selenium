from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com")
userName = driver.find_element_by_name("userName")
print(userName.is_displayed())
print(userName.is_enabled())
print(userName.is_selected())
password = driver.find_element_by_name("password")
print(password.is_displayed())
print(password.is_enabled())
print(password.is_selected())
# userName.send_keys("mercury")
# password.send_keys("mercury")
# driver.find_element_by_name("login").click()
# roundtrip = driver.find_element_by_css_selector("input[value=roundtrip]")
# print(roundtrip.is_selected())
# oneway = driver.find_element_by_css_selector("input[value=oneway]")
# print(oneway.is_selected())
driver.close()
