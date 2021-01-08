from PIL import Image, ImageDraw, ImageColor, ImageFont
from random import randint

def img_square(img_adr: str, sq_size: int, sq_width: int, sq_color):
    try:
    
        im = Image.open(img_adr)
        draw = ImageDraw.Draw(im)

        sz = im.size
    
        # рисуем первую верхнюю линию квадрата
        draw.line([((sz[0]-sq_size)/2,(sz[1]-sq_size)/2),
        ((sz[0]+sq_size)/2,(sz[1]-sq_size)/2)],
        fill=sq_color, width=sq_width)

        # рисуем вторую линию квадрата
        draw.line([(sz[0]/2 + sq_size/2, sz[1]/2 - sq_size/2),
        (sz[0]/2 + sq_size/2, sz[1]/2 + sq_size/2)], 
        fill=sq_color, width=sq_width)

        # рисуем третью линию квадрата
        draw.line([(sz[0]/2 + sq_size/2, sz[1]/2 + sq_size/2),
        (sz[0]/2 - sq_size/2, sz[1]/2 + sq_size/2)], 
        fill=sq_color, width=sq_width)

        # рисуем четвертую линию квадрата
        draw.line([(sz[0]/2 - sq_size/2, sz[1]/2 + sq_size/2),
        (sz[0]/2 - sq_size/2, sz[1]/2 - sq_size/2)], 
        fill=sq_color, width=sq_width)

        im.save(img_adr)
        del draw

        return
    
    except Exception as ex:
        print('Сбой в работе функции img_square() - ' + str(ex))
        return None
    

