from PIL import Image, ImageGrab
from image_to_ascii import convert_image_to_text


def _get_screenshot() -> Image:
    ss = ImageGrab.grab()
    return ss


def convert_screenshot_to_ascii() -> str:
    screenshot = _get_screenshot()
    text = convert_image_to_text(screenshot, 7, inverted=False)
    print(len(text.split("\n")[0]))
    return text
