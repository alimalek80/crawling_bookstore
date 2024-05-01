# Scrapy Crawler for Books on 'toscrape.com'

## Description

This is a Scrapy crawler that extracts product data (title, price, availability) from book listings on 'toscrape.com'. It utilizes CrawlSpider functionalities to navigate through the website and extract relevant information.

## Installation

1. Make sure you have Scrapy installed: `pip install scrapy`
2. Clone this repository to your local machine.

## Usage

Run the scraper from the command line: `scrapy crawl mycrawler`

## Explanation

The code utilizes the following functionalities:

- **CrawlSpider:** This class allows for automatic crawling of websites by following links based on defined rules.
- **Rule:** This class defines rules for link extraction based on URL patterns (allow/deny) and specifies callbacks for extracted links.
- **LinkExtractor:** This class helps extract links from webpages based on URL patterns.

The crawler follows these steps:

1. Starts at the provided URL (https://books.toscrape.com/).
2. Extracts links containing "catalogue/category" in the URL and follows them to explore categories.
3. Extracts other links under "catalogue" but excludes "category" links.
4. For extracted product pages, it parses the content to retrieve the title, price, and availability using CSS selectors.
5. Finally, it yields the extracted data as a dictionary.

## Further Notes

- This is a basic example showcasing web scraping with Scrapy.
- You can modify the CSS selectors and logic to extract different data points or handle different website structures.
- Consider error handling and logging for a more robust scraper.
