from VnExpress import VnExpress


def main():
    vnexpress = VnExpress()
    vnexpress.get_article_metadata()
    vnexpress.crawl_article()


if __name__ == "__main__":
    main()
