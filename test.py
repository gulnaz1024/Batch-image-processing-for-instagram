from fileinput import filename
from PIL import Image, ImageDraw, ImageFont

#Opening Image & Creating New Text Layer
img = Image.open(r'c:/Disk Gulnaz/Learn Coding/projects/images/1.jpg').convert("RGBA")
img = img.crop((0, 0, 1080, 1080))
txt = Image.new('RGBA', img.size, (255,255,255,0))


#Creating Text
text = "Ala-Too the BEST"
font = ImageFont.truetype("arial.ttf", 52)


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


grayscale = watermarked.convert('L')
grayscale.save(r'./edited_images/cake_watermarked50.png')

grayscale.show()