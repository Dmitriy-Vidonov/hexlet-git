from PIL import Image, ImageDraw, ImageColor
im = Image.open('test2.png') # открываем существующее изображение

# ***** Изображение Image *****

# вывести инфу об изображении
print(im.format, im.size, im.mode)

# вывести содержимое картинки на экран
# im.show()

# делаем перевод избражения в другой формат
rgb_im = im.convert('RGB')
rgb_im.save('test2.jpg')

print(rgb_im.format, rgb_im.size, rgb_im.mode)

# вырежем прямоугольник. координаты в порядке - левый верхний, правый нижний
# начало координат стартует в левом верхнем углу экрана
box = (120, 120, 340, 340)
region = im.crop(box)

# вывод прямоугольника на экран
# region.show()

# ресайз изображения
rsz = im.resize((256, 256))
rsz.save('test2_resized.png')

# вращение изображения
rsz = im.rotate(70)
rsz.save('test2_rotated.png')

# ***** Рисование на холсте ImageDraw *****

# получаем холст изображения
draw = ImageDraw.Draw(im)

# рисуем линию, разделяющую изображение пополам
# (первый параметр -- список начальной и конечной пар x,y, 
# второй параметр -- цвет заполнения линии, набор трёх RGB-значений):
sz = im.size
print('размер изображения -', sz)
draw.line([sz[0]/2,0, sz[0]/2, sz[1]], fill=(255,128,255))
im.save('test2_with_line.png') # сохраняем изображение для применения изменений
del draw # удаляем холст
im.show() # выводим итоговое изображение на экран

# выводим заполненный белым прямоугольник
kartinka = Image.open('test2.png') # открыли картинку
draw = ImageDraw.Draw(kartinka)    # создали холст
draw.rectangle([100,100, 300,300], fill=(255,255,255)) # рисуем прямоугольник

# пишем текст
draw.multiline_text((500,500), '11111\n55555')

kartinka.save('test_with_rectangle_und_text.png') # сохраняем картинку
del draw # удаляем холст
kartinka.show() # выводим картинку на просмотр



