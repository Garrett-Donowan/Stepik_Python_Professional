
from zipfile import ZipFile

def extract_this(*args):
    lst = [x for x in args]
    with ZipFile(lst[0]) as zip_file:
        if len(lst) <= 1:
            zip_file.extractall()
        else:
            zip_file.extractall(members = lst[1::])
    return


extract_this('workbook.zip', 'earth.jpg', 'exam.txt')

