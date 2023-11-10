from PIL import Image, ImageGrab
from image_to_ascii import convert_image_to_text


def _get_screenshot() -> Image:
    ss = ImageGrab.grab()
    return ss


def convert_screenshot_to_ascii(font_size, invert) -> str:
    screenshot = _get_screenshot()
    text = convert_image_to_text(screenshot, font_size, inverted=invert)
    return text
