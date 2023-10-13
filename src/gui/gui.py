import tkinter as tk
from tkinter import filedialog, messagebox

from src.settings import settings
from src.core.core import run_scan


def start_gui():
    window = tk.Tk()
    window.title(settings.WINDOW_TITLE)
    window.geometry(settings.WINDOW_SIZE)

    def select_folder():
        folder = filedialog.askdirectory()
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)

    tk.Label(window, text=settings.MESSAGE_GET_INPUT_PATH).pack(pady=10)
    path_entry = tk.Entry(window, width=50)
    path_entry.pack(pady=10)

    select_button = tk.Button(window, text="Select Folder", command=select_folder)
    select_button.pack(pady=5)

    tk.Label(window, text=settings.MESSAGE_GET_RELEVANT_SIZE).pack(pady=10)
    size_entry = tk.Entry(window, width=50)
    size_entry.pack(pady=10)

    result_frame = tk.Frame(window, pady=20)
    result_frame.pack(fill="both", expand=True)

    def on_scan_click():
        folder_path = path_entry.get()
        size = size_entry.get()

        results = run_scan(folder_path, size)
        if results:
            for widget in result_frame.winfo_children():
                widget.destroy()

            tk.Label(result_frame, text=f"Folder Path: {results['entry_path']}").pack(anchor="w")
            tk.Label(
                result_frame, text=f"Total Size: {results['formatted_total_size']}"
            ).pack(anchor="w")
        else:
            messagebox.showerror("Error", "Scan failed!")

    scan_button = tk.Button(window, text="Start Scan", command=on_scan_click)
    scan_button.pack(pady=20)

    window.mainloop()


if __name__ == '__main__':
    start_gui()
