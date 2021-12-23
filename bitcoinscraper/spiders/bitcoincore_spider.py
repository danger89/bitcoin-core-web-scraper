import scrapy
from bitcoinscraper.items import BitcoinscraperDownloadItem

class BitcoinCoreSpider(scrapy.Spider):
    name = 'bitcoincore'
    start_urls = [
        'https://bitcoincore.org/bin/',
    ]

    def parse(self, response):
        links = response.css('pre a::attr("href")').getall()

        downloadItem = BitcoinscraperDownloadItem()
        downloadItem['file_urls'] = []
        if links is not None:
            for link in links:
                # If the links is a folder, continue follow that link/crawling futher
                if link.startswith("bitcoin-core"):
                    # Optionally: We could also try to export additional data (eg. to JSON file)
                    #version = link.split("/")[0].split("-")[-1]
                    #yield {
                    #    'version': version,
                    #    'url': response.urljoin(link)
                    #}
                    yield response.follow(link, self.parse)
                elif link.startswith("bitcoin-") or link.startswith("SHA256SUMS"):
                    # Ready to download those files, by adding the url to the files_urls item field
                    downloadItem['file_urls'].append(response.urljoin(link))

            # Only yield when we actually filled-in file_urls
            if not len(downloadItem['file_urls']) == 0:
                yield downloadItem
