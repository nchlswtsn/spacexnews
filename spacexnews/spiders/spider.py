# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from spacexnews.items import SpacexnewsItem


class MySpider(BaseSpider):
	name =  "spacexnews"
	allowed_domains = ["spacex.com"]		
	start_urls = ["http://www.spacex.com/missions"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		manifest = response.xpath('//div[@class="view-content"][2]/table[@class="views-table cols-4"]/tbody/tr')
		items = []


		for launch in manifest:
		    item = SpacexnewsItem()
		    item["customer"] = launch.xpath('./td[@class="customer"]/span/text()').extract()
		    item["location"] = launch.xpath('./td[@class="launch-site"]/span/text()').extract()
		    item["rocket"] = launch.xpath('./td[@class="vehicle"]/span/div/h2/a/text()').extract()
		    items.append(item)
		return items
		