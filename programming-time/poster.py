import os
from PIL import Image
dir = os.listdir('images')

def poster(name):
    filtered = []
    for f in dir:
        if f.endswith(".png"):
            filtered.append(f)
    filtered.sort()
    n = 12
    images = [Image.open(os.path.join('images',x)) for x in filtered]
    widths, heights = zip(*(i.size for i in images))

    total_width = widths[0] * n
    total_height = int(len(images) / n) * heights[0]
     

    new_im = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0
    for (i,im) in enumerate(images):
        new_im.paste(im, (x_offset,y_offset))
        x_offset += im.size[0]
        if i != 0 and i % n == 0:
            y_offset += im.size[1]
            x_offset = 0

    new_im.save(name + '.jpg')

poster('front')