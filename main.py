import logging

import sys

from logger import Logger
from parsers.arguments import ArgParser
from exceptions import ArgumentError
from network_request.request import Requester
from domain.objects import Payload, RouteEntry
from parsers.headers import HTTPHeaderParser
from parsers.html import HTMLParser


def main():
    try:
        domain, regex, route_list, log_level = ArgParser.get_options()
        logger = Logger.instance(log_level)
    except ArgumentError as err:
        print(err.msg)
        sys.exit(1)

    logger.info(
        "Running Varys with the following options: domain={domain}, regex={regex}, route_list={route_list}, log_level={log_level}".format(
            domain=domain, regex=regex, route_list=route_list, log_level=log_level
        )
    )

    # define final payload
    payload = Payload(entries=[])

    # build requester, this requires domain and reference to the preferred route_list
    requester = Requester.instance(domain, route_list, logger=logger)
    for url, headers, page in requester.next_page():
        entry = RouteEntry(headers, html=page, route=url)
        http_header_parser = HTTPHeaderParser(regex, logger=logger)
        html_parser = HTMLParser(regex, logger=logger)

        header_match = http_header_parser.find_match(entry)
        html_match = html_parser.find_match(entry)

        if header_match or html_match:
            payload.entries.append(entry)


if __name__ == "__main__":
    main()
