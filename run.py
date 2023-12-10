from src.settings import settings
from src.core.core import run_scan
from src.modules import cli


def run_cli_mode():
    entry_path = cli.get_cli_input(settings.MESSAGE_GET_INPUT_PATH)
    relevant_input = cli.get_cli_input(settings.MESSAGE_GET_RELEVANT_SIZE)

    result = run_scan(entry_path, relevant_input)

    cli.print_scan_summary(
        result['entry_path'],
        result['formatted_total_size'],
    )


def main():
    try:
        cli_mode = input(settings.MESSAGE_USE_GUI).strip().lower() == 'n'
        if cli_mode:
            run_cli_mode()
        else:
            from src.gui import gui
            gui.start_gui()
    except ImportError:
        run_cli_mode()


if __name__ == '__main__':
    main()
