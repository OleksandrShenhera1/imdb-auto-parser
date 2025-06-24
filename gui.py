import sys
import customtkinter as ctk
from logic import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class PrintLogger:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert("end", text)
        self.textbox.see("end")

    def flush(self):
        pass

class TopLvlWindow(ctk.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # Settings
        self.title("Settings")
        self.resizable(width=False, height=False)

        # Main frame
        self.fullFrame = ctk.CTkFrame(master=self, fg_color="#292F33")
        self.fullFrame.pack(fill="both", expand=True)

        btnPossX, btnPossY = parent.settingsButton.winfo_rootx(), parent.settingsButton.winfo_rooty()
        self.geometry(f"600x360+{btnPossX + 200}+{btnPossY}")

class MainGui(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        self.leftTopFrame = ctk.CTkFrame(master=self.topFrame, fg_color="#292F33", border_width=1, border_color="#E1E8ED", width=360)
        self.leftTopFrame.pack(side="left", fill="both", expand=True)
        self.leftTopFrame.pack_propagate(False) # cant be resized
        # Right frame in top
        self.rightTopFrame = ctk.CTkFrame(master=self.topFrame, fg_color="#292F33")
        self.rightTopFrame.pack(side="right", fill="both", expand=True)
        # Bottom frame
        self.bottomFrame = ctk.CTkFrame(master=self.fullFrame, fg_color="#292F33", border_width=1, border_color="#E1E8ED")
        self.bottomFrame.pack(side="bottom", fill="both", expand=True, padx=4, pady=2)

        # Left frame in top Btn
        self.parseButton = ctk.CTkButton(master=self.leftTopFrame, text="Parse", font=("", 18), bg_color="#292F33", corner_radius=7, command=parseCheck)
        self.parseButton.pack(side="top", fill="x", padx=10, pady=8)

        self.saveCSVButton = ctk.CTkButton(master=self.leftTopFrame, text="Save to CSV", font=("", 18), bg_color="#292F33", corner_radius=7, command=saveFile)
        self.saveCSVButton.pack(side="top", fill="x", padx=10, pady=8)

        self.folderButton = ctk.CTkButton(master=self.leftTopFrame, text="View file folder", font=("", 18), bg_color="#292F33", corner_radius=7, command=openFolderBtn)
        self.folderButton.pack(side="top", fill="x", padx=10, pady=8)

        self.settingsButton = ctk.CTkButton(master=self.leftTopFrame, text="Settings", font=("", 18), bg_color="#292F33", corner_radius=7, command=self.openSettings)
        self.settingsButton.pack(side="top", fill="x", padx=10, pady=8)

        self.githubButton = ctk.CTkButton(master=self.leftTopFrame, text="GitHub Profile", font=("", 18), bg_color="#292F33", corner_radius=7, command=githubProfileBtn)
        self.githubButton.pack(side="top", fill="x", padx=10, pady=8)

        self.parseButton = ctk.CTkButton(master=self.leftTopFrame, text="Check ip", font=("", 18), bg_color="#292F33", corner_radius=7, command=currentIp)
        self.parseButton.pack(side="top", fill="x", padx=10, pady=8)

        # Right frame in top Lbl
        self.info1Label = ctk.CTkButton(master=self.rightTopFrame, text="How to use? (link)", text_color="#E1E8ED", fg_color="#292F33", cursor="hand2", command=openManual)
        self.info1Label.pack(pady=10)


        self.info2Label = ctk.CTkLabel(master=self.rightTopFrame, text=instruction, anchor="center", justify="left", font=("", 14))
        self.info2Label.pack(fill="x", padx=4, pady=20)

        # Console Logger
        self.textbook = ctk.CTkTextbox(self.bottomFrame)
        self.textbook.pack(fill="both", expand=True, padx=5, pady=5)

        sys.stdout = PrintLogger(self.textbook)

        self.topLvlSettings = None

    def openSettings(self):
        if self.topLvlSettings is None or not self.topLvlSettings.winfo_exists():
            self.topLvlSettings = TopLvlWindow(self) # Create window if None
            self.topLvlSettings.grab_set()
        else:
            self.topLvlSettings.focus() # If exists display it
