# coding: utf-8
from scrapy.item import Item, Field


class SpacexnewsItem(Item):
	customer = Field()
	location = Field()
	rocket = Field()