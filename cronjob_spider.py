#!/usr/bin/env python3
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

from bitcoinscraper.spiders.bitcoincore_spider import BitcoinCoreSpider

process = CrawlerProcess(get_project_settings())
# Start the crawler in a scheduler
scheduler = TwistedScheduler(timezone="Europe/Amsterdam")
# Use cron job; runs once a week on the monday at 20:15
scheduler.add_job(process.crawl, 'cron', args=[BitcoinCoreSpider], day_of_week='mon', hour=20, minute=15)
scheduler.start()
process.start(False)
