import tkinter as tk
import database
import ui

def main():
    database.init_db()
    root = tk.Tk()
    root.title("Traffic Sign Prototype")
    ui.build_login_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
