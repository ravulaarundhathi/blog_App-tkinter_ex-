import tkinter as tk
from tkinter import ttk

class PostsTreeviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tree = ttk.Treeview(self, columns=('Author', 'Date'))
        tree.heading('#0', text='Title')
        tree.heading('Author', text='Author')
        tree.heading('Date', text='Date')
        
        tech = tree.insert("", "end", text="Technology", open=True)
        tree.insert(tech, "end", text="Python 2026", values=("Admin", "Jan 27"))
        
        life = tree.insert("", "end", text="Lifestyle", open=True)
        tree.insert(life, "end", text="Morning Coffee", values=("User1", "Jan 25"))
        
        tree.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    PostsTreeviewPage(root, root).pack(fill="both", expand=True)
    root.mainloop()