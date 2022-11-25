import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "#location du module de tesseract dans ton ordi"

img = cv2.imread("")

bike_info = pytesseract.image_to_string(img)

print(bike_info)