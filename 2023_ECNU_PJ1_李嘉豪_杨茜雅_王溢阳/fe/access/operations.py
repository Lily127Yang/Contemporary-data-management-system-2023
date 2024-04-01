import requests
from urllib.parse import urljoin


class Operations:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "operations/")

    def set_delivery(self, order_id, store_id, store_owner_id, password):
        json = {"order_id": order_id, "store_id": store_id, "store_owner_id": store_owner_id, "password": password}
        url = urljoin(self.url_prefix, "delivery")
        r = requests.post(url, json=json)
        return r.status_code

    def set_receipt(self, order_id, user_id, password) -> int:
        json = {"order_id": order_id, "user_id": user_id, "password": password}
        url = urljoin(self.url_prefix, "receipt")
        r = requests.post(url, json=json)
        return r.status_code

    def order_lookup(self, order_id, user_id, password) -> int:
        json = {"order_id": order_id, "user_id": user_id, "password": password}
        url = urljoin(self.url_prefix, "lookup")
        r = requests.post(url, json=json)
        return r.status_code

    def order_cancer(self, order_id, user_id, password) -> int:
        json = {"order_id": order_id, "user_id": user_id, "password": password}
        url = urljoin(self.url_prefix, "cancer")
        r = requests.post(url, json=json)
        return r.status_code

    def book_search(self, keyword, how, store_id="") -> int:
        json = {"keyword": keyword, "how": how, "store_id": store_id}
        url = urljoin(self.url_prefix, "search")
        r = requests.post(url, json=json)
        return r.status_code

    def book_recommend(self, user_id, password) -> int:
        json = {"user_id": user_id, "password": password}
        url = urljoin(self.url_prefix, "recommend")
        r = requests.post(url, json=json)
        return r.status_code