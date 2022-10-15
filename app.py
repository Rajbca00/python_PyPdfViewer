from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import os
from PyPDF2 import PdfMerger
from tkPDFViewer import tkPDFViewer as pdf
import logging

#Config Logging
logging.basicConfig(level=logging.DEBUG, filename=r"log.log",format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", datefmt='%H:%M:%S', filemode='a+', force=True)

root = Tk()
folder_text = StringVar()
files_list_data = StringVar()

def main():
    load_app()
    load_view()


def load_app():
    """
        Setup and load main screen
    """

    try:
        root.title("Pdf Picker")
        root.geometry("400x250")
        root.resizable(width=False, height=False)

        logging.info("load_app completed")
    except Exception as e:
        logging.error("Failed to load app. " +str(e))

def load_view():
    """
        Add all GUI elements to main screen
    """
    try:
        # Frame
        frame = Frame(root, padx=20, pady=20)
        frame.pack()

        # Label
        folder_label = ttk.Label(frame, text="Choose Folder:")
        folder_label.pack()

        # Entry
        folder_entry = ttk.Entry(frame,textvariable=folder_text, width=30)
        folder_entry.pack()

        # Button
        search_button = ttk.Button(frame, text="Get Files", command=add_files)
        search_button.pack()

        # Listbox
        files_list = Listbox(frame, width=50, height=10, border=0, listvariable=files_list_data)
        files_list.pack(pady=20, padx=10)

        # Scrollbar
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack()

        # Set Scroll to Listbox
        files_list.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=files_list.yview)

        logging.info("All Ui elements are added to main screen")

        root.mainloop()

    except Exception as e:
        logging.error("Failed to load elements. " +str(e))
    

def add_files():
    """
        Add files to list element
    """
    try:
        files_list_data.set(get_files())
        check_pdf_files()
    except Exception as e:
        logging.error("Failed to add files to list element. " +str(e))

def get_files():
    """
        Get files from given directory
    """
    try:
        folder_path = folder_text.get()
        files = os.listdir(folder_path)
        return files
    except Exception as e:
        logging.error("Failed to get files from directory. " +str(e))

def check_pdf_files():
    """
    Check for pdf files
    """
    try:

        pdf_files = [file for file in get_files() if ".pdf" in file]
        if len(pdf_files) == 0:
            messagebox.showinfo(title="Application Error",message="No pdf files found in the directory")
            return
        merge_pdf(pdf_files)
        show_pdf()
    
    except Exception as e:
        logging.error("Failed to check for pdf files. " +str(e))


def merge_pdf(pdf_files):
    """
        Merge Pdf Files
    """

    try:
        merger = PdfMerger()
        folder_path = folder_text.get()

        for pdf in pdf_files:
            merger.append(folder_path+"/"+pdf)

        merger.write("result.pdf")
        merger.close()
        print("File merged")
    except Exception as e:
        logging.error("Failed to merge pdf files. " +str(e))


def show_pdf():
    """
    Display Pdf file in Tkinter window
    """

    try:
        pdf_root = Toplevel(root)
        pdf_root.geometry("550x750")
        pdf_root.title("Pdf Viewer")
        root.resizable(width=False, height=False)

        #creating object of ShowPdf from tkpdfWindow   
        v1 = pdf.ShowPdf()

        

        #Adding pdf location and width and height
        v2 = v1.pdf_view(pdf_root,pdf_location=r"result.pdf", width=600, height=400)

        v2.pack()
        pdf_root.mainloop()
    except Exception as e:
        logging.error("Failed to load pdf file. " +str(e))

main()