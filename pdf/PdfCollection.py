from os import listdir
from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import isfile, join

from pdf import PdfFile
from utils import EmptyFolder, StringUtils, OsTools


class PdfCollection:
    def __init__(self, folder_path):
        self.__folder_path = folder_path
        self.__separator = OsTools.separator(folder_path)

    def get_all_files(self):
        all_files = [f for f in listdir(self.__folder_path) if isfile(join(self.__folder_path, f))]
        return [f for f in all_files if f.lower().endswith('.pdf')]

    def rotate(self, degree):
        for file_path in self.get_all_files():
            pdf_file = PdfFile(f"{self.__folder_path}{self.__separator}{file_path}")
            pdf_file.rotate(degree)

    def merge_files(self, name):
        self.__validate_folder()

        writer = PdfFileWriter()
        for file_path in self.get_all_files():
            file_input = open(f"{self.__folder_path}{self.__separator}{file_path}", 'rb')
            pdf_file = PdfFileReader(file_input)
            for page in range(0, pdf_file.getNumPages()):
                writer.addPage(pdf_file.getPage(page))

        parent_folder = StringUtils.rremove(self.__folder_path, self.__separator, 1)
        with open(f"{parent_folder}{self.__separator}{name}.pdf", 'wb') as file_out:
            writer.write(file_out)

    def __validate_folder(self):
        if self.get_all_files() == 0:
            raise EmptyFolder("Es sind keine Pdfs in dem Ordner vorhanden.")
