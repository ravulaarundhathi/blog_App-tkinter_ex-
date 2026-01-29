import tkinter as tk
from tkinter import ttk, messagebox

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Header - Using Green color to distinguish from Login
        header = tk.Frame(self, bg="#06A77D")
        header.pack(fill="x", padx=0, pady=0)
        tk.Label(header, text="📝 Create Account", font=("Helvetica", 24, "bold"), 
                bg="#06A77D", fg="white").pack(pady=20)
        
        # Form frame
        form_frame = ttk.Frame(self)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Full Name
        ttk.Label(form_frame, text="Full Name:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.fullname_entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=35)
        self.fullname_entry.pack(anchor="w", pady=(0, 12))
        
        # Email
        ttk.Label(form_frame, text="Email:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.email_entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=35)
        self.email_entry.pack(anchor="w", pady=(0, 12))
        
        # Username
        ttk.Label(form_frame, text="Username:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.username_entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=35)
        self.username_entry.pack(anchor="w", pady=(0, 12))
        
        # Password
        ttk.Label(form_frame, text="Password:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.password_entry = ttk.Entry(form_frame, show="•", font=("Helvetica", 10), width=35)
        self.password_entry.pack(anchor="w", pady=(0, 12))
        
        # Confirm Password
        ttk.Label(form_frame, text="Confirm Password:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.confirm_entry = ttk.Entry(form_frame, show="•", font=("Helvetica", 10), width=35)
        self.confirm_entry.pack(anchor="w", pady=(0, 20))
        
        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(fill="x", pady=10)
        
        ttk.Button(button_frame, text="Sign Up", command=self.signup).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Back to Login", 
                  command=self.back_to_login).pack(side="left", padx=5)
    
    def signup(self):
        """Handle signup logic simulation"""
        fullname = self.fullname_entry.get().strip()
        email = self.email_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        
        # Check if any field is empty
        if not all([fullname, email, username, password, confirm]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Check if passwords match
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        # Simple success simulation
        messagebox.showinfo("Success", f"Account created for {username}!\nYou can now log in.")
        print(f"User Registered: {username} ({email})")

    def back_to_login(self):
        """Simulate navigation back to login"""
        print("Navigation Triggered: Returning to Login Page...")
        messagebox.showinfo("Navigation", "In the full app, this would switch to the Login Page.")

# ================= EXECUTABLE SECTION =================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blog App - Signup Only")
    root.geometry("450x650") # Slightly taller to fit more fields

    # Passing root as parent and controller for standalone run
    signup_page = SignupPage(parent=root, controller=root)
    signup_page.pack(fill="both", expand=True)

    root.mainloop()



    # ('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', '8514oem', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight', '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI', 'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI', 'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'MingLiU_MSCS-ExtB', '@MingLiU_MSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Nirmala Text', 'Nirmala Text Semilight', 'Palatino Linotype', 'Sans Serif Collection', 'Segoe Fluent Icons', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'Segoe UI Variable Small Light', 'Segoe UI Variable Small Semilig', 'Segoe UI Variable Small', 'Segoe UI Variable Small Semibol', 'Segoe UI Variable Text Light', 'Segoe UI Variable Text Semiligh', 'Segoe UI Variable Text', 'Segoe UI Variable Text Semibold', 'Segoe UI Variable Display Light', 'Segoe UI Variable Display Semil', 'Segoe UI Variable Display', 'Segoe UI Variable Display Semib', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small', 'Sitka Small Semibold', 'Sitka Text', 'Sitka Text Semibold', 'Sitka Subheading', 'Sitka Subheading Semibold', 'Sitka Heading', 'Sitka Heading Semibold', 'Sitka Display', 'Sitka Display Semibold', 'Sitka Banner', 'Sitka Banner Semibold', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold', 'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight', '@Yu Gothic UI Semilight', 'SimSun-ExtG', '@SimSun-ExtG', 'Agency FB', 'Algerian', 'Arial Narrow', 'Arial Rounded MT Bold', 'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Berlin Sans FB Demi', 'Bernard MT Condensed', 'Blackadder ITC', 'Bodoni MT', 'Bodoni MT Black', 'Bodoni MT Condensed', 'Bodoni MT Poster Compressed', 'Book Antiqua', 'Bookman Old Style', 'Bookshelf Symbol 7', 'Bradley Hand ITC', 'Britannic Bold', 'Broadway', 'Brush Script MT', 'Californian FB', 'Calisto MT', 'Castellar', 'Centaur', 'Century', 'Century Gothic', 'Century Schoolbook', 'Chiller', 'Colonna MT', 'Cooper Black', 'Copperplate Gothic Bold', 'Copperplate Gothic Light', 'Curlz MT', 'Dubai', 'Dubai Light', 'Dubai Medium', 'Edwardian Script ITC', 'Elephant', 'Engravers MT', 'Eras Bold ITC', 'Eras Demi ITC', 'Eras Light ITC', 'Eras Medium ITC', 'Felix Titling', 'Footlight MT Light', 'Forte', 'Franklin Gothic Book', 'Franklin Gothic Demi', 'Franklin Gothic Demi Cond', 'Franklin Gothic Heavy', 'Franklin Gothic Medium Cond', 'Freestyle Script', 'French Script MT', 'Garamond', 'Gigi', 'Gill Sans MT', 'Gill Sans MT Condensed', 'Gill Sans MT Ext Condensed Bold', 'Gill Sans Ultra Bold', 'Gill Sans Ultra Bold Condensed', 'Gloucester MT Extra Condensed', 'Goudy Old Style', 'Goudy Stout', 'Haettenschweiler', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Imprint MT Shadow', 'Informal Roman', 'Jokerman', 'Juice ITC', 'Kristen ITC', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Typewriter', 'Magneto', 'Maiandra GD', 'Matura MT Script Capitals', 'Mistral', 'Modern No. 20', 'Monotype Corsiva', 'MS Outlook', 'MS Reference Sans Serif', 'MS Reference Specialty', 'MT Extra', 'Niagara Engraved', 'Niagara Solid', 'OCR A Extended', 'Old English Text MT', 'Onyx', 'Palace Script MT', 'Papyrus', 'Parchment', 'Perpetua', 'Perpetua Titling MT', 'Playbill', 'Poor Richard', 'Pristina', 'Rage Italic', 'Ravie', 'Rockwell', 'Rockwell Condensed', 'Rockwell Extra Bold', 'Script MT Bold', 'Showcard Gothic', 'Snap ITC', 'Stencil', 'Tempus Sans ITC', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Tw Cen MT Condensed Extra Bold', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Wingdings 2', 'Wingdings 3', 'HP Simplified', 'HP Simplified Light', 'HP Simplified Jpan Light', '@HP Simplified Jpan Light', 'HP Simplified Jpan', '@HP Simplified Jpan', 'HP Simplified Hans Light', '@HP Simplified Hans Light', 'HP Simplified Hans', '@HP Simplified Hans', 'Montserrat Medium', 'Montserrat', 'Ubuntu Mono', 'Ubuntu Mono Medium', 'Cascadia Code ExtraLight', 'Cascadia Code Light', 'Cascadia Code SemiLight', 'Cascadia Code', 'Cascadia Code SemiBold', 'Cascadia Mono ExtraLight', 'Cascadia Mono Light', 'Cascadia Mono SemiLight', 'Cascadia Mono', 'Cascadia Mono SemiBold')