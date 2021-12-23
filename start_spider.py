#!/usr/bin/env python3
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from bitcoinscraper.spiders.bitcoincore_spider import BitcoinCoreSpider

# Start crawl right away
process = CrawlerProcess(get_project_settings())
process.crawl(BitcoinCoreSpider)
process.start()
