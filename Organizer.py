import os
import tkinter as tk
import tkinter.filedialog

class Organizer(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.quenue = []

        self.master = master
        self.master.title('File Organizer')
        self.master.geometry('445x480')
        self.create_widgets()

    def create_widgets(self):
        DROPDOWN_WIDTH = 10
        ENTRY_WIDTH = 70
        HEADING_FONT = ("Arial Bold", 18)
        BTN_FONT = ("Arial", 9)
        LIST_FONT = ("Arial", 8)

        curr_row = 0

        # Create widgets for settings
        settings_label = tk.Label(self.master, text='Settings', font=HEADING_FONT)

        organize_by_label = tk.Label(self.master, text='Organize By', font=BTN_FONT)
        self.organize_by = tk.StringVar(self.master)
        self.organize_by.set('none')
        organize_by_dropdown = tk.OptionMenu(self.master, self.organize_by, 'none', 'year', 'month', 'day', 'name', 'extension', 'category')
        organize_by_dropdown.configure(width=DROPDOWN_WIDTH)

        rename_by_label = tk.Label(self.master, text='Rename Files By', font=BTN_FONT)
        self.rename_by = tk.StringVar(self.master)
        self.rename_by.set('none')
        rename_by_dropdown = tk.OptionMenu(self.master, self.rename_by, 'none', 'yyyy-mm-dd', 'sterilize (-)', 'sterilize (_)')
        rename_by_dropdown.configure(width=DROPDOWN_WIDTH)

        warn_label = tk.Label(self.master, text='Show Warnings', font=BTN_FONT)
        self.show_warnings = tk.StringVar(self.master)
        self.show_warnings.set('yes')
        warn_dropdown = tk.OptionMenu(self.master, self.show_warnings, 'yes', 'no')
        warn_dropdown.configure(width=DROPDOWN_WIDTH)

        # Display widgets for settings
        settings_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        curr_row += 1
        organize_by_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        organize_by_dropdown.grid(row=curr_row, column=1, padx=10, sticky=tk.W)
        curr_row += 1
        rename_by_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        rename_by_dropdown.grid(row=curr_row, column=1, padx=10, sticky=tk.W)
        curr_row += 1
        warn_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        warn_dropdown.grid(row=curr_row, column=1, padx=10, sticky=tk.W)
        curr_row += 1

        # Create widgets for adding folders
        add_dir_label = tk.Label(self.master, text='Add Folder', font=HEADING_FONT)
        self.add_dir_entry = tk.Entry(self.master, textvariable=tk.StringVar(), width=ENTRY_WIDTH)
        browse_dir_btn = tk.Button(self.master, text='Browse', font=BTN_FONT, command=self.browse_dir, width=10)
        add_dir_btn = tk.Button(self.master, text='Add', font=BTN_FONT, command=self.add_dir, width=10)

        # Display widgets for adding folders
        add_dir_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        curr_row += 1
        self.add_dir_entry.grid(row=curr_row, column=0, columnspan=3, padx=10, sticky=tk.W)
        curr_row += 1
        browse_dir_btn.grid(row=curr_row, column=0, padx=10, sticky=tk.EW)
        add_dir_btn.grid(row=curr_row, column=1, sticky=tk.EW)

        # Create widgets for adding files
        add_file_label = tk.Label(self.master, text='Add Files', font=HEADING_FONT)
        self.add_file_entry = tk.Entry(self.master, textvariable=tk.StringVar(), width=ENTRY_WIDTH)
        browse_file_btn = tk.Button(self.master, text='Browse', font=BTN_FONT, command=self.browse_file, width=10)
        add_file_btn = tk.Button(self.master, text='Add', font=BTN_FONT, command=self.add_file, width=10)

        # Display widgets for adding files
        curr_row += 1
        add_file_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        curr_row += 1
        self.add_file_entry.grid(row=curr_row, column=0, columnspan=3, padx=10, sticky=tk.W)
        curr_row += 1
        browse_file_btn.grid(row=curr_row, column=0, padx=10, sticky=tk.EW)
        add_file_btn.grid(row=curr_row, column=1, sticky=tk.EW)

        # Create widgets for quenue
        add_file_label = tk.Label(self.master, text='Quenue', font=HEADING_FONT)
        quenue_items = tk.StringVar(value=self.quenue)
        self.quenue_listbox = tk.Listbox(self.master, listvariable=quenue_items, selectmode='multiple', font=LIST_FONT, width=ENTRY_WIDTH)
        organize_btn = tk.Button(self.master, text='Organize', font=BTN_FONT, command=self.organize_quenue, width=10)
        delete_btn = tk.Button(self.master, text='Delete', font=BTN_FONT, command=self.update_quenue, width=10)
        clear_quenue_btn = tk.Button(self.master, text='Clear', font=BTN_FONT, command=self.clear_quenue, width=10)

        # Display widgets for quenue
        curr_row += 1
        add_file_label.grid(row=curr_row, column=0, padx=10, sticky=tk.W)
        curr_row += 1
        self.quenue_listbox.grid(row=curr_row, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)
        curr_row += 1
        organize_btn.grid(row=curr_row, column=0, sticky=tk.E)
        delete_btn.grid(row=curr_row, column=1)
        clear_quenue_btn.grid(row=curr_row, column=2, sticky=tk.W)

    def organize_quenue(self):
        organize_by = self.organize_by.get()
        if organize_by == 'none':
            pass
        elif organize_by == 'year':
            pass
        elif organize_by == 'month':
            pass
        elif organize_by == 'day':
            pass
        elif organize_by == 'name':
            pass
        elif organize_by == 'extension':
            pass
        elif organize_by == 'category':
            pass
        self.clear_quenue()

    def display_quenue(self):
        self.quenue_listbox.delete(0, 'end')
        for i, path in enumerate(self.quenue):
            self.quenue_listbox.insert(i, path)

    def clear_quenue(self):
        self.quenue = []
        self.display_quenue()

    def update_quenue(self):
        selected_indices = self.quenue_listbox.curselection()
        for i in selected_indices[::-1]:
            del self.quenue[i]
        self.display_quenue()

    def browse_dir(self):
        dir_path = tk.filedialog.askdirectory(mustexist=True)
        self.add_dir_entry.delete(0, 'end')
        self.add_dir_entry.insert(0, f'"{dir_path}"')

    def browse_file(self):
        files = tk.filedialog.askopenfiles()
        file_paths = []
        for file in files:
            file_paths.append(file.name)
        self.add_file_entry.delete(0, 'end')
        file_paths = '","'.join(file_paths)
        self.add_file_entry.insert(0, f'"{file_paths}"')

    def add_dir(self):
        path = self.add_dir_entry.get()[1:-1]
        if not self.is_valid_path(path, 'dir'):
            self.warning(f'No folder could be found at "{path}"!')
            self.add_dir_entry.delete(0, 'end')
            return
        if path in self.quenue:
            self.warning(f'The folder at "{path}" is already in the quenue!')
            self.add_dir_entry.delete(0, 'end')
            return

        self.quenue.append(path)
        self.add_dir_entry.delete(0, 'end')
        self.display_quenue()

    def add_file(self):
        file_paths = []
        for path in self.add_file_entry.get()[1:-1].split('","'):
            if not self.is_valid_path(path, 'file'):
                self.warning(f'No file could be found at "{path}"!')
                continue
            if path in self.quenue:
                self.warning(f'The file at "{path}" is already in the quenue!')
                continue
            file_paths.append(path)
        self.quenue += file_paths
        self.add_file_entry.delete(0, 'end')
        self.display_quenue()

    def is_valid_path(self, path, expected_type):
        if not path:
            return False
        if not os.path.exists(path):
            return False
        if expected_type == 'dir' and not os.path.isdir(path):
            return False
        if expected_type == 'file' and not os.path.isfile(path):
            return False
        return True

    def warning(self, body):
        if self.show_warnings.get() == 'yes':
            tk.messagebox.showwarning('Warning!', body)

    def error(self, body):
        tk.messagebox.showwarning('Error!', body)


if __name__ == '__main__':
    try:
        root = tk.Tk()
        organizer = Organizer(master=root)
        organizer.mainloop()
    except Exception as e:
        tk.messagebox.showerror('Error!', f'Failed to launch organizer: {e}')
