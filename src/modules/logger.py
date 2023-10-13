def save_to_log(sorted_sizes, entry_path, total_size, start_time, end_time, format_size_func, path_scan_log_file):
    with open(path_scan_log_file, 'a', encoding='utf-8') as log_file:
        log_file.write("==========\n")
        log_file.write(f"Scan start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"Input path: {entry_path}\n\n")
        for dirpath, size in sorted_sizes:
            log_file.write(f"{dirpath} - {format_size_func(size)}\n")
        log_file.write(f"\nTotal size of {entry_path}: {format_size_func(total_size)}\n")
        log_file.write(f"Scan end time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write("==========\n\n")
