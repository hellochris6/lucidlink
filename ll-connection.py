import os
import concurrent.futures
from tqdm import tqdm 

LUCIDLINK_PATH = "#"

def is_lucidlink_mounted():
    return os.path.ismount(LUCIDLINK_PATH)

def calculate_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            try:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
            except (FileNotFoundError, PermissionError):
                continue
    return os.path.basename(folder_path), round(total_size / (1024 * 1024), 2)  # MB

def get_top_level_folder_sizes(base_path):
    folder_paths = [
        os.path.join(base_path, name)
        for name in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, name)) and not name.startswith('.')
    ]

    folder_sizes = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(calculate_folder_size, path): path for path in folder_paths}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Scanning folders"):
            folder_name, size = future.result()
            folder_sizes[folder_name] = size

    return folder_sizes

def format_size_mb(size_mb):
    if size_mb >= 1024 * 1024:
        return f"{size_mb / (1024 * 1024):.2f} TB"
    elif size_mb >= 1024:
        return f"{size_mb / 1024:.2f} GB"
    else:
        return f"{size_mb:.2f} MB"

if is_lucidlink_mounted():
    print("✅ LucidLink is mounted.\n")
    sizes = get_top_level_folder_sizes(LUCIDLINK_PATH)
    for folder, size in sizes.items():
        print(f"{folder}: {format_size_mb(size)}")
else:
    print("⚠️ LucidLink is NOT mounted.")
