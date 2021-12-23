# Bitcoin Core Web Scraper

A script for web scraping and downloading the [Bitcoin Core `bin`](https://bitcoincore.org/bin) directory.  
Ideal for creating your own mirror!

## Usage

### Dependencies

Run-time dependency:

* Python3 + pip (`python3 python3-dev python3-pip`)
* Additional libs for Scrapy (`libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`)

More packages will be downloaded via `pip`, see next section.

### Prepare

I advice you to use a [Python virtual environment](https://docs.python.org/3/library/venv.html#), create & activate such an environment via:

```sh
python3 -m venv env
source env/bin/activate
```

Next, install the required packages via:

```sh
pip install -r requirements.txt
```

### Run scraper

Execute scraper and **start downloading**:

```sh
scrapy crawl bitcoincore
```

*Note:* Files are stored within the `bin` sub-folder of the root-folder of this project (at the moment).

Optionally, execute scraper and output the meta-data to a "feed" file (eg. JSON file):

```sh
scrapy crawl bitcoincore -O bitcoincore.json
```

## Build Docker image

*Note:* Docker Image is [available on DockerHub](https://hub.docker.com/r/danger89/bitcoinscraper).

Run:

```sh
docker build -t danger89/bitcoinscraper .
```

I also provided a [docker-compose file](bitcoinscraper-compose.yml).

## Learn & Debug

You can use the Scrapy shell to help debugging or learn how to extract data:

```sh
scrapy shell 'https://bitcoincore.org/bin/'
```

Now, check the `response` object for data, just an example:

```py
response.css('pre a')[3].get()
```

## External Links

More info:

* [Scrapy homepage](https://scrapy.org)
* [Scrapy Tutorial docs](https://docs.scrapy.org/en/latest/intro/tutorial.html) (ideal for beginners)
* [APScheduler Cron docs](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html)
