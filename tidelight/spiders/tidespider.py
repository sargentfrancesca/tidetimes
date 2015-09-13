import scrapy
import datetime
from tidelight.items import TideLightItem

class TideSpider(scrapy.Spider):
    name = "tidespider"
    allowed_domains = ["tidetimes.org.uk"]
    start_urls = [
        "https://www.tidetimes.org.uk/falmouth-tide-times"
    ]

    def parse(self, response):
        tides = response.xpath('.//td[@class="tac"][1]/span[1]//text()').extract()
        low_1 = tides[0]
        high_1 = tides[1]
        low_2 = tides[2]
        high_2 = tides[3]

        next_high = response.xpath('.//div[@id="nxhi"]/span//text()').extract()
        next_low = response.xpath('.//div[@id="nxlo"]/span//text()').extract()

        print next_high, next_low

        item = TideLightItem()
        item['low_1'] = low_1
        item['high_1'] = high_1
        item['low_2'] = low_2
        item['high_2'] = high_2
        item['timecollected'] = datetime.datetime.now()
        item['next_high'] = next_high[0]
        item['next_low'] = next_low[0]

        return item

