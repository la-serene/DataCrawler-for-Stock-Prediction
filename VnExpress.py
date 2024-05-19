import requests
import hashlib
from bs4 import BeautifulSoup

from Article import Article


class VnExpress(Article):
    def __init__(self):
        super().__init__("https://vnexpress.net/", "kinh-doanh/chung-khoan")

    def get_article_metadata(self):
        raw_html = self.crawl_raw(num_pages=2)
        soup = BeautifulSoup(raw_html, "html.parser")
        h2_elements = soup.find_all('h2', class_='title-news')

        for element in h2_elements:
            a_tag = element.find("a").attrs
            hashcode = hash(a_tag["title"])
            if self.hash_table.get(hashcode, 0) == 0:
                self.hash_table[hashcode] = 1
                self.metadata.append(a_tag)

        print(self.metadata)
