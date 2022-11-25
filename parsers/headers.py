from domain.objects import RouteEntry
from . import BaseParser
from re import IGNORECASE


class HTTPHeaderParser(BaseParser):
    def find_match(self, entry: RouteEntry) -> bool:
        return self.regex.findall(str(entry.header), IGNORECASE)
