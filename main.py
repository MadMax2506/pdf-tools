import sys

from utils import OsTools
from pdfManagement import pdf_file, pdf_collection


def print_general_message(first_opening=False, valid_input=True):
    OsTools.cls()
    print("---------- PDF Tools ----------\n")

    if not valid_input:
        print("Fehler bei der Eingabe! Versuchen Sie es erneut.\n")
    elif not first_opening:
        print("Die Eingabe wurde erfolgreich verarbeitet!\n")

    print("1) einzelne PDF-Datei")
    print("2) Ordner mit PDF-Dateien")
    print("3) Programm beenden")


def validate_and_handle_start_menu_input():
    try:
        choice = int(input("\nEingabe: "))
    except ValueError:
        return False

    if choice == 1:
        return pdf_file()
    elif choice == 2:
        return pdf_collection()
    elif choice == 3:
        sys.exit()
    else:
        return False


if __name__ == '__main__':
    print_general_message(first_opening=True)
    valid_input = validate_and_handle_start_menu_input()

    while True:
        print_general_message(valid_input=valid_input)
        valid_input = validate_and_handle_start_menu_input()