import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm


def parse_header(raw_article):
    soup = BeautifulSoup(raw_article, "html.parser")

    title = soup.find("h1", class_="article-detail-title f0")
    datetime = soup.find("span", class_="article-detail-publish")

    return title.text, datetime.text


def parse_paragraph(raw_article):
    soup = BeautifulSoup(raw_article, "html.parser")
    paragraphs = soup.find_all("p")

    content = ""
    for paragraph in paragraphs:
        content += paragraph.text

    return content


def crawl_article_by_numOfPages(num_pages):
    num_pages = num_pages if num_pages <= 236 else 236

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    delay = 10

    topic_url = "https://vietnamtimes.org.vn/economy"
    df = []
    for i in tqdm(range(1, num_pages + 1)):
        page_url = topic_url + "&s_cond=&BRSR={}".format((i - 1) * 20)
        driver.get(page_url)

        WebDriverWait(driver, delay).until(EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "h3.article-title"
        )))
        articles_wrapper = driver.find_element(By.CSS_SELECTOR, "div.col-Left.lt")
        articles_wrapper_raw = articles_wrapper.get_attribute("outerHTML")
        soup = BeautifulSoup(articles_wrapper_raw, "html.parser")

        url_wrappers = soup.find_all("a", class_="article-image")
        for url_wrapper in url_wrappers:
            article_url = url_wrapper.attrs["href"]

            driver.get(article_url)
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "div.google-auto-placed.ap_container")
            ))
            info_wrapper = driver.find_element(By.CSS_SELECTOR, "div.article-detail.fw.clearfix")
            info_wrapper_raw = info_wrapper.get_attribute("outerHTML")
            title, datetime = parse_header(info_wrapper_raw)

            content_wrapper = driver.find_element(By.CSS_SELECTOR, "div#__MB_MASTERCMS_EL_3")
            content_wrapper_raw = content_wrapper.get_attribute("outerHTML")

            content = parse_paragraph(content_wrapper_raw)

            row = {"Title": title, "Datetime": datetime, "Content": content}
            df.append(row)

    # df.to_csv("vntimes.csv")
    print(df)


if __name__ == "__main__":
    crawl_article_by_numOfPages(2)
