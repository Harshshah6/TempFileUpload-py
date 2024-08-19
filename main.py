from customtkinter import *
from PIL import Image
import requests
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App(CTk):
    URL = "https://tmpfiles.org/api/v1/upload"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filepath:StringVar = StringVar(self,"File Path")
        self.responseVAR = StringVar(self,"")


        self.FRAME2 = CTkFrame(master=self, height=100, corner_radius=0)
        self.FRAME2.pack(fill="both")

        self.browseFileIcon = CTkLabel(master=self.FRAME2, cursor="hand2",text="", compound="left", anchor="center", justify="left", fg_color="transparent", image=CTkImage(Image.open(resource_path(r"12075830.png")), size=(25, 25)), height=25)
        self.browseFileIcon.pack(padx=(10, 0), side="left")
        self.browseFileIcon.bind("<Button-1>",lambda e:self.onBrowseClick())

        self.filePath = CTkEntry(master=self.FRAME2, placeholder_text="File Path", textvariable=self.filepath)
        self.filePath.pack(padx=(8, 20), expand=1, fill="both", pady=21, side="left")

        self.buttonUpload = CTkButton(master=self.FRAME2, width=140, height=38, compound="right", text="Upload", corner_radius=30, fg_color=("#2CC985", "#2FA572"), text_color=("gray98", "#DCE4EE"), hover_color=("#0C955A", "#106A43"), border_color=("#3E454A", "#949A9F"), border_width=0, text_color_disabled=("gray78", "gray68"), image=CTkImage(Image.open(resource_path(r"baseline_arrow_forward_white_18dp_1x.png")), size=(18, 18)), font=CTkFont(size=15, weight="normal"), command=self.onUploadClick)
        self.buttonUpload.pack(padx=(0, 10), pady=21)

        self.FRAME8 = CTkFrame(master=self, fg_color="transparent", bg_color="transparent", height=0)
        self.FRAME8.pack_propagate(False)
        self.FRAME8.pack(expand=True, fill="both", pady=12)

        # self.response = CTkEntry(master=self.FRAME8, justify="left",  state="readonly", textvariable=self.responseVAR, fg_color="transparent", border_width=0, bg_color="transparent")
        # self.response.pack(padx=(21, 0), side="left", expand=1, fill="both",)

        self.response = CTkTextbox(master=self.FRAME8, fg_color="transparent", state="disabled",border_width=0, bg_color="transparent")
        self.response.pack(padx=(21, 0), side="left", expand=1, fill="both",)

        self.FRAME10 = CTkFrame(master=self)
        self.FRAME10.pack(fill="both")

        self.LABEL11 = CTkLabel(master=self.FRAME10, text="Made with love @LEGENDARY STREAMER", padx=0, pady=10, font=CTkFont(size=12))
        self.LABEL11.pack()

    def onBrowseClick(self):
        self.filepath.set(filedialog.askopenfilename())

    def onUploadClick(self):
        FILE_PATH:str = self.filepath.get().strip()
        if FILE_PATH == "File Path" or FILE_PATH == "":
            self.updateResponse("Please select a file to upload.")
            return
        
        try:
            params = {"file" : open(FILE_PATH, "rb")}  
            response = requests.post(self.URL, files=params)
            JSON = response.json()
            if JSON.get("status") == "success":
                self.updateResponse("\n")
                self.updateResponse(f"File {FILE_PATH} uploaded successfully.\nLINK:- {JSON.get("data").get("url")}")
                self.updateResponse("\n")
            else:
                self.updateResponse(f"Failed to upload file {FILE_PATH}.\nError: {JSON.get('message')}")

        except Exception as e:
                self.updateResponse(f"Error: {e}")

    def updateResponse(self,text:str):
        # ftext = self.response.cget("text") + text + "\n" 
        # self.response.configure(text=ftext)
        ftext = text + "\n"
        self.responseVAR.set(ftext)
        self.response.configure(state="normal")
        self.response.insert(END,ftext)
        self.response.configure(state="disabled")
        
set_default_color_theme("blue")
root = App()
root.geometry("700x500")
root.title("TempFileUpload")
root.configure(fg_color=['gray92', 'gray14'])
root.mainloop()
            
