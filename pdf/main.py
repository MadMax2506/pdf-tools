from PdfFile import PdfFile
from PdfCollection import PdfCollection

if __name__ == '__main__':
    collection = PdfCollection("E:\\downloads\\mg-cheat-sheet")
    #collection.rotate(180)
    collection.merge_files("mg_zusammenfassung")
