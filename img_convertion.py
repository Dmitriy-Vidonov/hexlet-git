from PIL import Image
from files_search import file_search
from RGBA_to_RGB import rgba_to_rgb

def img_convertion(ext_1: str, ext_2: str) -> str:
    try:
        file_search(ext_1) # нашли файлы нужного расширения и записали их в массив
        rgba_to_rgb(ext_1) # проверили, нет ли в файлах профиля RGBA и его переделали в RGB где был

        for i in range(len(file_search(ext_1))):
            im = Image.open(file_search(ext_1)[i])  # открыли файлы с уже корректным профилем
            im.save(file_search(ext_1)[i].replace(ext_1, ext_2))  # меняем расширение и сохраняем

        return
    except Exception as ex:
        print('Сбой в работе функции img_convertion() - ' + str(ex))
        return None