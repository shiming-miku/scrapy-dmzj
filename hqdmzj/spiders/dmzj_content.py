import scrapy

from hqdmzj.items import HqdmzjItem

class dmzjContentpider(scrapy.Spider):
    name = "dmzjcontent"
    allowed_domains = ["dmzj.com"]
    start_urls = [
        "https://news.dmzj.com/article/48308.html"
    ]
    def parse(self,response):
        print response.url
        for sel in response.xpath('//div[@class="news_content_con"]'):
            dmzjitem = HqdmzjItem()
            dmzjitem['content'] = sel.extract().encode('utf-8')
            yield dmzjitem