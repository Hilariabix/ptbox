import os

from utils import logger


def fill_extensions(extension, extensions, file, full_path):
    if extension not in extensions:
        extensions[extension] = []
    extensions[extension].append((os.path.getsize(full_path), file))


def get_size_and_amount(extensions):
    length_dict = {key: len(value) for key, value in extensions.items()}
    logger.info(length_dict)
    for extension in extensions:
        extensions[extension].sort(key=lambda size: size[0], reverse=True)
        extensions[extension] = extensions[extension][:10]
    return extensions
