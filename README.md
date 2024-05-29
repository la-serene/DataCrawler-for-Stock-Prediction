# Data Crawler

This crawler is designed to crawl data for stock prediction problem. Data are mainly historical stock data, NASDAQ, Dow Jones,
etc. plus Finance/Stock
articles from VietnamTimes for market sentiment analysis, which could be a meaningful feature for prediction.

## Usage
Stock data can be pulled through CLI:
```
python stock_crawler.py
```

NASDAQ, Down Jones, etc. indices can be pulled by running the following command:
```angular2html
python collect_financial_data.py
```

Articles can also be crawled through similar process:
```
python VnTimes.py
```

By default, stock symbols used in dataset are "FPT", "VCB", "HPG", "VPB", "VNM" and "VIC". Meanwhile, articles are downloaded from VnExpress.
In case user wants to crawl other stock symbol, clone the repo and change `stock_list` in stock_crawler.py to desired value.

The outdated VnExpress is stored in vnexpress_crawler directory.
