from tkinter import messagebox
import database

def login_user(username, password, open_upload_window):
    result = database.get_user(username, password)
    if result:
        messagebox.showinfo("Login", "Login Successful!")
        open_upload_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register_user(username, password):
    if database.add_user(username, password):
        messagebox.showinfo("Register", "Registration Successful! Please login.")
    else:
        messagebox.showerror("Register Failed", "Username already exists")
