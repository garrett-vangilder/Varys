import sys
from argument_parser.parser import ArgParser
from exceptions import ArgumentError
from network_request.request import Requester


def main(argv):
    try:
        domain, regex = ArgParser.get_options(argv)
    except ArgumentError as err:
        print(err.msg)
        sys.exit(1)

    requester = Requester.instance(domain)
    for headers, page in requester.next_page():
        pass

if __name__ == '__main__':
    main(sys.argv)
