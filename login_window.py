import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from records_window import RecordsWindow
class LoginWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("300x150")
        self.configure(background="#d4d7fa")

        self.username_label = ttk.Label(self, text="Username", font=("Arial",10))
        self.username_label.place(relx=0.1, rely=0.1)
        self.username_entry = ttk.Entry(self)
        self.username_entry.place(relx=0.5, rely=0.1)

        self.password_label = ttk.Label(self, text="Password", font=("Arial",10))
        self.password_label.place(relx=0.1, rely=0.3)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.place(relx=0.5, rely=0.3)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


    def open_records_window(self):
        Records = RecordsWindow()
    def login(self):
        # Implement your login logic here
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the login is successful
        if username == "admin" and password == "password":
            messagebox.showinfo("Success","Successfully Logged In")
            self.open_records_window()      
            self.destroy()
        else:
            messagebox.showerror("Error","Wrong Username or Password")
