import tkinter as tk
from tkinter import ttk
from data_manager import DataManager

class RecordsWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Access Records")
        self.geometry("800x600")
        self.configure(background="#d4d7fa")

        self.search_label = ttk.Label(self, text="Search:", font=("Arial", 10))
        self.search_label.pack()

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack()

        self.treeview_frame = ttk.Frame(self)
        self.treeview_frame.pack(fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(self.treeview_frame)
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.treeview_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.treeview.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.configure(xscrollcommand=self.scrollbar_x.set)

        self.setup_treeview()
        self.load_data()

        self.search_var.trace("w", self.search_data)

    def setup_treeview(self):
        self.treeview["columns"] = (
            "First Question",
            "Second Question",
            "Third Question",
            "Fourth Question",
            "Fifth Question",
            "Respondent Name",
            "Email Address",
            "Contact Number",
            "Contact Person Name",
            "Contact Person Contact Number",
            "Contact Person Email Address",
            "Relationship",
            "Submit Time"
        )

        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0", width=50)

        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
            self.treeview.column(column, width=150)

    def load_data(self):
        # Load data from the "data.csv" file using DataManager
        data = DataManager.load_data('data.csv')

        # Insert data into the Treeview
        for index, record in enumerate(data, start=1):
            self.treeview.insert("", "end", text=str(index), values=record)

    def search_data(self, *args):
        search_text = self.search_var.get().lower()

        # Clear previous search results
        self.treeview.delete(*self.treeview.get_children())

        # Load data from the "data.csv" file using DataManager
        data = DataManager.load_data('data.csv')

        # Search and insert matching data into the Treeview
        for index, record in enumerate(data, start=1):
            if search_text in str(record).lower():
                self.treeview.insert("", "end", text=str(index), values=record)

