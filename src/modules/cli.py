def get_cli_input(message):
    return input(message)

def print_scan_start_time(start_time):
    print(f"Starting scan at {start_time.strftime('%Y-%m-%d %H:%M:%S')}...")

def print_scan_summary(entry_path, formatted_total_size):
    print(f"Total size of {entry_path}: {formatted_total_size}")
    print('Scan completed! Results saved to log file.')
