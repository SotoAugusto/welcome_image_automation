# Welcome Image Automation Tool
![](https://github.com/SotoAugusto/welcome_image_automation/blob/main/demo.gif)
## Description
The Welcome Image Automation Tool generates personalized images by overlaying profile pictures and text onto template images. It's designed to batch process data from a CSV file, making it easy to create custom images for multiple entries in one go.

## Why?
I had the assignment to create welcome pictures for a non-profit charity race benefiting underprivileged children with school supplies. Initially, I was given one single template and made all the images with a simple image editor on my phone. Then, over 200 people signed up for the race, and I was instructed to use 7 different templates and ensure all templates were used, as each contained different logos from all the sponsors.

This made the process a lot more time-consuming. So, being the programmer I am, I created this script to automate part of the process of my job. The Welcome Image Automation Tool saved me significant time and effort, allowing me to focus on other important tasks for the event.

## 🚀 Quick Start

### Prerequisites
Ensure you have Python and the necessary libraries installed:
```bash
pip install pandas pillow
```
### Prepare Your Data
Create a CSV file named `names.csv` with the following columns:
```plaintext
Name,Profile Picture,Folio Number
John Doe,101,101
Jane Smith,102,102
```
Place profile pictures in a folder named `profile_pics`, with filenames corresponding to the `Profile Picture` column in the CSV (e.g., `101.jpg`, `102.jpg`, `103.jpeg`, `104.jpeg`).

### Run the Script
Place your template images in a folder named `templates` and ensure you have the font file `Orbitron-Bold.ttf` in a folder named `fonts`. Then, run the script:

```bash
python script.py
```

## 📖 Usage
The script processes the data and generates images in the `output` folder. It reads each row from `names.csv`, selects a random template, and overlays the profile picture and text onto the template.

### CSV Format
- `Name`: The name to be displayed on the image (will be converted to uppercase).
- `Profile Picture`: The filename (without extension) of the profile picture.
- `Folio Number`: A unique identifier for each entry (will be zero-padded to 4 digits).

### Template Images
Place your template images in the `templates` folder. The script will randomly select a template for each image.

### Profile Pictures
Ensure all profile pictures are in the `profile_pics` folder. The script supports both `.jpg` and `.jpeg` file formats.

## Attribution
The profile pictures used in this project are courtesy of thispersondoesnotexist.com and are generated by artificial intelligence algorithms. I do not claim ownership of these images, and they are used solely for demonstration purposes.

Additionally, the templates used in this project may contain logos or images that I do not own. These logos and images are used for demonstration purposes only, and I do not claim any ownership over them.

Please ensure that you have the necessary rights and permissions before using this code or its outputs in any public or commercial capacity.

