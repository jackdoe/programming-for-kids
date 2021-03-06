import os, math
from PIL import Image
dir = os.listdir('images')
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
def poster(name):
    filtered = []
    for f in dir:
        if f.endswith(".tiff") and (name == 'both' or f.startswith(name)):
            filtered.append(f)
    filtered.sort()

    n = 10
    images = [Image.open(os.path.join('images',x)) for x in filtered]
    widths, heights = zip(*(i.size for i in images))

    total_width = int(14024/2)
    total_height = int(19857/2)

    new_im = Image.new('CMYK', (total_width, total_height), (20,20,20,255))

    base_x =  int((total_width - widths[0] * n)/2)
    x_offset = base_x
    y_offset = int((total_height - (math.ceil(len(images) / n) * heights[0]))/2)
    for row in chunks(images, n):
        for im in row:
            new_im.paste(im, (x_offset,y_offset))
            x_offset += im.size[0]

        y_offset += im.size[1]
        x_offset = base_x

    new_im.save(name + '.tiff',compression = "tiff_lzw")

poster('front')
poster('back')
