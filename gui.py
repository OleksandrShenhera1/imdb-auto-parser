import sys
import customtkinter as ctk
from logic import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class printLogger:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert("end", text)
        self.textbox.see("end")

    def flush(self):
        pass


class mainGui(ctk.CTk):
    def __init__(self):
        super().__init__()

    #self = ctk.CTk()
    # Settings
        self.title("Imdb-parser")
        self.geometry("1080x720")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)

        # Main frame
        self.fullFrame = ctk.CTkFrame(master=self, fg_color="#292F33")
        self.fullFrame.pack(fill="both", expand=True)
        # Top frame
        self.topFrame = ctk.CTkFrame(master=self.fullFrame, fg_color="#292F33", border_width=2, border_color="#E1E8ED")
        self.topFrame.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        # Left frame in top
        self.leftTopFrame = ctk.CTkFrame(master=self.topFrame, fg_color="#292F33", border_width=1, border_color="#E1E8ED")
        self.leftTopFrame.pack(side="left", fill="both", expand=True)
        # Right frame in top
        self.rightTopFrame = ctk.CTkFrame(master=self.topFrame, fg_color="#292F33")
        self.rightTopFrame.pack(side="right", fill="both", expand=True)
        # Bottom frame
        self.bottomFrame = ctk.CTkFrame(master=self.fullFrame, fg_color="#292F33", border_width=1, border_color="#E1E8ED")
        self.bottomFrame.pack(side="bottom", fill="both", expand=True, padx=4, pady=2)

        # Buttons
        self.parseButton = ctk.CTkButton(master=self.leftTopFrame, text="Parse", font=("", 18), bg_color="#292F33", corner_radius=7, command=parseCheck)
        self.parseButton.pack(side="top", fill="x", padx=10, pady=8)

        self.saveCSVButton = ctk.CTkButton(master=self.leftTopFrame, text="Save to CSV", font=("", 18), bg_color="#292F33", corner_radius=7, command=saveFile)
        self.saveCSVButton.pack(side="top", fill="x", padx=10, pady=8)

        self.folderButton = ctk.CTkButton(master=self.leftTopFrame, text="View file folder", font=("", 18), bg_color="#292F33", corner_radius=7, command=openFolderBtn)
        self.folderButton.pack(side="top", fill="x", padx=10, pady=8)

        self.settingsButton = ctk.CTkButton(master=self.leftTopFrame, text="Settings", font=("", 18), bg_color="#292F33", corner_radius=7)
        self.settingsButton.pack(side="top", fill="x", padx=10, pady=8)

        self.githubButton = ctk.CTkButton(master=self.leftTopFrame, text="GitHub Profile", font=("", 18), bg_color="#292F33", corner_radius=7, command=githubProfileBtn)
        self.githubButton.pack(side="top", fill="x", padx=10, pady=8)

        self.parseButton = ctk.CTkButton(master=self.leftTopFrame, text="Check ip", font=("", 18), bg_color="#292F33", corner_radius=7, command=currentIp)
        self.parseButton.pack(side="top", fill="x", padx=10, pady=8)
        
        # Console Logger
        self.textbook = ctk.CTkTextbox(self.bottomFrame)
        self.textbook.pack(fill="both", expand=True, padx=5, pady=5)

        sys.stdout = printLogger(self.textbook)


app = mainGui()
app.mainloop()