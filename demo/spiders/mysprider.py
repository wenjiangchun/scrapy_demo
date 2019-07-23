import scrapy

from demo.items import DemoItem

class MySpider(scrapy.Spider):
    name = "demo"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        item =  DemoItem()
        item["name"] = filename
        item["title"] = response.body
       # with open(filename, 'wb') as f:
        #    f.write(response.body)
        self.log('Saved item %s' % filename)
        yield item