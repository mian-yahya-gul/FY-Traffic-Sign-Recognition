import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import recognition
import auth

def open_upload_window(root):
    upload_window = tk.Toplevel(root)
    upload_window.title("Traffic Sign Recognition")

    label_img = tk.Label(upload_window)
    label_img.pack()

    label_result = tk.Label(upload_window, text="Prediction: ")
    label_result.pack()

    def upload_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            label_img.config(image=img_tk)
            label_img.image = img_tk
            prediction = recognition.dummy_recognition()
            label_result.config(text=f"Prediction: {prediction}")

    btn_upload = tk.Button(upload_window, text="Upload Traffic Sign", command=upload_image)
    btn_upload.pack()

def build_login_window(root):
    tk.Label(root, text="Username:").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    btn_login = tk.Button(root, text="Login", command=lambda: auth.login_user(
        entry_username.get(), entry_password.get(), lambda: open_upload_window(root)))
    btn_login.pack()

    btn_register = tk.Button(root, text="Register", command=lambda: auth.register_user(
        entry_username.get(), entry_password.get()))
    btn_register.pack()
