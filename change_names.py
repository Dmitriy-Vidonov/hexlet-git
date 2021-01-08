from files_search import file_search
from PIL import Image

def change_name(ext_1: str, ext_2: str) -> str:
    try:
        massiv_change_names = []
        for i in range(len(file_search(ext_1))):
            massiv_change_names.append(file_search(ext_1)[i].replace(ext_1, ext_2))
        
        return massiv_change_names

    except Exception as ex:
        print('Сбой в работе функции change_names() - ' + str(ex))
        return None

# из тестов запускать за раз какой-то один, иначе не сработает
# print(change_name('.png', '.jpg'))

# выводим список всех файлов построчно + смотрим профиль изображений
#for i in range(len(change_name('.png', '.jpg'))):
 #   print(change_name('.png', '.jpg')[i])