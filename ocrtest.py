from PIL import Image
import pytesseract
imageObject=Image.open('QQ20170624-094346@2x.png')
print (imageObject)
print (pytesseract.image_to_string(imageObject))