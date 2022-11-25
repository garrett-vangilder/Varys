"""
Helper functions to parse command line arguments passed into varys
"""
import getopt
import sys
from typing import Tuple

from exceptions import ArgumentError


class ArgParser:
    """
    Encapsulated command line parser.

    methods:
        - get_options
    """

    @staticmethod
    def get_options() -> Tuple[str, str, str]:
        """
        Returns parsed command line arguments / options into varys script
        :return: Tuple[str, str, str]
        """
        domain = None
        regex = None
        route_list = "./config/default.txt"

        try:
            opts, _ = getopt.getopt(
                sys.argv[1:], "hd:r:rl:", ["help", "domain=", "regex=", "route_list="]
            )
            for opt, arg in opts:
                if opt == "-h":
                    print("test.py -d <domain> -r <regex>")
                    sys.exit()
                elif opt in ("-d", "--domain"):
                    domain = arg
                elif opt in ("-r", "--regex"):
                    regex = arg
                elif opt in ("-rl", "--route_list"):
                    route_list = arg

        except ValueError as err:
            raise ArgumentError(str(err)) from err

        if not domain:
            raise ArgumentError(
                f"[ArgumentError] Did not provide required parameters domain: {domain}"
            )
        if not regex:
            raise ArgumentError(
                f"[ArgumentError] Did not provide required parameters regex: {regex}"
            )

        return domain, regex, route_list
