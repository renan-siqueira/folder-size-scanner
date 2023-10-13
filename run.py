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
        use_gui = input(settings.MESSAGE_USE_GUI).strip().lower() == 'y'
        if use_gui:
            from src.gui import gui
            gui.start_gui()
        else:
            run_cli_mode()
    except ImportError:
        run_cli_mode()


if __name__ == '__main__':
    main()
