import getopt
import sys

from exceptions import ArgumentError
from re import escape


class ArgParser:

    @staticmethod
    def get_options(argv):
        """"""
        domain = None
        regex = None

        try:
            opts, args = getopt.getopt(sys.argv[1:], "hd:r:", ["help", "domain=", "regex="])
            for opt, arg in opts:
                if opt == '-h':
                    print('test.py -d <domain> -r <regex>')
                    sys.exit()
                elif opt in ("-d", "--domain"):
                    domain = arg
                elif opt in ("-r", "--regex"):
                    # regex = r'' + escape(arg) + ''
                    regex = arg
        except ValueError as err:
            raise ArgumentError(err)

        if not domain:
            raise ArgumentError(f"[ArgumentError] Did not provide required parameters domain: {domain}")
        if not regex:
            raise ArgumentError(f"[ArgumentError] Did not provide required parameters regex: {regex}")

        return domain, regex
