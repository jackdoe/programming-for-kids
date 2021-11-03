import os, math
from PIL import Image
dir = os.listdir('images')
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
def poster(name):
    filtered = []
    for f in dir:
        if f.endswith(".png") and f.startswith(name):
            filtered.append(f)
    filtered.sort()

    n = 12
    images = [Image.open(os.path.join('images',x)) for x in filtered]
    widths, heights = zip(*(i.size for i in images))

    total_width = widths[0] * n
    total_height = math.ceil(len(images) / n) * heights[0]

    new_im = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0
    for row in chunks(images, n):
        for im in row:
            new_im.paste(im, (x_offset,y_offset))
            x_offset += im.size[0]

        y_offset += im.size[1]
        x_offset = 0

    new_im.save(name + '.jpg')

poster('front')
poster('back')