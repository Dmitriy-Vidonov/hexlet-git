from PIL import Image, ImageDraw, ImageFont

def img_square_with_txt(img_adr: str, sq_size: int, sq_width: int, sq_color, 
               sq_text: str, txt_fnt_size: int, txt_align: str, txt_str_width: int):
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

        fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', txt_fnt_size)
        draw.multiline_text((sz[0]/2 - sq_size/2 + sq_width*2,
        sz[1]/2 - sq_size/2 + sq_width*2),
        sq_text, font = fnt, fill=None,
        align=txt_align, stroke_width=txt_str_width)

        im.save(img_adr)
        del draw

        return
    
    except Exception as ex:
        print('Сбой в работе функции img_square_with_txt() - ' + str(ex))
        return None

# example
# img_square_with_txt('for_test.jpg', 300, 10, (132, 0, 0),
# 'Hello,\nWorld!', 40, 'left', 1)
