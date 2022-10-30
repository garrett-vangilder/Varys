import sys
from argument_parser.parser import ArgParser
from exceptions import ArgumentError
from network_request.request import Requester


def main(argv):
    print('Initializing Varys')

    try:
        domain, regex = ArgParser.get_options(argv)
    except ArgumentError as err:
        print(err.msg)
        sys.exit(1)

    print(f'Target domain: {domain}')
    print(f'Target regex: {regex}')

    requester = Requester.instance(domain)
    while True:
        next_page = requester.next_page()

        if not next_page:
            print('finish enumeration')
            break



if __name__ == '__main__':
    main(sys.argv)
