from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url_form = "http://financials.morningstar.com/valuation/price-ratio.html?t={}"

symbols = ["amzn", "aapl", "fb", "ibm", "msft"]

for i, symbol in enumerate(symbols):
 
	url = url_form.format(symbol)
	driver.get(url)
	company_xpath = "//h3[contains(text(), 'Current Valuation')]"

	company = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, company_xpath))).text
	pe_xpath = "//*[@id='currentValuationTable']/tbody/tr[2]/td[1]"
	pe = driver.find_element_by_xpath(pe_xpath).text
	print(pe)

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

