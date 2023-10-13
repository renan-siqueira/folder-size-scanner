# Folder Size Scanner

A python tool to scan directories and log their sizes.

This tool offers both a command-line interface and a graphical user interface.

## Project Structure

- `run.py`: The main entry point for the program. It determines whether to run in GUI or CLI mode.
- `/logs`: A directory to store log files.
- `/src`:
  - `/core`: Contains the main functionality for scanning directories.
  - `/gui`: Contains the graphical user interface code.
  - `/modules`: Houses the various modules supporting the core functionality such as CLI prompts, formatting, logging, and scanning.
  - `/settings`: Configuration and default settings for the application.
  - `/utils`: Utility functions like size conversions.
- `.gitignore`: Git ignore file to exclude specific files/directories from version control.
- `LICENSE`: The license for the project.
- `README.md`: This documentation file.
- `structure.txt`: An overview of the project structure.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run `run.py`.
```bash
python run.py
```

### Command-Line Interface (CLI):

4. When prompted if you want to use the graphical interface, answer 'n' for CLI mode.
5. Follow the on-screen prompts to scan directories.

### Graphical User Interface (GUI):

4. When prompted if you want to use the graphical interface, answer 'y' for GUI mode.
5. A window will appear. Use the interface to select directories and initiate scans.
