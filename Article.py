import requests


class Article:
    def __init__(self, base_url, topic):
        self.base_url = base_url
        self.topic = topic
        self.metadata = []
        self.hash_table = {}

    def crawl_raw(self, num_pages):
        responses = ""

        for i in range(num_pages):
            topic_url = self.base_url + self.topic + "-p{}".format(i + 1)
            response = requests.get(topic_url)
            responses += response.content.decode()

        return responses
