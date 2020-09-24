import os
import argparse
from enum import Enum
from map_files import fill_extensions, get_size_and_amount
from password_extractor import extract_passwords_from_file
from utils import logger


class Task(Enum):
    passwords = 'passwords'
    file_types = 'file_types'

    def __str__(self):
        return self.value


def run(root, task):
    extensions = {}
    for root, dirs, files in os.walk(root):
        for file in files:
            full_path = os.path.join(root, file)
            extension = file.split('.')[-1]
            if task == Task.passwords:
                extract_passwords_from_file(full_path)
            elif task == Task.file_types:
                fill_extensions(extension, extensions, file, full_path)
    if task == Task.file_types:
        logger.info(get_size_and_amount(extensions))


def main():
    parser = argparse.ArgumentParser("Files walker")
    parser.add_argument("--root", required=True, type=os.path.abspath,
                        help="Root directory to walk from")
    parser.add_argument("--task", action="store", required=True, type=Task, choices=list(Task),
                        help="Task to execute")
    args = parser.parse_args()
    run(args.root, args.task)


if __name__ == "__main__":
    main()
