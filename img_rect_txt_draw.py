from PIL import Image, ImageDraw, ImageFile, ImageColor, ImageFont
ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open('for_draw_exps.png')
draw = ImageDraw.Draw(im) # получили холст изображения

sz = im.size
square_side = 300
square_width = 10

# рисуем первую верхнюю линию квадрата
#draw.line([(sz[0]/2 - square_side/2, sz[1]/2 - square_side/2), 
#(sz[0]/2 + square_side/2, sz[1]/2 - square_side/2)], 
#fill=(227, 187, 11), width=square_width)

draw.line([((sz[0]-square_side)/2,(sz[1]-square_side)/2),
((sz[0]+square_side)/2,(sz[1]-square_side)/2)],
fill=(227, 187, 11), width=square_width)

# рисуем вторую линию квадрата
draw.line([(sz[0]/2 + square_side/2, sz[1]/2 - square_side/2),
(sz[0]/2 + square_side/2, sz[1]/2 + square_side/2)], 
fill=(227, 187, 11), width=square_width)

# рисуем третью линию квадрата
draw.line([(sz[0]/2 + square_side/2, sz[1]/2 + square_side/2),
(sz[0]/2 - square_side/2, sz[1]/2 + square_side/2)], 
fill=(227, 187, 11), width=square_width)

# рисуем четвертую линию квадрата
draw.line([(sz[0]/2 - square_side/2, sz[1]/2 + square_side/2),
(sz[0]/2 - square_side/2, sz[1]/2 - square_side/2)], 
fill=(227, 187, 11), width=square_width)

# задаем шрифт для текста и пишем текст
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
draw.multiline_text((sz[0]/2 - square_side/2 + square_width*2,
sz[1]/2 - square_side/2 + square_width*2),
'Hello,\nWorld!', font = fnt, fill=None,
align='left', stroke_width=1)

size = draw.multiline_textsize('Hello,\nWorld!', font = fnt, stroke_width=1)
print(size)

im.save('TEST_for_draw_exps.png')
del draw
im.show()



