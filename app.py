import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdf
from util import merge_pdf
from logger import get_logging

logging = get_logging()

class App:
    def __init__(self):
        try:
            self.root = Tk()
            self.root.geometry("400x250")
            self.root.title("Py Pdf Finder")
            self.folder_text = StringVar()
            self.files_list_data = StringVar()
        except Exception as e:
            logging.error("Failed to load app. " +str(e))
        

    def run(self):
        self.root.mainloop()

    def get_files(self):
        """
        Get files from given directory
        """
        try:
            folder_path = self.folder_text.get()
            files = os.listdir(folder_path)
            return files
        except Exception as e:
            logging.error("Failed to get files from directory. " +str(e))

    def add_files(self):
        """
        Add files to list element
        """
        try:
            self.files_list_data.set(self.get_files())
            if merge_pdf(folder_path= self.folder_text.get() ,files=self.get_files(), filename="result.pdf"):
                self.load_pdf("result.pdf")
            else:
                messagebox.showinfo(title="Application Error",message="No pdf files found in the directory")
        except Exception as e:
            logging.error("Failed to add files to list element. " +str(e))

    def load_ui_elements(self):
        try:
            # Frame
            frame = Frame(self.root, padx=20, pady=20)
            frame.pack()

            # Label
            folder_label = ttk.Label(frame, text="Choose Folder:")
            folder_label.pack()

            # Entry
            folder_entry = ttk.Entry(frame,textvariable=self.folder_text, width=30)
            folder_entry.pack()

            # Button
            search_button = ttk.Button(frame, text="Get Files", command=lambda : self.add_files())
            search_button.pack()

            # Listbox
            files_list = Listbox(frame, width=50, height=10, border=0, listvariable=self.files_list_data)
            files_list.pack(pady=20, padx=10)

            # Scrollbar
            scroll_bar = Scrollbar(frame)
            scroll_bar.pack()

            # Set Scroll to Listbox
            files_list.configure(yscrollcommand=scroll_bar.set)
            scroll_bar.configure(command=files_list.yview)

            logging.info("All Ui elements are added to main screen")
        except Exception as e:
            logging.error("Failed to load app. " +str(e))


    def load_pdf(self,filename):
        """
        Display Pdf file in Tkinter window
        """
        try:
            pdf_root = Toplevel(self.root)
            pdf_root.geometry("550x750")
            pdf_root.title("Pdf Viewer")
            pdf_root.resizable(width=False, height=False)

            #creating object of ShowPdf from tkpdfWindow   
            v1 = pdf.ShowPdf()

            #Adding pdf location and width and height
            v2 = v1.pdf_view(pdf_root,pdf_location=filename, width=600, height=400)

            v2.pack()
            pdf_root.mainloop()
        except Exception as e:
            logging.error("Failed to load pdf file. " +str(e))

def main():
    app = App()
    app.load_ui_elements()
    app.run()

main()