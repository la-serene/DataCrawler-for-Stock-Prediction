import datetime
import json

import requests
from bs4 import BeautifulSoup

from Article import Article


class VnExpress(Article):
    def __init__(self):
        super().__init__("https://vnexpress.net/", "kinh-doanh/chung-khoan")

    def get_article_metadata(self):
        raw_html = self.crawl_page(num_pages=1)
        soup = BeautifulSoup(raw_html, "html.parser")
        h2_elements = soup.find_all('h2', class_='title-news')

        for element in h2_elements:
            a_tag = element.find("a").attrs

            # Check if one article already existed in metadata
            hashcode = hash(a_tag["title"])
            if self.hash_table.get(hashcode, 0) == 0:
                self.hash_table[hashcode] = 1
                self.metadata.append(a_tag)

    def crawl_article(self):
        data = {}
        for i, val in enumerate(self.metadata):
            res = requests.get(val["href"]).content.decode()
            soup = BeautifulSoup(res, "html.parser")
            title = soup.find("h1", class_="title-detail").contents[0].text
            passages = soup.findAll("p")
            content = ""
            for j in range(len(passages) - 1):
                content += passages[j].contents[0].text

            data[i] = {
                "title": title,
                "content": content
            }

        today = datetime.datetime.now()
        year = today.year
        month = today.month
        day = today.day
        filename = "./data/article-{}-{}-{}.json".format(year, month, day)
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
