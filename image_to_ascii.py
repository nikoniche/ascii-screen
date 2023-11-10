import json
from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = [" ", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
INVERTED_CHARS = [x for x in reversed(ASCII_CHARS)]

VERTICAL_RATIO = 0.6

def convert_image_to_text(org_image: Image, font_size: int, new_pixel_width=None, inverted=False) -> str:
    """Converts an image to a txt file."""

    # resize image according to a new width
    def resize_image(image: Image):
        width, height = image.size
        ratio = height / width

        new_width = round(width // font_size * 1.67) if new_pixel_width is None \
            else round(new_pixel_width // font_size * 1.67)

        new_height = int(new_width * ratio * VERTICAL_RATIO)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    # convert each pixel to grayscale
    def grayify(image):
        grayscale_image = image.convert("L")
        return grayscale_image

    # convert pixels to a string of ascii characters
    def pixels_to_ascii(image):
        pixels = image.getdata()
        chars = ASCII_CHARS if not inverted else INVERTED_CHARS
        characters = "".join([chars[pixel // 25] for pixel in pixels])
        return characters

    # convert image to ascii
    resized_image = resize_image(org_image)
    org_image = resized_image
    new_image_data = pixels_to_ascii(grayify(org_image))

    # format
    pixel_count = len(new_image_data)
    new_width = org_image.size[0]
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    return ascii_image
