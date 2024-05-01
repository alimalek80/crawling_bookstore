# Import necessary classes from Scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Define our CrawlSpider subclass
class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'  # Name for this crawler
    allowed_domains = ['toscrape.com']  # Restrict crawling to this domain

    # Starting point for crawling
    start_urls = ['https://books.toscrape.com/']

    # Define rules for link extraction and parsing
    rules = (
        # Extract links that contain "catalogue/category" in the URL
        Rule(LinkExtractor(allow="catalogue/category"), follow=True),
        # Extract other links under "catalogue" but exclude "category"
        # and call the parse_item callback for these extracted links
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    # Parse items on product pages
    def parse_item(self, response):
        # Extract product title using CSS selector
        title = response.css(".product_main h1::text").get()

        # Extract product price using CSS selector
        price = response.css(".price_color::text").get()

        # Extract product availability using CSS selector and clean text
        availability = response.css(".availability::text")[1].get().replace("\n", "").replace(" ", "")

        # Yield extracted data as a dictionary
        yield {
            'title': title,
            'price': price,
            'availability': availability,
        }