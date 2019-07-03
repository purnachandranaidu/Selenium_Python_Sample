from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='F:/chromedrive/chromedriver.exe')
driver.get("https://www.wonderwe.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//i[@class='fa fa-times']").click()
title=driver.title
print(title)
driver.find_element_by_xpath("(//div[@class='homePage-title'])[1]").click()
Bigtext=driver.find_element_by_xpath("//div[@class='bigtext']/h1").text
print(Bigtext)
driver.find_element_by_xpath("//div[@class='col-sm-6 col-centered section-action']").click()

select = Select(driver.find_element_by_xpath("//SELECT[@id='COUNTRY']"))
select.select_by_index(2)
driver.implicitly_wait(10)
driver.find_element_by_id("mce-city").send_keys("Sydney")
driver.implicitly_wait(10)
driver.find_element_by_id("mce-zip").send_keys("5807")
driver.implicitly_wait(10)
driver.find_element_by_name("subscribe").click()

