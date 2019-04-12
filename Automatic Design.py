import datetime
import glob
from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from colour import Color

title = u'Title of poster'
subtitle = u'Subtitle'
buttonText = u'DOWNLOAD'

buttonHeight = 40
buttonWidth = 160

fillColor = (255,255,255)
outlineColor = (255,255,255)

x0=150
x1=x0+buttonWidth
y0=400
y1=y0+buttonHeight

def watermark():
    for files in glob.glob('/Users/moqu/Downloads/imglib/*.png'):
        chfont = ImageFont.truetype('/Library/Fonts/_H_HelveticaNeue.ttc',72)
        enfont = ImageFont.truetype('/Library/Fonts/_H_HelveticaNeue.ttc',48)
        buttonfont = ImageFont.truetype('/Library/Fonts/_H_HelveticaNeue.ttc',24)
        img = Image.open(files)

        target = Image.new('RGBA', img.size, (0, 0, 0, 0))

        draw = ImageDraw.Draw(img)
        draw.text((img.size[0] - 1060, img.size[1] - 416), title, fill=(255, 100, 100), font=chfont)
        draw.text((img.size[0] - 1060, img.size[1] - 420), title, fill=(255, 255, 255), font=chfont)
        draw.text((img.size[0] - 1060, img.size[1] - 320), subtitle, fill=(255, 255, 255), font=enfont)
        draw.rectangle([(x0, y0), (x1, y1)], fillColor,outlineColor)
        draw.text((160, 400), buttonText, fill=(0, 0, 0), font=buttonfont)

        logo_img = Image.open(r'/Users/moqu/Downloads/素材库1.0/Logo/Lazada_Group_Logo.png')
        box = (img.size[0] - 200, img.size[1] - 200,img.size[0], img.size[1])


        region = logo_img
        region = region.convert("RGBA")
        region = region.resize((box[2] - box[0], box[3] - box[1]))

        img.paste(region, box, region)

        dir = "/Users/moqu/Downloads/Outputfolder/"
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = dir + name + '_result.png'
        sleep(1)
        img.save(filename)



if __name__=='__main__':
    watermark()

