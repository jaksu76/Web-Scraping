import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from nasdaq.items import NasdaqItem
import csv
import re

class NasdaqSpider(Spider):
    name = "nasdaq_spider"
    allowed_urls = ['https://www.nasdaq.com/']
    
    def start_requests(self):
        with open('/Users/sheetaldarekar/NYCDS/Project/WebScraping/cnn_sp/cnn_sp.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                start_urls = 'https://www.nasdaq.com/symbol/' + row[1].lower() + '/institutional-holdings'
                yield scrapy.Request(url = start_urls, callback = self.parse, method = 'GET', meta = {'ticker' : row[1]})

    def parse(self, response):
        
        Ticker = response.meta['ticker']
        
        rows = response.xpath('//*[@class="infoTable marginT15px marginL15px"]//tr')
        InstOwnerPercent = rows[0].xpath('./td/text()').extract_first()
        TotalOwners = rows[1].xpath('./td/text()').extract_first()
        TotalValue = rows[2].xpath('./td/text()').extract_first()

        rows2 = response.xpath('//div[@class="infoTable paddingT5px"]/table/tr[@class="sum"]//td')
        InstOwners = rows2[0].xpath('./text()').extract_first()
        InstValue = rows2[1].xpath('./text()').extract_first()

        new_urls = [response.url + '?page=' + str(i+1) for i in range(3)]
        for new_url in new_urls:
            yield scrapy.Request(url = new_url, callback = self.parse_owners, method = 'GET', meta = {
                'Ticker' : Ticker, 'InstOwnerPercent' : InstOwnerPercent, 'TotalOwners' : TotalOwners, 'TotalValue' : TotalValue, 'InstValue' : InstValue, 'InstOwners' : InstOwners
                })

    def parse_owners(self, response):

        Ticker = response.meta['Ticker']
        InstOwnerPercent = response.meta['InstOwnerPercent']
        TotalOwners = response.meta['TotalOwners']
        TotalValue = response.meta['TotalValue']
        InstValue = response.meta['InstValue']
        InstOwners = response.meta['InstOwners']
        rows3 = response.xpath('//*[@id="quotes_content_left_pnlInsider"]/table//tr')
        for i in range(0, len(rows3)):
            OwnerNames = rows3[i].xpath('./td[1]/a/text()').extract_first()
            SharesHeld = rows3[i].xpath('./td[3]/text()').extract_first()
            SharesValue = rows3[i].xpath('./td[6]/text()').extract_first()

            item = NasdaqItem()
            item['Ticker'] = Ticker
            item['InstOwnerPercent'] = InstOwnerPercent
            item['TotalOwners'] = TotalOwners
            item['TotalValue'] = TotalValue
            item['OwnerNames'] = OwnerNames
            item['InstOwners'] = InstOwners
            item['InstValue'] = InstValue
            item['SharesHeld'] = SharesHeld
            item['SharesValue'] = SharesValue

            yield item