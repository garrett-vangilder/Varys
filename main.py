import sys
from parsers.arguments import ArgParser
from exceptions import ArgumentError
from network_request.request import Requester
from domain.objects import Payload, RouteEntry
from parsers.headers import HTTPHeaderParser
from parsers.html import HTMLParser


def main(argv):
    try:
        domain, regex = ArgParser.get_options(argv)
    except ArgumentError as err:
        print(err.msg)
        sys.exit(1)

    payload = Payload(entries=[])
    requester = Requester.instance(domain)
    for url, headers, page in requester.next_page():
        entry = RouteEntry(headers, html=page, route=url)
        http_header_parser = HTTPHeaderParser(regex)
        html_parser = HTMLParser(regex)

        header_match = http_header_parser.find_match(entry)
        html_match = html_parser.find_match(entry)

        if header_match or html_match:
            payload.entries.append(entry)


if __name__ == '__main__':
    main(sys.argv)
