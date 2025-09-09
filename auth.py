from tkinter import messagebox   # Used to show popup messages (info, error)
import database                  # Import database functions (user storage, retrieval)

# ------------------------------
# Function: login_user
# Purpose: Validate login credentials by checking them against the database.
# Arguments:
#   username (str) - entered username
#   password (str) - entered password
#   open_upload_window (function) - callback to open next window on success
# ------------------------------
def login_user(username, password, open_upload_window):
    # Check if the username/password exists in the database
    result = database.get_user(username, password)

    if result:
        # If user exists → show success message
        messagebox.showinfo("Login", "Login Successful!")
        # Open the next screen (image upload window)
        open_upload_window()
    else:
        # If credentials are wrong → show error
        messagebox.showerror("Login Failed", "Invalid username or password")


# ------------------------------
# Function: register_user
# Purpose: Register a new user by adding username and password into database.
# Arguments:
#   username (str) - chosen username
#   password (str) - chosen password
# ------------------------------
def register_user(username, password):
    # Try to add the new user into database
    if database.add_user(username, password):
        # If added successfully → show success message
        messagebox.showinfo("Register", "Registration Successful! Please login.")
    else:
        # If username already exists (IntegrityError) → show error
        messagebox.showerror("Register Failed", "Username already exists")
