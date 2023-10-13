import os

def get_size_of_files_in_dir(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
    return total

def list_folders_with_size(start_path):
    sizes = {}
    for dirpath, _, _ in os.walk(start_path):
        folder_size = get_size_of_files_in_dir(dirpath)
        sizes[dirpath] = folder_size
    return sizes

def get_sorted_sizes(sizes, relevant_size=None):
    if relevant_size:
        return sorted(
            [(dirpath, size) for dirpath, size in sizes.items() if size >= relevant_size], 
            key=lambda x: x[1],
            reverse=True
        )
    else:
        return sorted(sizes.items(), key=lambda x: x[1], reverse=True)
