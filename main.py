import rembg
from PIL import Image, ImageOps

def remove_white_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as input_file:
        input_image = rembg.remove(input_file.read(), background_color='white')

    with open(output_image_path, "wb") as output_file:
        output_file.write(input_image)

def add_white_background(input_image_path, output_image_path):
    processed_image = Image.open(input_image_path)
    bg = Image.new('RGB', processed_image.size, (255, 255, 255))
    bg.paste(processed_image, (0, 0), processed_image)
    bg.save(output_image_path)

input_image_path = r"images/image.webp"
output_image_path = r"images/output_image.png"

remove_white_background(input_image_path, output_image_path)
add_white_background(output_image_path, output_image_path + "_with_bg.png")

# Open the processed image with PIL
processed_image = Image.open(output_image_path + "_with_bg.png")
processed_image.show()
