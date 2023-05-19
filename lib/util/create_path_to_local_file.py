from pathlib import Path

def create_path_to_local_file(sibling_file, file_name):
    parent_path = Path(sibling_file).resolve().parent
    return Path(parent_path, file_name).resolve()
