from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import random


def fit_text(draw, text, font_path, max_width, max_height):
    """
    Fit text within a given width and height by adjusting font size.
    """
    font_size = 1
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(text, font=font)

    while text_width < max_width and text_height < max_height:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = draw.textsize(text, font=font)

    # Return the last font that was within the bounds
    return ImageFont.truetype(font_path, font_size - 1)


# Load spreadsheet data
data = pd.read_csv("names.csv")  

# Define template images and font
template_paths = [
    "templates/template_1.jpeg",
    "templates/template_2.jpeg",
    "templates/template_3.jpeg",
    "templates/template_4.jpeg",
    "templates/template_5.jpeg",
    "templates/template_6.jpeg",
    "templates/template_7.jpeg",
]
font_path = "fonts/Orbitron-Bold.ttf"

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Iterate over each name and create image
for index, row in data.iterrows():
    name = row["Name"].upper()  # Convert name to uppercase
    profile_pic_filename = row["Profile Picture"]
    folio_number = row["Folio Number"]

    # Select a random template
    template_index = random.randint(0, len(template_paths) - 1)

    # Open the selected template and profile picture
    template_image = Image.open(template_paths[template_index])
    # Determine the profile picture file extension
    profile_pic_file = f"profile_pics/{profile_pic_filename}"
    if os.path.exists(profile_pic_file + ".jpg"):
        profile_pic_file += ".jpg"
    elif os.path.exists(profile_pic_file + ".jpeg"):
        profile_pic_file += ".jpeg"

    profile_pic = Image.open(profile_pic_file) 

    # Resize profile picture to fit template
    profile_pic_resized = profile_pic.resize((1500, 1500)) 

    # Paste profile picture onto template
    profile_pic_position = (840, 1270)  # Adjust position as needed
    template_image.paste(profile_pic_resized, profile_pic_position)

    # Add name text within the white square
    draw = ImageDraw.Draw(template_image)
    max_width = 2508 - 671
    max_height = 3165 - 2855
    font = fit_text(draw, name, font_path, max_width, max_height)

    text_width, text_height = draw.textsize(name, font=font)
    name_x = 671 + (max_width - text_width) // 2
    name_y = 2855 + (max_height - text_height) // 2
    draw.text((name_x, name_y), name, font=font, fill="black")  

    # Add folio text on the right side
    folio_text = f"FOLIO:\n{folio_number:04d}"  # Add leading zeros
    font_size_folio = 500  # Increased initial font size for the folio text
    folio_font = ImageFont.truetype(font_path, font_size_folio)

    # Define folio text position and size
    folio_max_width = 500 
    folio_max_height = 1800  
    folio_x = (
        template_image.width - folio_max_width - 100
    )  # 100 pixels from the right edge
    folio_y = (template_image.height) // 2 + 300  # Centered vertically, 300 px down

    # Dynamically fit the folio text within the bounds
    folio_font = fit_text(
        draw, folio_text, font_path, folio_max_width, folio_max_height
    )
    folio_text_width, folio_text_height = draw.textsize(folio_text, font=folio_font)
    draw.multiline_text(
        (folio_x, folio_y), folio_text, font=folio_font, fill="white", align="center"
    )  # Adjust color as needed

    # Save generated image with folio number as filename
    output_filename = os.path.join("output", f"folio_{folio_number}.jpeg")
    template_image.save(output_filename)

    print(f"Generated image: {output_filename}")
