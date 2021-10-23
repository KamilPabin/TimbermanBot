from PIL import Image

with Image.open("other.png") as image:
    image.convert('L').point(lambda p: p > 7 and 255).show()