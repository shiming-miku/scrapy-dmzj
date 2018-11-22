import scrapy

from hqdmzj.items import HqdmzjItem


class dmzjContentpider(scrapy.Spider):
    name = "dmzjcontent"
    allowed_domains = ["dmzj.com"]
    start_urls = [
        "https://news.dmzj.com/article/48308.html"
    ]

    def parse(self, response):
        print response.url
        for sel in response.xpath('//div[@class="news_content_con"]/p'):
            dmzjitem = HqdmzjItem()
            try:
                sel.xpath('.//img/@src').extract()[0]
            except IndexError:
                try:
                    dmzjitem['content'] = sel.xpath('.//text()').extract()[0].encode('utf-8')
                except IndexError:
                    continue
            else:
                dmzjitem['content'] = sel.xpath('.//img/@src').extract()[0].encode('utf-8')
            yield dmzjitem
