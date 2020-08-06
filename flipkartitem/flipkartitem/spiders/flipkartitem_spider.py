import os
import scrapy
from ..items import FlipkartitemItem

class FlipkartitemSpider(scrapy.Spider):
    name = 'flipkartitem'
    flipkart_list = []
    with open('SKUs_Flipkart.txt', 'r') as flipkart_prod_links:
        for prod_link in flipkart_prod_links:
            flipkart_list.append(prod_link)
    count = len(flipkart_list)

    start_urls = [str(flipkart_list[0])]
    print("prod_link:  ", start_urls)
    next_page = start_urls
    page = 1
    def parse(self, response):
                items = FlipkartitemItem()
                prod_link = self.next_page
                title = response.css("._35KyD6::text").extract()
                reviews = response.css("._38sUEc span span:nth-child(1)").css("::text").extract()
                offerprice = response.css("._3qQ9m1::text").extract()
                initialprice = response.css("._1POkHg").css("::text").extract()
                rating = response.css("._3ors59 .hGSR34").css("::text").extract()
                description = response.css("._2-riNZ::text").extract()
                images = response.css("._2_AcLJ").css("::attr(style)").extract()

                items['prod_link'] = prod_link
                items['title'] = str(title).strip()
                items['reviews'] = reviews
                items['offerprice'] = offerprice
                items['initialprice'] = initialprice
                items['rating'] = rating
                items['description'] = str(description).strip()
                items['images'] = images

                yield items

                self.next_page = str(self.flipkart_list[self.page])

                if FlipkartitemSpider.page <= self.count:
                    yield response.follow(self.next_page, callback=self.parse)
                    FlipkartitemSpider.page += 1