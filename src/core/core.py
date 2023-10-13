import os
import datetime

from src.settings.settings import PATH_SCAN_LOG_FILE
from src.modules import scanner, formatter, logger
from src.utils import utils


def run_scan(entry_path, relevant_input):
    relevant_size = utils.convert_size_to_bytes(relevant_input) if relevant_input else None

    start_time = datetime.datetime.now()

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

    summary = {
        "entry_path": entry_path,
        "formatted_total_size": formatter.format_size(total_size),
    }
    return summary
