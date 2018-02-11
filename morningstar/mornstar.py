from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import csv
import re
import time

#Enter username and password
#Add time.sleep accordingly

path="/Users/sheetaldarekar/anaconda3/bin/geckodriver"
driver = webdriver.Firefox(executable_path=path)
wait = WebDriverWait(driver, 15) 
url = "http://www.morningstar.com"
driver.get(url)
time.sleep(25)
	
try:
	wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='image-0']/a"))).click()

except TimeoutException:
	pass

wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-step-0"]/div/section/div/p[2]/a'))).click()

time.sleep(10)
username = driver.find_element_by_name("uEmail")
username.send_keys("******")
password = driver.find_element_by_name("uPassword")
password.send_keys("******")

time.sleep(10)

rem = driver.find_element_by_xpath('//label[@for="remember_me"]')
rem.click()

form = driver.find_element_by_id("uim-login-submit")
form.click()

with open('moringstar.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	dic = {}

	dic['Ticker'] = 'Ticker'
	dic['Assessment'] = 'Assessment'
	dic['Fair Value'] = 'Fair Value'
	dic['FiveStarPrice'] = 'FiveStarPrice'
	dic['OneStarPrice'] = 'OneStarPrice'
	writer.writerow(dic.values())

	with open('/Users/sheetaldarekar/NYCDS/Project/WebScraping/cnn_sp.csv') as f:
		symbols = csv.reader(f)
		next(symbols)
		for symbol in symbols:
			tick=symbol[1]
			time.sleep(4)
			search = driver.find_element_by_xpath("//input[@type='search']")
			actions = ActionChains(driver)
			actions.move_to_element(search).click().send_keys(tick).send_keys(Keys.RETURN).perform()
			print(tick)
			print("Start : %s" %time.ctime())
			time.sleep( 25 )
			print("End : %s" %time.ctime())

			wait.until(EC.text_to_be_present_in_element((By.XPATH,"//span[@class='sal-component-title ng-binding']"),"Morningstar's Analysis"))
			
			analysis1 = driver.find_elements_by_xpath('//div[@class="dp-value ng-binding ng-scope"]')
			Assessment = analysis1[1].text
			FairVal = analysis1[2].text
			analysis2 = driver.find_elements_by_xpath('//span[@class="ng-binding ng-scope"]')
			FiveStarPrice = analysis2[1].text
			OneStarPrice = analysis2[3].text

			print(Assessment)
			print(FairVal)
			print(FiveStarPrice)
			print(OneStarPrice)
			print("<<<<--->>>>>")
			time.sleep(1)

			dic['Ticker'] = tick
			dic['Assessment'] = Assessment
			dic['Fair Value'] = FairVal
			dic['FiveStarPrice'] = FiveStarPrice
			dic['OneStarPrice'] = OneStarPrice
			writer.writerow(dic.values())
		f.close()
		csvfile.close()
	
driver.close()

