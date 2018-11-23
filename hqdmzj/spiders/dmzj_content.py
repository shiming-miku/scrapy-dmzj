import scrapy

from hqdmzj.items import ContentItem


class dmzjContentpider(scrapy.Spider):
    name = "dmzjcontent"
    allowed_domains = ["dmzj.com"]
    start_urls = [
        "https://news.dmzj.com/article/48397.html"
    ]

    def parse(self, response):
        print response.url
        for sel in response.xpath('//div[@class="news_content_con"]/p'):
            contentItem = ContentItem()
            contentItem['text'] = ''
            try:
                sel.xpath('.//img/@src').extract()[0]
            except IndexError:
                try:
                    sel.xpath('.//span').extract()[0]
                    for self in sel.xpath('.//span'):
                        contentItem['text'] += self.xpath('.//text()').extract()[0].encode('utf-8')
                except IndexError:
                    try:
                        contentItem['text'] = sel.xpath('.//text()').extract()[0].encode('utf-8')
                    except IndexError:
                        continue

            else:
                contentItem['text'] = sel.xpath('.//img/@src').extract()[0].encode('utf-8')
            yield contentItem
