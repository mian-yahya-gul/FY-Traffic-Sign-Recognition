import tkinter as tk         # GUI toolkit for creating windows, buttons, labels, etc.
import database              # Custom module for database operations (user login/register)
import ui                    # Custom module for building the user interface

# ------------------------------
# Function: main
# Purpose: Entry point of the application
# ------------------------------
def main():
    # Initialize database and create tables if not already present
    database.init_db()

    # Create the main Tkinter window (root window of the application)
    root = tk.Tk()
    root.title("Traffic Sign Prototype")   # Set window title

    # Build the login window inside the root
    ui.build_login_window(root)

    # Start the Tkinter event loop (keeps window running until closed)
    root.mainloop()


# ------------------------------
# Ensures this script runs only when executed directly
# and not when imported as a module
# ------------------------------
if __name__ == "__main__":
    main()
