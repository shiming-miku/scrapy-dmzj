import scrapy

from hqdmzj.items import HqdmzjItem

class DmzjSpider(scrapy.Spider):
    name = "dmzj"
    allowed_domains = ["dmzj.com"]
    start_urls = [
        "https://news.dmzj.com/"
    ]
    def parse(self,response):
        item = []
        item2 = []
        for sel in response.xpath('//div[@class="li_content_img"]'):
            dmzjitem = HqdmzjItem()
            dmzjitem['title'] = sel.xpath('.//a/@title').extract()
            dmzjitem['cover'] = sel.xpath('.//a').xpath('img/@src').extract()
            dmzjitem['url'] = sel.xpath('.//a/@href').extract()
            item.append(dmzjitem)
        for sel in response.xpath('//p[@class="head_con_p_o"]'):
            dmzjitem = HqdmzjItem()
            dmzjitem['time'] = sel.xpath('.//span[1]/text()').extract()
            dmzjitem['author'] = sel.xpath('.//span[3]/text()').extract()
            item2.append(dmzjitem)
        for i in range(len(item)):
            dmzjitem = HqdmzjItem
            dmzjitem2 = HqdmzjItem
            dmzjitem = item[i]
            dmzjitem2 = item2[i]
            dmzjitem['time'] = dmzjitem2['time']
            dmzjitem['author'] = dmzjitem2['author']
            yield dmzjitem