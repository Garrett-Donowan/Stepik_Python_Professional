
from zipfile import ZipFile

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

def structure_zip():
    
    with ZipFile('desktop.zip') as zip_file:
        for el in zip_file.infolist():
            struct = list(filter(lambda x: x != "", el.filename.split("/")))
            if el.is_dir():
                print("  " * (len(struct) -1) + struct[-1])
            else:
                print("  " * (len(struct) -1) + struct[-1] + " " + convert_bytes(el.file_size))
    return

structure_zip()

