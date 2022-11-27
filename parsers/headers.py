from domain.objects import RouteEntry
from . import BaseParser
from re import IGNORECASE


class HTTPHeaderParser(BaseParser):
    def find_match(self, entry: RouteEntry) -> bool:
        match = []
        for match_ in self.regex.finditer(str(entry.header), IGNORECASE):
            # grab starting and end pos to account for groups
            match.append(match_.string[match_.start() : match_.end()])

        # remove dupes
        match = set(match)

        if match and self.logger:
            self.logger.info(
                f"[HTTPHeaderParser.find_match()] Match found on {entry.route}"
            )
            self.logger.info(f"\n\n{match}\n\n")

        return match
