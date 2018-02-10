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

#binary = FirefoxBinary(irefox.exe’)
path="/Users/sheetaldarekar/anaconda3/bin/geckodriver"
driver = webdriver.Firefox(executable_path=path)
wait = WebDriverWait(driver, 15)
url_form = "http://www.morningstar.com/stocks/{}/{}/quote.html"

exchange = ["xnas","xnas","xnas","xnys","xnas"]
sym = ["amzn", "aapl", "fb", "ibm", "msft"]
symbols = pd.DataFrame({'exchange': exchange, 'sym': sym})
 
url = "http://www.morningstar.com"
driver.get(url)
time.sleep(10)
	#wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='Direct to Morningstar.com']"))).click()
try:
	wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='image-0']/a"))).click()

except TimeoutException:
	pass

wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-step-0"]/div/section/div/p[2]/a'))).click()

time.sleep(3)
username = driver.find_element_by_name("uEmail")
username.send_keys("mdsheetal@gmail.com")
password = driver.find_element_by_name("uPassword")
password.send_keys("Winwin@321")

rem = driver.find_element_by_xpath('//label[@for="remember_me"]')
rem.click()

form = driver.find_element_by_id("uim-login-submit")
form.click()

#h4_xpath = "//h4[contains(text(), 'Sign in to Morningstar.com/xa0')]"
#wait.until(EC.presence_of_element_located((By.XPATH, h4_xpath)))
with open('moringstar.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	dic = {}

	dic['Ticker'] = 'Ticker'
	dic['Assessment'] = 'Assessment'
	dic['Fair Value'] = 'FairVal'
	writer.writerow(dic.values())


	with open('/Users/sheetaldarekar/NYCDS/Project/WebScraping/cnn_sp.csv') as f:
		symbols = csv.reader(f)
		next(symbols)
		for symbol in symbols:
			tick=symbol[1]
			time.sleep(4)
			#wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='search']")))
			#driver.implicitly_wait(10)
			search = driver.find_element_by_xpath("//input[@type='search']")
			actions = ActionChains(driver)
			#search.click()
			actions.move_to_element(search).click().send_keys(tick).send_keys(Keys.RETURN).perform()
			print(tick)
			#search.send_keys(tick)
			print("Start : %s" %time.ctime())
			time.sleep( 20 )
			print("End : %s" %time.ctime())

			wait.until(EC.text_to_be_present_in_element((By.XPATH,"//span[@class='sal-component-title ng-binding']"),"Morningstar's Analysis"))
			#he element reference of <div class="dp-value ng-binding ng-scope"> is stale; either the element is no longer attached to the DOM, it is not in the current frame context, or the document has been refreshed

			analysis = driver.find_elements_by_xpath('//div[@class="dp-value ng-binding ng-scope"]')
			Assessment = analysis[0].text
			FairVal = analysis[1].text

			print(Assessment)
			print("--->>>>>")
			print(FairVal)
			time.sleep(1)


			dic['Ticker'] = tick
			dic['Assessment'] = Assessment
			dic['Fair Value'] = FairVal
			writer.writerow(dic.values())
		f.close()
		csvfile.close()	




	
	#	driver.find_element_by_xpath('//*[@id="_content_morningstarcomv2_en_us_jcr_content_parsys-whole_teaser"]/section/div/header/div/a/span[1]').click()

	#driver.find_element_by_xpath("/html/body/div[4]/footer/div[1]/div[2]/div/section[5]/div/div[1]/section/header/div/div/div[2]/div/div/ul/li/a").click()
	
	#sign in button
	#driver.find_element_by_xpath("/html/body/div[4]/header/div[1]/div[1]/div[3]/div[2]/div/ul/li[4]/a").click()
	#h4_xpath = "//h4[contains(text(), 'Sign in to Morningstar.com/xa0')]"
	#WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, h4_xpath)))
	#username = driver.find_element_by_name("uEmail")
	#username.send_keys("mdsheetal@gmail.com")
	#password = driver.find_element_by_name("uPassword")
	#password.send_keys("winwin@321")
	#form = browser.find_element_by_id("uim-login-submit")
	#form.submit()
	#search = driver.find_element_by_id("header_site_search-0")
	#search.send_keys(symbol[1])
	#company_xpath = "//span[contains(id, 'sal-components-take')]"
	#company_xpath = "//h3[contains(text(), 'Current Valuation')]"
	#driver.find_element_by_class_name
	#//*[@id="sal-components-take"]/div[2]/div/div[1]/span

	#company = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, company_xpath))).text

	#pe_xpath = "//*[@id='panel_take_report']/div/div[1]/div[1]/div[3]"
	#pe = driver.find_element_by_xpath(pe_xpath).text
	#print("Hi")

#	except:
#		company = nan
	#print(reviews)
		# Iterate through the list and find the details of each review.
	#for review in reviews:
			# Initialize an empty dictionary for each review
	#	review_dict = {}
			# Use relative xpath to locate the title, content, username, date, rating.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use `element.get_attribute()`
	#	title = review[1].find_element_by_xpath('./th"]').text
			# .get_attribute('itemprompt')
			#Your code here
			#content=review.find_elements_by_xpath('.//div[@class="bv-content-summary-body-text"]/p')
			#content="".join([x.text for x in content])
			#author=review.find_element_by_xpath('.//h3[@class="bv-author"]').text
			#stars=review.find_element_by_xpath('.//span[@class="bv-off-screen"]').text[0]
			#dt=review.find_element_by_xpath('.//span[@class="bv-content-datetime-stamp"]').text
			#date = review.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
	#	print(title)
	#	print("---"*20)
		#button = driver.find_element_by_xpath('//li[@class="bv-content-pagination-buttons-item bv-content-pagination-buttons-item-next"]')
		#button.click()



		# Locate the next button element on the page and then call `button.click()` to click it.
		# button = # Your code here
		# button.click()

#except Exception as e:
#	print(e)
driver.close()

