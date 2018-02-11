from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

driver = webdriver.Chrome()

url_form = "http://financials.morningstar.com/valuation/price-ratio.html?t={}"

with open('financials_moringstar.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	dic = {}

	dic['Ticker'] = 'Ticker'
	dic['pe'] = 'Price/Earnings'
	dic['pe_ind'] = 'Price/Earnings_ind'
	dic['pe_sp'] = 'Price/Earnings_sp'
	dic['pe_5yavg'] = 'Price/Earnings_5yavg'
	dic['pb'] = 'Price/Book'
	dic['pb_ind'] = 'Price/Book_ind'
	dic['pb_sp'] = 'Price/Book_sp'
	dic['pb_5yavg'] = 'Price/Book_5yavg'
	dic['ps'] = 'Price/Sales'
	dic['ps_ind'] = 'Price/Sales_ind'
	dic['ps_sp'] = 'Price/Sales_sp'
	dic['ps_5yavg'] = 'Price/Sales_5yavg'
	dic['pc'] = 'Price/Cash Flow'
	dic['pc_ind'] = 'Price/Cash Flow_ind'
	dic['pc_sp'] = 'Price/Cash Flow_sp'
	dic['pc_3yavg'] = 'Price/Cash Flow_3yavg'
	dic['div'] = 'Dividend Yield %'
	dic['div_ind'] = 'Dividend Yield %_ind'
	dic['div_sp'] = 'Dividend Yield %_sp'
	dic['div_5yavg'] = 'Dividend Yield %_5yavg'
	dic['peg'] = 'PEG Ratio'

	writer.writerow(dic.values())

	with open('/Users/sheetaldarekar/NYCDS/Project/WebScraping/cnn_sp.csv') as f:
		symbols = csv.reader(f)
		next(symbols)
		for symbol in symbols:
			tick=symbol[1]

			url = url_form.format(tick)
			driver.get(url)

			time.sleep(2)
			company_xpath = "//h3[contains(text(), 'Current Valuation')]"

			company = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, company_xpath))).text
			pe_xpath = "//*[@id='currentValuationTable']/tbody/tr[2]/td[1]"
			pe = driver.find_element_by_xpath(pe_xpath).text
			pe_ind_xpath = "//*[@id='currentValuationTable']/tbody/tr[2]/td[2]"
			pe_ind = driver.find_element_by_xpath(pe_ind_xpath).text
			pe_sp_xpath = "//*[@id='currentValuationTable']/tbody/tr[2]/td[3]"
			pe_sp = driver.find_element_by_xpath(pe_sp_xpath).text
			pe_5yavg_xpath = "//*[@id='currentValuationTable']/tbody/tr[2]/td[4]"
			pe_5yavg = driver.find_element_by_xpath(pe_5yavg_xpath).text

			pb_xpath = "//*[@id='currentValuationTable']/tbody/tr[4]/td[1]"
			pb = driver.find_element_by_xpath(pb_xpath).text
			pb_ind_xpath = "//*[@id='currentValuationTable']/tbody/tr[4]/td[2]"
			pb_ind = driver.find_element_by_xpath(pb_ind_xpath).text
			pb_sp_xpath = "//*[@id='currentValuationTable']/tbody/tr[4]/td[3]"
			pb_sp = driver.find_element_by_xpath(pb_sp_xpath).text
			pb_5yavg_xpath = "//*[@id='currentValuationTable']/tbody/tr[4]/td[4]"
			pb_5yavg = driver.find_element_by_xpath(pb_5yavg_xpath).text

			ps_xpath = "//*[@id='currentValuationTable']/tbody/tr[6]/td[1]"
			ps = driver.find_element_by_xpath(ps_xpath).text
			ps_ind_xpath = "//*[@id='currentValuationTable']/tbody/tr[6]/td[2]"
			ps_ind = driver.find_element_by_xpath(ps_ind_xpath).text
			ps_sp_xpath = "//*[@id='currentValuationTable']/tbody/tr[6]/td[3]"
			ps_sp = driver.find_element_by_xpath(ps_sp_xpath).text
			ps_5yavg_xpath = "//*[@id='currentValuationTable']/tbody/tr[6]/td[4]"
			ps_5yavg = driver.find_element_by_xpath(ps_5yavg_xpath).text

			pc_xpath = "//*[@id='currentValuationTable']/tbody/tr[8]/td[1]"
			pc = driver.find_element_by_xpath(pc_xpath).text
			pc_ind_xpath = "//*[@id='currentValuationTable']/tbody/tr[8]/td[2]"
			pc_ind = driver.find_element_by_xpath(pc_ind_xpath).text
			pc_sp_xpath = "//*[@id='currentValuationTable']/tbody/tr[8]/td[3]"
			pc_sp = driver.find_element_by_xpath(pc_sp_xpath).text
			pc_3yavg_xpath = "//*[@id='currentValuationTable']/tbody/tr[8]/td[4]"
			pc_3yavg = driver.find_element_by_xpath(pc_3yavg_xpath).text

			div_xpath = "//*[@id='currentValuationTable']/tbody/tr[10]/td[1]"
			div = driver.find_element_by_xpath(div_xpath).text
			div_ind_xpath = "//*[@id='currentValuationTable']/tbody/tr[10]/td[2]"
			div_ind = driver.find_element_by_xpath(div_ind_xpath).text
			div_sp_xpath = "//*[@id='currentValuationTable']/tbody/tr[10]/td[3]"
			div_sp = driver.find_element_by_xpath(div_sp_xpath).text
			div_5yavg_xpath = "//*[@id='currentValuationTable']/tbody/tr[10]/td[4]"
			div_5yavg = driver.find_element_by_xpath(div_5yavg_xpath).text

			peg_xpath = "//*[@id='forwardValuationTable']/tbody/tr[4]/td[1]"
			peg = driver.find_element_by_xpath(pb_xpath).text
		
			print(tick)
			print('pe:',pe, "  ", pe_ind,"  ", pe_sp, "  ", pe_5yavg)
			print('pb:',pb, "  ", pb_ind,"  ", pb_sp, "  ", pb_5yavg)
			print('ps:',ps, "  ", ps_ind,"  ", ps_sp, "  ", ps_5yavg)
			print('pc:',pc, "  ", pc_ind,"  ", pc_sp, "  ", pc_3yavg)
			print('div:',pb, "  ", div_ind,"  ", div_sp, "  ", div_5yavg)
			print('peg:', peg)
			print("<<<<<<------->>>>>>")

			dic['Ticker'] = tick
			dic['pe'] = pe
			dic['pe_ind'] = pe_ind
			dic['pe_sp'] = pe_sp
			dic['pe_5yavg'] = pe_5yavg
			dic['pb'] = pb
			dic['pb_ind'] = pb_ind
			dic['pb_sp'] = pb_sp
			dic['pb_5yavg'] = pb_5yavg
			dic['ps'] = ps
			dic['ps_ind'] = ps_ind
			dic['ps_sp'] = ps_sp
			dic['ps_5yavg'] = ps_5yavg
			dic['pc'] = pc
			dic['pc_ind'] = pc_ind
			dic['pc_sp'] = pc_sp
			dic['pc_3yavg'] = pc_3yavg
			dic['div'] = div
			dic['div_ind'] = div_ind
			dic['div_sp'] = div_sp
			dic['div_5yavg'] = div_5yavg
			dic['peg'] = peg
			writer.writerow(dic.values())
	f.close()
csvfile.close()



driver.close()

