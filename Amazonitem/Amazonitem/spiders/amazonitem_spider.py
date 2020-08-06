import os
import scrapy
from ..items import AmazonitemItem

class AmazonitemSpider(scrapy.Spider):
    name = 'amazonitem'
    amazon_list = []
    with open('SKUs_amazon.txt', 'r') as amazon_prod_links:
        for prod_link in amazon_prod_links:
            amazon_list.append(prod_link)
    count = len(amazon_list)

    start_urls = [str(amazon_list[114])]
    print("prod_link:  ", start_urls)
    next_page = start_urls
    page = 115
    def parse(self, response):
                items = AmazonitemItem()
                prod_link = self.next_page
                title = (str(response.css("#productTitle::text").extract()))
                reviews = response.css("#acrCustomerReviewText").css("::text").extract()
                offerprice = response.css("#priceblock_ourprice::text").extract()
                initialprice = response.css(".priceBlockStrikePriceString").css("::text").extract()
                rating = response.css(".reviewCountTextLinkedHistogram .a-icon-alt").css("::text").extract()
                description = response.css("#featurebullets_feature_div").css("::text").extract()
                image1 = response.css("#altImages .a-spacing-top-micro").css("::attr(src)").extract()

                items['prod_link'] = prod_link
                items['title'] = title.strip()
                items['reviews'] = reviews
                items['offerprice'] = offerprice
                items['initialprice'] = initialprice
                items['rating'] = rating
                items['description'] = str(description).strip()
                items['image1'] = image1

                yield items

                self.next_page = str(self.amazon_list[self.page])

                if AmazonitemSpider.page <= 124:
                    yield response.follow(self.next_page, callback=self.parse)
                    AmazonitemSpider.page += 1

