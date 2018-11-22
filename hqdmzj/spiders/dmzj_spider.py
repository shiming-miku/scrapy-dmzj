# coding=utf-8
import scrapy
from scrapy import Request

from hqdmzj.items import HqdmzjItem
from hqdmzj.items import ContentItem


class DmzjSpider(scrapy.Spider):
    name = "dmzj"
    allowed_domains = ["dmzj.com"]
    start_urls = [
        "https://news.dmzj.com/"
    ]

    # decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
    # encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码

    def parse(self, response):
        item = []
        item2 = []
        for sel in response.xpath('//div[@class="li_content_img"]'):
            dmzjitem = HqdmzjItem()
            dmzjitem['title'] = sel.xpath('.//a/@title').extract()[0].encode("utf-8")
            dmzjitem['cover'] = sel.xpath('.//a').xpath('img/@src').extract()[0].encode("utf-8")
            dmzjitem['url'] = sel.xpath('.//a/@href').extract()[0].encode("utf-8")
            #yield Request(url=dmzjitem['url'], callback=self.get_content, meta={'dmzjitem':dmzjitem})
            #yield Request(url=dmzjitem['url'], callback=self.insert_content, meta={'dmzjitem':dmzjitem})
            item.append(dmzjitem)

        for sel in response.xpath('//p[@class="head_con_p_o"]'):
            dmzjitem = HqdmzjItem()
            dmzjitem['time'] = sel.xpath('.//span[1]/text()').extract()[0].encode("utf-8")
            dmzjitem['author'] = sel.xpath('.//span[3]/text()').extract()[0].encode("utf-8")
            item2.append(dmzjitem)

        for i in range(len(item)):
            dmzjitem = item[i]
            dmzjitem2 = item2[i]
            dmzjitem['time'] = dmzjitem2['time']
            dmzjitem['author'] = dmzjitem2['author']
            yield dmzjitem

        for i in range(len(item)):
            dmzjitem = item[i]
            yield Request(url=dmzjitem['url'], callback=self.insert_content, meta={'dmzjitem': dmzjitem})

    def insert_content(self,response):
        for sel in response.xpath('//div[@class="news_content_con"]/p'):
            contentItem = ContentItem()
            contentItem['url'] = response.meta['dmzjitem']['url']
            try:
                sel.xpath('.//img/@src').extract()[0]
            except IndexError:
                try:
                    contentItem['text'] = sel.xpath('.//text()').extract()[0].encode('utf-8')
                except IndexError:
                    continue
            else:
                contentItem['text'] = sel.xpath('.//img/@src').extract()[0].encode('utf-8')
            yield contentItem

    def get_content(self,response):
        for sel in response.xpath('//div[@class="news_content_con"]'):
            dmzjitem = response.meta['dmzjitem']
            dmzjitem['content'] = sel.xpath('.').extract()[0].encode("utf-8")
            yield dmzjitem