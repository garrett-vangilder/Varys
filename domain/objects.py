from json import dumps
from dataclasses import dataclass
from typing import List


@dataclass
class RouteEntry:
    header: object
    html: object
    route: str

    def to_wire(self):
        return {
            'header': dumps(dict(self.header)),
            'element': dumps(self.html),
            'route': self.route
        }


@dataclass
class Payload:
    entries: List[RouteEntry]

    def to_wire(self):
        return {entry.route: entry.to_wire() for entry in self.entries}
