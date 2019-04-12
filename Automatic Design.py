import datetime
import glob
from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from colour import Color
import openpyxl

title = u'Title of poster'
subtitle = u'Subtitle'
buttonText = u'DOWNLOAD'

buttonHeight = 40
buttonWidth = 280

fillColor = (255,255,255)
outlineColor = (255,255,255)

x0=150
x1=x0+buttonWidth
y0=400
y1=y0+buttonHeight

category = '电子数码'

wb = openpyxl.load_workbook('/Users/moqu/Downloads/素材库1.0/需求/素材需求0410.xlsx')
sheet = wb['Sheet1']

def watermark():
    i=2
    for files in glob.glob('/Users/moqu/Downloads/imglib/*.png'):
        chfont = ImageFont.truetype('/Library/Fonts/Tahoma.ttf',72)
        enfont = ImageFont.truetype('/Library/Fonts/Tahoma.ttf',48)
        buttonfont = ImageFont.truetype('/Library/Fonts/Tahoma.ttf',24)
        img = Image.open(files)

       # target = Image.new('RGBA', img.size, (0, 0, 0, 0))

        result = sheet.cell(row=i, column=6).value
        result_list = result.split("\n")
        title = str(result_list[0])
        subtitle = str(result_list[1])
        buttonText = str(result_list[2])

        draw = ImageDraw.Draw(img)
        draw.text((img.size[0] - 1060, img.size[1] - 416), title, fill=(255, 100, 100), font=chfont)
        draw.text((img.size[0] - 1060, img.size[1] - 420), title, fill=(255, 255, 255), font=chfont)
        draw.text((img.size[0] - 1060, img.size[1] - 320), subtitle, fill=(255, 255, 255), font=enfont)
        draw.rectangle([(x0, y0), (x1, y1)], fillColor,outlineColor)
        draw.text((160, 400), buttonText, fill=(0, 0, 0), font=buttonfont)

        '''
        commodity_box = (img.size/2,img.size/2-150,300,300)
        for commodity_img in glob.glob('/Users/moqu/Downloads/素材库1.0/分类/商品1.1/'+category+'/*.png'):
            commodity_img_
            img.paste(commodity_img,commodity_box,commodity_img)
        '''
        commodity_img = Image.open('/Users/moqu/Downloads/素材库1.0/分类/商品1.1/电子数码/电子数码001.png')
        commodity_region = commodity_img
        commodity_region = commodity_region.convert("RGBA")
        commodity_region.thumbnail((300,200))
        img.paste(commodity_region,(800,200),commodity_region)

        logo_img = Image.open(r'/Users/moqu/Downloads/素材库1.0/Logo/Lazada_Group_Logo.png')
        box = (img.size[0] - 300, img.size[1] - 200,img.size[0], img.size[1])
        region = logo_img
        region = region.convert("RGBA")
        region = region.resize((box[2] - box[0], box[3] - box[1]))

        img.paste(region, box, region)

        dir = "/Users/moqu/Downloads/Outputfolder/"
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      # filename = dir + name + '_result.png'
        filename = dir + sheet.cell(row=i, column=3).value+'.png'
        sleep(1)
        img.save(filename)
        print (filename+" Done!")

        i=i+1

if __name__=='__main__':
    watermark()







