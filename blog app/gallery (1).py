import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # You must have 'pip install Pillow' installed

class GalleryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="🖼️ Gallery", font=("Arial", 20), bg="#2E86AB", fg="white").pack(fill="x")
        
        # 1. Create the Listbox
        self.lb = tk.Listbox(self, height=5)
        self.lb.pack(fill="x", padx=20, pady=10)
        
        # Add your paths here
        self.lb.insert(tk.END, r"C:\Users\masir\OneDrive\Desktop\MTIS\Tkinter\sunrise.png")
        self.lb.insert(tk.END, "Tech.png")
        self.lb.insert(tk.END, "Coding.gif")
        
        # 2. Bind the selection event (runs show_image when clicked)
        self.lb.bind('<<ListboxSelect>>', self.show_image)
        
        # 3. Create the Canvas for preview
        self.preview = tk.Canvas(self, bg="white", height=200)
        self.preview.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Initial text
        self.placeholder_text = self.preview.create_text(250, 100, text="Select an image to preview")

    def show_image(self, event):
        # Get the selected file path from listbox
        try:
            selection = self.lb.curselection()
            if not selection:
                return
                
            file_path = self.lb.get(selection[0])
            
            # Load the image using PIL
            img = Image.open(file_path)
            
            # Resize image to fit the canvas while maintaining aspect ratio
            img.thumbnail((450, 180)) 
            
            # Convert to Tkinter-compatible format
            self.photo = ImageTk.PhotoImage(img)
            
            # Clear canvas and show image
            self.preview.delete("all")
            self.preview.create_image(250, 100, image=self.photo, anchor="center")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Gallery Preview")
    root.geometry("500x450")
    GalleryPage(root, root).pack(fill="both", expand=True)
    root.mainloop()