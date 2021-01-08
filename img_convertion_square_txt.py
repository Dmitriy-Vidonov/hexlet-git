from PIL import Image
from files_search import file_search
from RGBA_to_RGB import rgba_to_rgb
from sq_with_txt import img_square_with_txt

def img_convertion_square_txt(ext_1: str, ext_2: str, sq_size: int, sq_width: int, sq_color, 
               sq_text: str, txt_fnt_size: int, txt_align: str, txt_str_width: int):
    try:
        file_search(ext_1) # нашли файлы нужного расширения и записали их в массив
        rgba_to_rgb(ext_1) # проверили, нет ли в файлах профиля RGBA и его переделали в RGB где был

        for i in range(len(file_search(ext_1))):
            im = Image.open(file_search(ext_1)[i])  # открыли файлы с уже корректным профилем
            im.save(file_search(ext_1)[i].replace(ext_1, ext_2))  # меняем расширение и сохраняем
            img_square_with_txt(file_search(ext_1)[i].replace(ext_1, ext_2), sq_size, sq_width, sq_color,
            sq_text, txt_fnt_size, txt_align, txt_str_width)

        return
    except Exception as ex:
        print('Сбой в работе функции img_convertion_square_txt() - ' + str(ex))
        return None

# example
# img_convertion_square_txt('.png', '.jpg', 300, 10, (132, 0, 0),
# 'Hello,\nWorld!', 40, 'left', 1)        