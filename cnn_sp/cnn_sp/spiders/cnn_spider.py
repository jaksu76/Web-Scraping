from scrapy import Spider
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
            Company = rows[i].xpath('.//td[@class="wsod_firstCol"]/text()').extract()
            Company = ''.join(Company).replace(u'\xa0', u'')

            item = CnnSpItem()
            item['Company'] = Company
            item['Ticker'] = Ticker

            yield item