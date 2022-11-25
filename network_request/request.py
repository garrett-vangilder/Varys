from time import sleep

from requests import request
from random import randint
from time import sleep


class Requester(object):
    _instance = None

    current_index = None
    domain = None
    route_file = []

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls, domain=None, route_list=None):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        if not domain:
            raise ValueError("Domain is required")

        cls._instance.domain = domain
        cls.current_index = 0

        cls.route_file = open(route_list, "r")

        return cls._instance

    def next_page(self):
        domain = self.domain

        while True:
            route = self.route_file.readline().strip("\n")

            if route == "" and self.current_index != 0:
                break

            url = f"http://{domain}/{route}"
            resp = request("GET", url)

            # request made
            self.current_index += 1

            sleep(randint(0, 1))

            if resp.status_code == 200:
                yield url, resp.headers, resp.text
