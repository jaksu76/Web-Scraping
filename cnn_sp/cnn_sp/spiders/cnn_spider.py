from scrapy import Spider
import scrapy
from scrapy.selector import Selector
from cnn_sp.items import CnnSpItem


class CnnSpSpider(Spider):
    name = "cnn_spider"
    allowed_urls = ['http://money.cnn.com/']
    start_urls = ['http://money.cnn.com/data/markets/sandp/' + '?page=' + str(i+1) for i in range(34)]

    def parse(self, response):
        rows = response.xpath('//*[@id="wsod_indexConstituents"]/div[1]/table/tbody/tr')

        for i in range(0, len(rows)):
            Ticker = rows[i].xpath('.//td[@class="wsod_firstCol"]/a/text()').extract_first()
            Company = rows[i].xpath('.//td[@class="wsod_firstCol"]/text()').extract_first()
            Company = ''.join(Company).replace(u'\xa0', u'')
            url = "http://money.cnn.com/quote/quote.html?symb=" + Ticker
            yield scrapy.Request(url, callback=self.parse_quote, meta={'Ticker' : Ticker, 'Company' : Company})

    def parse_quote(self, response):
        Ticker = response.meta['Ticker']
        Company = response.meta['Company']
        rows =response.xpath('//div [h3="Profile"]/child::div/table//tr')
        row = rows[0].xpath('//td/div/div[2]/text()').extract()
        Sector = row[0]
        Industry = row[1]
        url = "http://money.cnn.com/quote/financials/financials.html?symb=" + Ticker
        yield scrapy.Request(url, callback=self.parse_fin, meta={'Ticker' : Ticker, 'Company' : Company, 'Sector' : Sector, 'Industry' : Industry})

    def parse_fin(self, response):
        Ticker = response.meta['Ticker']
        Company = response.meta['Company']
        Sector = response.meta['Sector']
        Industry =response.meta['Industry']
        row_income = response.xpath('//*[@id="financial_statement"]/table/tbody/tr [td="Net Income"]')
        NetIncome = row_income.xpath('child::td[5]/text()').extract_first()
        url = "http://money.cnn.com/quote/financials/financials.html?symb=" + Ticker + "&dataSet=BS"
        yield scrapy.Request(url, callback=self.parse_bs, meta={'Ticker' : Ticker, 'Company' : Company, 'NetIncome' : NetIncome, 'Sector' : Sector, 'Industry' : Industry})
    
    def parse_bs(self,response):
        Ticker = response.meta['Ticker']
        Company = response.meta['Company']
        Sector = response.meta['Sector']
        Industry =response.meta['Industry']
        NetIncome = response.meta['NetIncome']
        row_asset = response.xpath('//*[@id="financial_statement"]/table/tbody/tr [td="Total Assets"]')
        TotalAssets = row_asset[1].xpath('child::td[5]/text()').extract_first()

        row_equity = response.xpath('//*[@id="financial_statement"]/table/tbody/tr [td="Total Shareholder Equity"]')
        TotalShareholderEquity = row_equity.xpath('child::td[5]/text()').extract_first()

        item = CnnSpItem()
        item['Company'] = Company
        item['Ticker'] = Ticker
        item['NetIncome'] = NetIncome
        item['Sector'] = Sector
        item['Industry'] = Industry
        item['TotalAssets'] = TotalAssets
        item['TotalShareholderEquity'] = TotalShareholderEquity

        yield item