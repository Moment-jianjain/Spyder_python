import scrapy


class TipdmSpider(scrapy.Spider):
    name = "tipdm"
    allowed_domains = ["www.tipdm.com"]
    start_urls = ["https://www.tipdm.com"]

    def parse(self, response):
        pass
