import logging


class Logger:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls, level=logging.ERROR) -> logging.Logger:
        if cls._instance is None:

            logger = logging.getLogger("varys")

            logger.setLevel(level)

            if level is logging.INFO:
                log_formatter = logging.Formatter(
                    "%(name)s - %(levelname)s - %(message)s"
                )
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(log_formatter)
                logger.addHandler(console_handler)
            cls._instance = logger

        return cls._instance
