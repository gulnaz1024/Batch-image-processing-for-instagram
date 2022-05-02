from sys import path_importer_cache
from PIL import Image,ImageDraw, ImageFont
import os
from fileinput import filename

a = b = 0
c = d = 1080



#put pictures to "images" folder that must be at the same folder with python file
for filename in os.listdir('./images'):
    path_to_img = './images/' + str(filename)
    image = Image.open(path_to_img)
    tatras = image.crop((a, b, c, d))
    grayscale = tatras.convert('L')
    # grayscale.show()
    filename = filename.split('.')
    path_to_edited_img = './edited_images/' + filename[0] + '.png'
    print(path_to_edited_img)
