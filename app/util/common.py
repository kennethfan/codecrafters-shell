import os
from typing import List, Optional


def expand_path() -> List[str]:
    """
    expand PATH to directories
    :return:
    """
    path = os.getenv('PATH')
    if path is None:
        return []
    path = path.strip()
    if '' == path:
        return []
    return path.split(':')


def find_command(command: str) -> Optional[str]:
    """
    find command with in PATH
    :param command:
    :return:
    """
    directory_list = expand_path()
    for directory in directory_list:
        directory = directory.strip()
        if not os.path.exists(directory):
            continue
        for _, _, files in os.walk(directory):
            if command in files:
                return os.path.join(directory, command)
    return None
