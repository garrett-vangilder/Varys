from re import compile


class BaseParser:
    regex = None

    def __init__(self, regex):
        if not regex:
            raise ValueError(f'Regex not provided to parser. Instead received: {regex}')
        re_genre = r'{}'.format(regex)

        self.regex = compile(re_genre)

    def find_match(self, ):
        raise NotImplementedError('Do not use BaseParser')