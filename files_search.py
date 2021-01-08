import os.path
from PIL import Image

def file_search(file_ext: str) -> str:
    try:
        massiv_files_search = []
        for root, dirs, files in os.walk('.'):
            for name in files:
                if file_ext in name:
                    massiv_files_search.append(name) 
    
        return massiv_files_search
    except Exception as ex:
        print('Сбой в работе функции file_search() - ' + str(ex))
        return None

# обычный тестовый вызов работы функции
#print(file_search('png'))

# выводим список всех файлов построчно + смотрим профиль изображений
#for i in range(len(file_search('png'))):
   # im = Image.open(file_search('png')[i])
   # print(file_search('png')[i], im.mode)