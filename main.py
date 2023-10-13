import datetime
from settings import PATH_SCAN_LOG_FILE
from src import cli, scanner, formatter, utils, logger

def main():
    entry_path = cli.get_input_path()
    relevant_input = cli.get_relevant_size()

    relevant_size = utils.convert_size_to_bytes(relevant_input) if relevant_input else None

    start_time = datetime.datetime.now()
    cli.print_scan_start_time(start_time)

    sizes = scanner.list_folders_with_size(entry_path)
    sorted_sizes = scanner.get_sorted_sizes(sizes, relevant_size)

    end_time = datetime.datetime.now()
    total_size = sum(sizes.values())

    logger.save_to_log(
        sorted_sizes,
        entry_path,
        total_size,
        start_time,
        end_time,
        formatter.format_size,
        PATH_SCAN_LOG_FILE
    )
    cli.print_scan_summary(entry_path, formatter.format_size(total_size), PATH_SCAN_LOG_FILE)

if __name__ == '__main__':
    main()
