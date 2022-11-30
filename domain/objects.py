from json import dumps, loads
from dataclasses import dataclass
from typing import List, Set


@dataclass
class RouteEntry:
    header: object
    html: object
    route: str
    match: Set[str]

    def to_wire(self):
        return {
            "match": list(self.match),
            "route": self.route,
        }


@dataclass
class Payload:
    entries: List[RouteEntry]

    def to_wire(self):
        return {entry.route: entry.to_wire() for entry in self.entries}
