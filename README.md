# LucidLink Folder Size Scanner

This Python script scans top-level folders within a specified LucidLink directory, calculates the total size of each folder, and displays the sizes in a human-readable format. The script supports concurrent execution to speed up the scanning process and uses `tqdm` for a progress bar during the scan.

## Features

- Scans the LucidLink mount directory to calculate folder sizes.
- Handles large directories with multiple files using concurrent execution (multithreading).
- Displays the folder sizes in MB, GB, or TB for easy readability.
- Includes progress indication with a `tqdm` progress bar.
- Automatically checks if LucidLink is mounted before proceeding.

## Requirements

- Python 3.x
- `tqdm` (for the progress bar)
- `concurrent.futures` (for multithreading, part of the standard library)
- `os` and `pathlib` (standard libraries)

You can install the required libraries using `pip`:

```bash
pip install tqdm
