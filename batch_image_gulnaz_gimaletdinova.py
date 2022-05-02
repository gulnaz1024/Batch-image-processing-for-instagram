from sys import path_importer_cache
from PIL import Image,ImageDraw, ImageFont
import os
from fileinput import filename

a = b = 0
c = d = 1080

#Creating Text
text = "Ala-Too the BEST"
font = ImageFont.truetype("arial.ttf", 52)

#put pictures to "images" folder that must be at the same folder with python file
for filename in os.listdir('./images'):
    path_to_img = './images/' + str(filename)
    img = Image.open(r'c:/Disk Gulnaz/Learn Coding/projects/images/' + filename).convert("RGBA")
    img = img.crop((0, 0, 1080, 1080))
    txt = Image.new('RGBA', img.size, (255,255,255,0))
    #Creating Draw Object
    d = ImageDraw.Draw(txt)

#Positioning Text
    textwidth, textheight = d.textsize(text, font)
    x=600
    y=950


#Applying Text
    d.text((x,y), text, fill=(255,255,255, 120), font=font)

#Combining Original Image with Text and Saving
    watermarked = Image.alpha_composite(img, txt)
    grayscale = img.convert('L')
    # grayscale.show()
    filename = filename.split('.')
    path_to_edited_img = './edited_images/' + filename[0] + '.png'
    print(path_to_edited_img)
    grayscale.save(path_to_edited_img)
