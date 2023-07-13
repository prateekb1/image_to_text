from PIL import Image
import pytesseract


image_1 = "image1.png"
image_2 = "image4.png"

img_obj_1 = Image.open(image_2)

text_1 = pytesseract.image_to_string(img_obj_1)
print(text_1)