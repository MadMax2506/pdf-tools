import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from utils import StringUtils, PageNumberNotExists


class PdfFile:
    def __init__(self, path):
        self.__path = path

    def get_page_numbers(self):
        file_input = open(self.__path, 'rb')
        pdf_reader = PdfFileReader(file_input)

        page_numbers = pdf_reader.getNumPages()
        file_input.close()
        return page_numbers

    def rotate(self, degree):
        file_input = open(self.__path, 'rb')
        pdf_reader = PdfFileReader(file_input)
        pdf_writer = PdfFileWriter()

        for page_number in range(0, pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_number)
            page.rotateClockwise(degree)
            pdf_writer.addPage(page)

        file_output_str = StringUtils.rreplace(self.__path, ".", "-rotated.", 1)
        file_output = open(file_output_str, 'wb')
        pdf_writer.write(file_output)

        file_output.close()
        file_input.close()

    def split_pages(self, sub_output_dir=""):
        for page_number in range(0, self.get_page_numbers()):
            self.__split_by_page(page_number, sub_output_dir)

    def get_meta(self):
        file_input = open(self.__path, 'rb')
        pdf_reader = PdfFileReader(file_input)

        meta = pdf_reader.getDocumentInfo()
        file_input.close()
        return meta

    def extract_complete_text(self):
        texts = []
        for i in range(0, self.get_page_numbers()):
            texts.append(self.extract_text_by_page(i))
        return texts

    def extract_text_by_page(self, page_number):
        self.__validate_page_number(page_number)

        file_input = open(self.__path, 'rb')
        pdf_reader = PdfFileReader(file_input)
        try:
            text = pdf_reader.getPage(page_number).extractText()
        except ValueError:
            text = None
        file_input.close()

        return text

    def __split_by_page(self, page_number, sub_output_dir):
        self.__validate_page_number(page_number)

        file_input = open(self.__path, 'rb')
        pdf_reader = PdfFileReader(file_input)
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_number))

        if sub_output_dir:
            dir = StringUtils.rremove(self.__path, "\\", 1) + "\\" + sub_output_dir
            if not os.path.exists(dir):
                os.makedirs(dir)

            modified_path = StringUtils.rreplace(self.__path, "\\", f"\\{sub_output_dir}\\", 1)
        else:
            modified_path = self.__path
        file_output_str = StringUtils.rreplace(modified_path, ".", f"-page-{page_number + 1}.", 1)
        file_output = open(file_output_str, 'wb')
        pdf_writer.write(file_output)

        file_output.close()
        file_input.close()

    def __validate_page_number(self, page_number):
        if page_number < 0 or self.get_page_numbers() <= page_number:
            raise PageNumberNotExists("Seite existiert nicht in der PDF.")
