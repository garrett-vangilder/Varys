import bs4.element

from domain.objects import RouteEntry
from . import BaseParser
from bs4 import BeautifulSoup
from re import IGNORECASE


class HTMLParser(BaseParser):
    def find_match(self, entry: RouteEntry) -> list:
        match = []
        soup = BeautifulSoup(entry.html, "html.parser")
        import pdb

        pdb.set_trace()
        for element in soup.find_all(string=self.regex):
            if type(element) is bs4.element.NavigableString:
                match.append(str(element))
                continue

            for match_ in self.regex.finditer(str(element), IGNORECASE):

                # grab starting and end pos to account for groups
                match.append(match_.string[match_.start() : match_.end()])

        # remove dupes
        match = set(match)
        if match and self.logger:

            self.logger.info(f"[HTMLParser.find_match()] Match found on {entry.route}")
            self.logger.info(f"\n\n{match}\n\n")

        return match
