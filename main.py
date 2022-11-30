import sys
from datetime import datetime as dt

from logger import Logger
from output.json_file_write import JSONSerializer
from parsers.arguments import ArgParser
from exceptions import ArgumentError
from network_request.request import Requester
from domain.objects import Payload, RouteEntry
from parsers.headers import HTTPHeaderParser
from parsers.html import HTMLParser


def main():
    try:
        domain, regex, route_list, log_level, output_path = ArgParser.get_options()
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
        entry = RouteEntry(headers, html=page, route=url, match=set())
        http_header_parser = HTTPHeaderParser(regex, logger=logger)
        html_parser = HTMLParser(regex, logger=logger)

        header_match = http_header_parser.find_match(entry) or set()
        html_match = html_parser.find_match(entry) or set()

        entry.match = entry.match.union(header_match)
        entry.match = entry.match.union(html_match)

        if entry.match:
            payload.entries.append(entry)

            now = dt.now().strftime("%Y-%m-%dT%H:%M:%S")

            file_name = f"{domain}_{now}.json"
            # write to file
            JSONSerializer.to_file(
                payload.to_wire(), output_path, file_name=file_name, logger=logger
            )


if __name__ == "__main__":
    main()
