import pytesseract
import requests

from PIL import Image
from PIL import ImageFilter
from io import BytesIO

def img_to_text(url, lang):

    image = url_to_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image, lang)


def url_to_image(url):
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img
