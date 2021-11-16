import random
from sty import fg


def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue


def generateColour(red, green, blue):
    return fg(red, green, blue)


red, green, blue = generateRGB()
colour = generateColour(red, green, blue)

text = ['Look!', 'Can you imagine?', "This string changes it's colour randomly"]

for i in text:
    print(colour, i)
