"""
Helper functions to parse command line arguments passed into varys
"""
import logging
import getopt
import sys
from os import path
from typing import Tuple

from exceptions import ArgumentError


class ArgParser:
    """
    Encapsulated command line parser.

    methods:
        - get_options
    """

    @staticmethod
    def get_options(*args, **kwargs) -> Tuple[str, str, str, int]:
        """
        Returns parsed command line arguments / options into varys script
        :return: Tuple[str, str, str, str]
        """

        log_level = logging.ERROR
        domain = None
        regex = None
        route_list = "./config/default.txt"
        output_dir = "./"

        try:
            opts, _ = getopt.getopt(
                sys.argv[1:],
                "hd:r:rl:v:o:",
                ["help", "domain=", "regex=", "route_list=", "verbose", "output="],
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
                elif opt in ("-v", "--verbose"):
                    log_level = logging.INFO
                elif opt in ("-o", "--output"):
                    if not path.exists(arg):
                        raise ArgumentError(
                            f"[ArgumentError] Did not provide a valid output directory output_dir: {arg}"
                        )
                    output_dir = arg

        except ValueError as err:
            raise ArgumentError(str(err)) from err
        except ArgumentError as err:
            raise err

        if not domain:
            raise ArgumentError(
                f"[ArgumentError] Did not provide required parameters domain: {domain}"
            )
        if not regex:
            raise ArgumentError(
                f"[ArgumentError] Did not provide required parameters regex: {regex}"
            )

        return domain, regex, route_list, log_level, output_dir
