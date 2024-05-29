import json
import datetime
import os

if "ACCEPT_TC" not in os.environ:
    os.environ["ACCEPT_TC"] = "tôi đồng ý"

from vnstock3 import *


def main(start_date, end_date):
    """
        Crawl stock by OCHLV.
        Date should follow yy-mm-dd format.
    :return:
    """
    stock_list = ["FPT", "VCB", "HPG", "VPB", "VNM", "VIC"]

    with open("./data/stock.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for i in stock_list:
        stock = Vnstock().stock(symbol=i, source='VCI')
        df = stock.quote.history(start=start_date, end=end_date, interval='1D')
        df['time'] = df['time'].dt.strftime('%Y-%m-%d')
        data[i] = df.to_dict(orient='list')

    with open('./data/stock.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(data)


if __name__ == '__main__':
    start_date = input("Enter start date (yy-mm-dd):")
    if start_date == "\n":
        start_date = "2020-01-01"

    end_date = input("Enter end date (yy-mm-dd): ")
    if end_date == "\n":
        end_date = "2024-12-31"

    main(start_date, end_date)
