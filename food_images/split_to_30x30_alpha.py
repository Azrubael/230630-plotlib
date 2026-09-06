from pathlib import Path
from PIL import Image

# Input image
input_path = "food_icons_alpha.png"

# Folder where the resized icons will be saved
output_dir = Path("food_icons_alpha")
output_dir.mkdir(exist_ok=True)

# Desired output size
output_size = (30, 30)

# Open the image
image = Image.open(input_path)

# The image contains 4 columns × 4 rows = 16 equal-sized sections
columns = 4
rows = 4

width, height = image.size
icon_width = width // columns
icon_height = height // rows

icon_number = 1

for row in range(rows):
    for column in range(columns):
        left = column * icon_width
        top = row * icon_height
        right = left + icon_width
        bottom = top + icon_height

        # Crop one icon
        icon = image.crop((left, top, right, bottom))

        # Resize it to 30 × 30 pixels
        icon = icon.resize(output_size, Image.Resampling.LANCZOS)

        # Save the resized icon
        output_path = output_dir / f"food_icon_{icon_number:02d}.png"
        icon.save(output_path)

        icon_number += 1

print(f"Saved {icon_number - 1} resized icons to '{output_dir}'")

