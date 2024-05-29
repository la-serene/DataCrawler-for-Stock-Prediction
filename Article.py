import requests


class Article:
    def __init__(self, base_url, topic):
        self.base_url = base_url
        self.topic = topic
        self.metadata = []
        self.hash_table = {}

    def crawl_page(self, page):
        responses = ""

        for i in range(page):
            topic_url = self.base_url + self.topic + "-p{}".format(i + 1)
            response = requests.get(topic_url)
            responses += response.content.decode()

        return responses
