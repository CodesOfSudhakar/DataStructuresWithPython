import tkinter as tk  # import library

root = tk.Tk()  # Create a root

root.geometry("400x400+150+150")
root.title("Calculator")
root.resizable(False, False)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.mainloop()
