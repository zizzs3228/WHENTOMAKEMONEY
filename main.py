from operator import length_hint
from turtle import color
from PIL import Image, ImageDraw, ImageOps, ImageFont 
import webbrowser
yearA = 1965
yearB = 1962
yearC = 1958
yearsA = []
yearsB = []
yearsC = []
yearsA.append(yearA)
yearsB.append(yearB)
yearsC.append(yearC)
for i in range(1,6):
    yearA = yearA + 16
    yearsA.append(yearA)
    yearA = yearA + 18
    yearsA.append(yearA)
    yearA = yearA + 20
    yearsA.append(yearA)
# print('Года паники',end=' ')
# print(yearsA)
# print(len(yearsA))

for i in range(1,6):
    yearB = yearB + 10
    yearsB.append(yearB)
    yearB = yearB + 8
    yearsB.append(yearB)
    yearB = yearB + 9
    yearsB.append(yearB)
    yearB = yearB + 10
    yearsB.append(yearB)
    yearB = yearB + 8
    yearsB.append(yearB)
    yearB = yearB + 9
    yearsB.append(yearB)
# print('Лучшие года для продажи',end=' ')
# print(yearsB)
# print(len(yearsB))

for i in range(1,11):
    yearC = yearC + 11
    yearsC.append(yearC)
    yearC = yearC + 9
    yearsC.append(yearC)
    yearC = yearC + 7
    yearsC.append(yearC)

# print('Лучшие года для покупки',end=' ')
# print(yearsC)
# print(len(yearsC))

pc = Image.open('pc.png')
draw = ImageDraw.Draw(pc)
font = ImageFont.truetype('ARIAL.TTF', 20) 
draw.line([(0,300),(1920,300)],fill='white' ,width=2)
draw.line([(0,900),(1920,900)],fill='white' ,width=2)
draw.line([(0,600),(1920,600)],fill='white' ,width=2)
yearsA.reverse()
yearsB.reverse()
yearsC.reverse()
length = len(yearsA)
for i in range(1, len(yearsA)+1):
    draw.ellipse((i*124-4-62, 300-4, i*124+4-62, 300+4), fill=(255,0,0,0))
    draw.text((i*124-23-62, 250), text=f"{yearsA.pop()}", font = font, align ="centre")

for i in range(1, len(yearsB)+1):
    draw.ellipse((i*62+-4, 600-4, i*62+4, 600+4), fill=(255,0,0,0))
    draw.text((i*62+-23, 550), text=f"{yearsB.pop()}", font = font, align ="centre")

for i in range(1, len(yearsC)+1):
    draw.ellipse((i*62-31-4, 900-4, i*62-31+4, 900+4), fill=(255,0,0,0))
    draw.text((i*62-23-31, 930), text=f"{yearsC.pop()}", font = font, align ="centre")

for i in range(1, length+1):
    draw.line([(2*i*62-93,900),(2*i*62-62,300)],fill='white' ,width=1)
    draw.line([(2*i*62-31,900),(2*i*62-62,300)],fill='white' ,width=1)
    draw.line([(2*i*62-93,900),(2*i*62-62,600)],fill='white' ,width=1)
    draw.line([(2*i*62-31,900),(2*i*62-62,600)],fill='white' ,width=1)
    draw.line([(2*i*62-31,900),(2*i*62,600)],fill='white' ,width=1)
    draw.line([(2*i*62+31,900),(2*i*62,600)],fill='white' ,width=1)

font = ImageFont.truetype('ARIAL.TTF', 17)

for i in range(1,11):
    draw.text((3*i*62-134, 870), text="11", font = font, align ="centre")
    draw.text((3*i*62-68, 870), text="9", font = font, align ="centre")
    draw.text((3*i*62-5, 870), text="7", font = font, align ="centre")
    draw.text((3*i*62-100, 615), text="10", font = font, align ="centre")
    draw.text((3*i*62-35, 615), text="8", font = font, align ="centre")
    draw.text((3*i*62+30, 615), text="9", font = font, align ="centre")
    draw.text((3*i*62-142, 815), text="4", font = font, align ="centre")
    draw.text((3*i*62-115, 815), text="7", font = font, align ="centre")
    draw.text((3*i*62-80, 815), text="3", font = font, align ="centre")
    draw.text((3*i*62-52, 815), text="6", font = font, align ="centre")
    draw.text((3*i*62-18, 815), text="2", font = font, align ="centre")
    draw.text((3*i*62+10, 815), text="5", font = font, align ="centre")

for i in range(6):
    draw.text((6*i*62+114, 345), text="16", font = font, align ="centre")
    draw.text((6*i*62+240, 345), text="18", font = font, align ="centre")
    draw.text((6*i*62+365, 345), text="20", font = font, align ="centre")

font = ImageFont.truetype('ARIAL.TTF', 25)
draw.text((30, 980), text="C - Years of Hard Times, Low Prices, and a good time to buy Cryptos and Stocks", font = font, align ="centre")
draw.text((30, 500), text="B - Years of Good Times, How Prices, and a good time to sell Cryptos and Stocks", font = font, align ="centre")
draw.text((30, 200), text="A - Years in which panics have occurred and will occur again", font = font, align ="centre")
draw.text((30, 50), text="Made by zizzs for Sindicate", font = font, align ="centre")
draw.text((30, 100), text="With George Tritch's research", font = font, align ="centre")
pc.save('future.png')
#pc.show()