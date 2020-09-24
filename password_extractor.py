import re
from utils import logger

AFTER_PASS_REGEX = r'(?<=password:\s)(\w+)'


def extract_passwords_from_file(full_path):
    with open(full_path, "r", encoding='utf8') as auto:
        try:
            content = auto.read()
            match_list = re.findall(AFTER_PASS_REGEX, content, re.IGNORECASE)
            if match_list:
                logger.info(match_list)
        except UnicodeDecodeError:
            logger.warning(full_path)