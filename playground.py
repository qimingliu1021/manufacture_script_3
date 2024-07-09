from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)  # Should print the title of the page
driver.quit()