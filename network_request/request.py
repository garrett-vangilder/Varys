from time import sleep

from requests import request
from random import randint
from time import sleep


class Requester(object):
    _instance = None

    current_index = None
    domain = None
    logger = None
    route_file = []

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls, domain=None, route_list=None, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        if not domain:
            raise ValueError("Domain is required")

        cls._instance.domain = domain
        cls.current_index = 0
        cls.logger = kwargs.get("logger")
        cls.protocol = kwargs.get("protocol", "https")

        cls.route_file = open(route_list, "r")

        return cls._instance

    def next_page(self):
        domain = self.domain
        protocol = self.protocol

        while True:
            route = self.route_file.readline().strip("\n")

            if route == "" and self.current_index != 0:
                break

            url = f"{protocol}://{domain}/{route}"

            resp = request("GET", url)

            # request made
            self.current_index += 1

            sleep(randint(0, 1))

            self.logger.info(
                f"[Requester.next_page()] URL: {url} responded {resp.status_code}"
            )
            if resp.status_code == 200:
                yield url, resp.headers, resp.text
