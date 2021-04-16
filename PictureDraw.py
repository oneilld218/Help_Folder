"""
Todo
inputs: [navn, efternavn] & dato
"""

import os
import datetime
from PIL import Image, ImageDraw, ImageFont


# Script path
script_path = os.path.dirname(os.path.realpath(__file__))
# Change directory to script path
os.chdir(script_path)

# Picture details
origional_picture = "Origional.png"
customized_picture = "Customized_picture.png"

# Customize settings
font = "FreeMono.ttf"

# Text details
first_name = "Jane"
last_name = "Doe"
date = datetime.datetime.now()
day = date.strftime(r"%d/%m/%Y")
time = date.strftime("%H:%M")


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
    # Change directory to new folder
    os.chdir("Customized_Pictures")


# Draw or write on picture
with Image.open(customized_picture) as img:
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, 20)
    width, height = img.size
    
    # Width: 540 | Height: 961
    draw.text((100, 250), last_name, (0, 0, 0), font=font) # First Name
    draw.text((350, 250), first_name, (0, 0, 0), font=font) # Last Name
    draw.text((370, 338), day, (0, 0, 0), font=font) # Day
    draw.text((40, 365), time, (0, 0, 0), font=font) # Time
    
    """ Uncomment to save image """
    # img.save(customized_picture)
    img.show()
