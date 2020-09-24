import logging


def get_logger():
    lgr = logging.getLogger(__name__)
    lgr.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    lgr.addHandler(file_handler)
    return lgr


logger = get_logger()
