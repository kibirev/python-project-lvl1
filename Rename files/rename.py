from PyPDF2 import PdfReader
import os


def getting_list_files():
    content = os.listdir('C:\\DSSL\\temp')
    return content


def replacing_name_file(new_name, old_name):
    os.rename(f"C:\\DSSL\\temp\\{old_name}", f"C:\\DSSL\\temp\\{new_name}")


def reading_pdf_file(file):
    chars = ['"']
    path = 'C:\\DSSL\\temp\\' + file
    reader = PdfReader(path)
    page = reader.pages[0]
    text = page.extract_text()
    name_company = text.split('\n')[11].split(',')[0].split(':')[1]
    name_company = name_company.translate(str.maketrans('', '', ''.join(chars)))
    return  name_company

def main():
    list_files = getting_list_files()
    for filename in list_files:
        new_name_file = reading_pdf_file(filename) + ' ' + filename
        replacing_name_file(new_name_file, filename)


if __name__ == '__main__':
    main()