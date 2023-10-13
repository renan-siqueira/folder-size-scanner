def get_input_path():
    return input("Enter the folder path to start the scan: ")

def get_relevant_size():
    return input("Enter the relevant size for logging (e.g., 1GB, 500MB, 100KB) or press Enter to skip: ")

def print_scan_start_time(start_time):
    print(f"Starting scan at {start_time.strftime('%Y-%m-%d %H:%M:%S')}...")

def print_scan_summary(entry_path, formatted_total_size, path_scan_log_file):
    print(f"Total size of {entry_path}: {formatted_total_size}")
    print(f"Scan completed! Results saved to {path_scan_log_file}")
