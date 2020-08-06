import scrapy
from  ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self,response):
        items = QuotetutorialItem()
        all_div_quotes = response.css("div.quote")

        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css("small.author::text").extract()
            tags = quote.css(".tags .tag::text").extract()
            print("tags is :",tags)
            items['title'] = "".join(title)
            items['author'] = "".join(author)
            items['tags'] = ",".join(tags)

            yield items
