from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

from pdf import PdfFile, PdfCollection
from utils import OsTools


def pdf_file():
    OsTools.cls()
    print(f"---------- PDF-Datei ----------\n")
    print("Datei auswählen...")

    Tk().withdraw()
    filename = askopenfilename()
    if filename == "":
        return True

    file = PdfFile(filename)

    # print information
    print(f"Datei ausgewählt: '{filename}'\n")

    print("1) Seiten splitten")
    print("2) Seiten rotieren")
    print("3) Abbrechen")

    try:
        # get new week number
        choice = int(input("\nEingabe: "))
        if choice == 1:
            sub_dir_name = input("\nName des Verzeichnis: ")
            file.split_pages(sub_dir_name)
            return True
        elif choice == 2:
            try:
                degree = int(input("\nDrehung in Grad: "))
                file.rotate(degree)
                return True
            except ValueError:
                return False
        elif choice == 3:
            return True
        return False
    except ValueError:
        return False


def pdf_collection():
    OsTools.cls()
    print(f"---------- PDF-Dateien ----------\n")
    print("Ordner auswählen...")

    Tk().withdraw()
    directory = askdirectory()
    if directory == "":
        return True

    collection = PdfCollection(directory)

    # print information
    print(f"Ordner ausgewählt: '{directory}'\n")

    print("1) Seiten mergen")
    print("2) Seiten rotieren")
    print("3) Abbrechen")

    try:
        # get new week number
        choice = int(input("\nEingabe: "))
        if choice == 1:
            pdf_file_name = input("\nName der PDF-Datei: ")
            collection.merge_files(pdf_file_name)
            return True
        elif choice == 2:
            try:
                degree = int(input("\nDrehung in Grad: "))
                collection.rotate(degree)
                return True
            except ValueError:
                return False
        elif choice == 3:
            return True
        return False
    except ValueError:
        return False