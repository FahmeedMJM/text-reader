import pytesseract
import cv2
from PIL import Image
import numpy as np

# Specify the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  



coordinates = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        coordinates.append((x, y))
        cv2.rectangle(img, coordinates[0], coordinates[1], (0, 255, 0), 2)
        cv2.imshow("Image", img)

img = cv2.imread('F:\\FAHMEED ANTLER\\letter detection photo\\H9410065158.jpg')  

display_img = img.copy()

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

cv2.imshow("Image", display_img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break

x1, y1 = coordinates[0]
x2, y2 = coordinates[1]
roi = img[y1:y2, x1:x2]




# Check if the image was successfully loaded
if roi is not None:
    # Convert BGR to RGB if needed (OpenCV loads images in BGR format)
    
    

    image = cv2.resize(roi,(roi.shape[1]*5,roi.shape[0]*5,))

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    
     
   
    #img_grb = cv2.cvtColor(new_pillow_img, cv2.COLOR_RGB2BGR)
    #gray_image = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Binary Image',binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_rgb = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2RGB)

    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.fromarray(img_rgb))

    print("Extracted Text:", text)
    

    #print(text)
   
else:
    print(f"Error: Unable to load image")

print("file path:",__file__)