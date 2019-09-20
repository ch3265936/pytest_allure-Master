import logging
from setting import Setting as ST

def init_logging():
    logger = logging.getLogger(ST.APP)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt='[%(asctime)s][%(levelname)s]<%(name)s> %(message)s',
        datefmt='%I:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = init_logging()


# def get_logger(name):
#     logger = logging.getLogger(name)
#     return logger
