import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import recognition   # Our dummy recognition module
import auth          # Authentication module (login & registration)

# ------------------------------
# Function: open_upload_window
# Purpose: Opens a new window where the user can upload a traffic sign image 
#          and see a dummy recognition result.
# ------------------------------
def open_upload_window(root):
    # Create a new top-level window (child of the main window)
    upload_window = tk.Toplevel(root)
    upload_window.title("Traffic Sign Recognition")

    # Label to display the uploaded image
    label_img = tk.Label(upload_window)
    label_img.pack()

    # Label to display the prediction result
    label_result = tk.Label(upload_window, text="Prediction: ")
    label_result.pack()

    # Inner function: handle image upload and recognition
    def upload_image():
        # Open file dialog to let user pick an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            # Open and resize the selected image
            img = Image.open(file_path)
            img = img.resize((200, 200))   # Resize to 200x200 for display
            img_tk = ImageTk.PhotoImage(img)

            # Display the image inside the label
            label_img.config(image=img_tk)
            label_img.image = img_tk   # Keep reference to avoid garbage collection

            # Get dummy prediction (for prototype)
            prediction = recognition.dummy_recognition()
            label_result.config(text=f"Prediction: {prediction}")

    # Upload button (click → run upload_image)
    btn_upload = tk.Button(upload_window, text="Upload Traffic Sign", command=upload_image)
    btn_upload.pack()


# ------------------------------
# Function: build_login_window
# Purpose: Create the login/registration interface on the main window.
# ------------------------------
def build_login_window(root):
    # Username label + input field
    tk.Label(root, text="Username:").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    # Password label + input field (masked with *)
    tk.Label(root, text="Password:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    # Login button
    # On click → call auth.login_user(), pass username, password,
    # and a callback function (open_upload_window) if login is successful
    btn_login = tk.Button(root, text="Login", command=lambda: auth.login_user(
        entry_username.get(), entry_password.get(), lambda: open_upload_window(root)))
    btn_login.pack()

    # Register button
    # On click → call auth.register_user() with entered username and password
    btn_register = tk.Button(root, text="Register", command=lambda: auth.register_user(
        entry_username.get(), entry_password.get()))
    btn_register.pack()
