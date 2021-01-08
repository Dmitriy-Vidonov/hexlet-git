from PIL import Image
from files_search import file_search

def rgba_to_rgb(ext_for_check: str) -> str:
    try:
        for i in range (len(file_search(ext_for_check))):
            im = Image.open((file_search(ext_for_check)[i]))
            if im.mode == 'RGBA':
                im = im.convert('RGB')
                im.save((file_search(ext_for_check)[i]))
        return
    except Exception as ex:
        print('Сбой в работе функции rgba_to_rgb() - ' + str(ex))
        return None

# обычный тестовый вызов работы функции
#rgba_to_rgb('png')

# выводим список всех файлов построчно + смотрим профиль изображений
#for i in range(len(file_search('png'))):
 #   im = Image.open(file_search('png')[i])
  #  print(file_search('png')[i], im.mode)