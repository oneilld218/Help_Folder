"""
Todo
skriv til billede
gem billede
størrelse: 640x320 pixels
inputs: [navn, efternavn] & dato
"""

import os
import shutil
from PIL import Image, ImageDraw, ImageFont


# Script path
script_path = os.path.dirname(os.path.realpath(__file__))
# Change directory to script path
os.chdir(script_path)

# Picture details
origional_picture = "Covidpass.png"
customized_picture = "Customized_picture.png"

font = "FreeMono.ttf"

# Folder for customized pictures
try:
    # Create folder for new image
    os.mkdir("Customized_Pictures")
    # Copy and paste the origional photo into the new folder
    os.system(f"cp {origional_picture} {customized_picture}")
    os.system(f"mv {customized_picture} Customized_Pictures")
    # Change directory to new folder
    os.chdir("Customized_Pictures")
except:
    os.system(f"cp {origional_picture} {customized_picture}")
    os.system(f"mv {customized_picture} Customized_Pictures")
    # Change directory to new folder, if folder already exists
    os.chdir("Customized_Pictures")

# Draw or write on picture
with Image.open(customized_picture) as img:
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, 20)
    width, height = img.size
    
    # draw.line((0,0) + img.size, fill=128)
    # draw.line((0, img.size[1], img.size[0], 0), fill=128)
    draw.text((width//2, height//2), "Text One", (0, 0, 0), font=font)
    
    img.show()
