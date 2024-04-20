import rembg
from PIL import Image

def remove_white_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as input_file:
        input_image = rembg.remove(input_file.read(), background_color='white')

    with open(output_image_path, "wb") as output_file:
        output_file.write(input_image)

input_image_path = r"images/image.jpg"
output_image_path = r"images/output_image.png"

remove_white_background(input_image_path, output_image_path)

# Open the processed image with PIL
processed_image = Image.open(output_image_path)
processed_image.show()