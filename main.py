#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import sys
import textwrap
import uuid
import random
import os

# quote font
system_font = "fonts/Quote.ttf"
# font size
system_font_size = 50

# image type
image_type = "RGBA"

# image size
image_size_x = 1200 # x
image_size_y = 600  # y

# background color
#colors = [(255,0,0), (51, 0, 51), (0,0,255), (0,0,0)]
colors = [(255,255,255)]

def alingText(text_size, text):
    wrapper = textwrap.TextWrapper(width = system_font_size) #*3
    text_element = wrapper.wrap(text = text)
    return text_element

def centerPixel(strlen, line_no):
    temp = []
    x = image_size_x / 2
    y = image_size_y / 2
    t = (strlen * system_font_size) / 6
    temp.append(x - t)
    temp.append(y - (system_font_size * line_no))
    return temp

def createImage(text, image_name):
    fonts = ImageFont.truetype(system_font, system_font_size)
    system_color = random.choice(colors)
    img = Image.new(image_type, (image_size_x, image_size_y), (system_color[0], system_color[1], system_color[2]))
    draw = ImageDraw.Draw(img)
    text_element = alingText(fonts.getsize(text), text)
    line = len(text_element)/2
    for element in text_element:
        points = centerPixel(len(element), line)
        draw.text((points[0], points[1]), element, (0, 0, 0), font=fonts)
        draw = ImageDraw.Draw(img)
        line = line - 1.5
    img.save(image_name)



with open("quotes.txt", "r") as a_file:
  for line in a_file:
    # read quote
    quote_text = line
    # create unique name
    image_name = 'images\{name}.png'.format(name = str(uuid.uuid4()))
    # create an image
    createImage(quote_text, image_name)
