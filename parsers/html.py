from domain.objects import RouteEntry
from . import BaseParser
from bs4 import BeautifulSoup


class HTMLParser(BaseParser):
    def find_match(self, entry: RouteEntry) -> list:
        soup = BeautifulSoup(entry.html, "html.parser")

        return soup.find_all(text=self.regex)
