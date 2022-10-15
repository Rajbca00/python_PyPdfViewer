from logger import get_logging
from PyPDF2 import PdfMerger

logging = get_logging()

def merge_pdf(*,folder_path,files, filename):
    """
        Check and merge pdf files.

        if files not present 
            returns False
        else
            returns True
    """
    pdf_files = [file for file in files if ".pdf" in file]

    if len(pdf_files) == 0:
        return False
    else:
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(folder_path+"/"+pdf)

        merger.write(filename)
        merger.close()
        logging.info("File merged")

        return True