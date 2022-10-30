from requests import request


class Requester(object):
    _instance = None
    current_index = None
    domain = None
    routes = []

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, domain=None):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        if not domain:
            raise ValueError('Domain is required')

        # init
        cls._instance.domain = domain
        cls.current_index = 0

        # TODO implement route parser from external dictionarys
        cls.routes = ['about', 'careers', 'app']

        return cls._instance

    def next_page(self):
        domain = self.domain

        while True:
            route = self.routes[self.current_index]
            resp = request('GET', f'http://{domain}/{route}')
            self.current_index += 1

            if resp.status_code == 200:
                yield resp.headers, resp.text
            if self.current_index >= len(self.routes):
                break
