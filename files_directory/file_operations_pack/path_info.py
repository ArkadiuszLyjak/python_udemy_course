import os
from pathlib import Path


def print_path_info(path):
    print("Path:", path)
    print("exists:", os.path.exists(path))
    print(os.path.isdir(path))
    print(os.path.dirname(path))
    print(os.path.dirname(__file__))
    print(os.getcwd())

def dirs_in_path_count(p: Path) -> int:
    parent = p.parent
    anchor = parent.anchor

    return sum(1 for part in parent.parts if part and part != anchor)
