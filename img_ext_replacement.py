import os.path
from PIL import Image

ext_1 = '.png'
ext_2 = '.jpg'

Dict = {ext_1:ext_2} # создаем словарь для дальнейшей замены имен

for root, dirs, files in os.walk('.'): # пробегаемся по структуре файлов
    for name in files:
        if ext_1 in name: # ищем файлы исходного расширения
            im = Image.open(name) # открываем изображение
            if im.mode == 'RGBA': # если у нас RGBA профиль, конвертим его в RGB
                im = im.convert('RGB')  # теперь у нас im с нужным профилем
                # сделать замену в имени с одного расширение на другое
                for i in Dict:
                    if name.find(i) >= 0:
                        name = name.replace(i, Dict[i])
                        print(name)
                        im.save(name)
            
            # конвертация без перевода профиля из RGBA в RGB
            else:
                for i in Dict:
                    if name.find(i) >= 0:
                        name = name.replace(i, Dict[i])
                        print(name)
                        im.save(name)


         
