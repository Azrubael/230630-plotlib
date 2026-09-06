from pathlib import Path
from PIL import Image

# Input image
input_path = "food_icons.png"

# Folder where the 16 cropped icons will be saved
output_dir = Path("food_icons_split")
output_dir.mkdir(exist_ok=True)

# Open the image
image = Image.open(input_path)

# The image contains 4 columns × 4 rows = 16 equal-sized sections
columns = 4
rows = 4

width, height = image.size
icon_width = width // columns
icon_height = height // rows

# Crop and save each icon
icon_number = 1

for row in range(rows):
    for column in range(columns):
        left = column * icon_width
        top = row * icon_height
        right = left + icon_width
        bottom = top + icon_height

        icon = image.crop((left, top, right, bottom))

        output_path = output_dir / f"icon_{icon_number:02d}.png"
        icon.save(output_path)

        icon_number += 1

print(f"Saved {icon_number - 1} icons to '{output_dir}'")
