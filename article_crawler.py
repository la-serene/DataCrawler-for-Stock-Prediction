from VnExpress import VnExpress
import requests
from bs4 import BeautifulSoup

def main():
    # vnexpress = VnExpress()
    # article_list = vnexpress.get_article_metadata()
    c = requests.get("https://www.investing.com/markets/vietnam").content
    s = BeautifulSoup(c, "html.parser")
    co = s.findAll("td")
    for i in co:
        print(i)
    pass


if __name__ == "__main__":
    main()
