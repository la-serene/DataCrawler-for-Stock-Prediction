# Simple_DataCrawler

This crawler is designed to crawl data for stock prediction problem. Data are mainly historical stock data plus Finance/Stock
articles for market sentiment analysis, which could be a meaningful feature for prediction.

Data are automatically crawled at 0:00 GMT+7 on the daily basis.

## Usage
Stock data can be downloaded through CLI:
```
python stock_crawler.py
```

Articles can also be crawled through similar process:
```
python article_crawler.py
```

By default, stock symbols used in dataset are "FPT", "VCB", "HPG", "VPB", "VNM" and "VIC". Meanwhile, articles are downloaded from VnExpress.
In case user wants to crawl other stock symbol, clone the repo and change `stock_list` in stock_crawler.py to desired value.
