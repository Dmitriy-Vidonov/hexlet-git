from PIL import Image, ImageDraw
from random import randint
from center_square import img_square

size = 50
size_step = 10
width = 1
width_step = 1
loop_len = 25

# RGB задал в диапазонах сине-фиолетовых оттенков

Red = randint(1, 10)
Green = randint(120, 150)
Blue = randint(250, 255)

for i in range(loop_len):
    img_square('1_test.png', size, width, (Red, Green, Blue))

    if i % 2 == 0:
        Red = randint(0, 190)
        Green = randint(0, 140)
        Blue = randint(250, 255)

    size += size_step*3
    while width < 10:
        width += width_step
