import pytesseract
import cv2
from PIL import Image
import numpy as np

# Specify the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Given pixel coordinates for the region of interest
x1, y1, x2, y2 = 529, 430, 820, 500  # Replace with the actual coordinates

img = cv2.imread('F:\\FAHMEED ANTLER\\letter detection photo\\H9410065158.jpg')  
resize_dimensions = (1270, 689)
resized_img = cv2.resize(img, resize_dimensions)

# Extract the region of interest based on the given coordinates
roi = resized_img[y1:y2, x1:x2]

# Check if the image was successfully loaded
if roi is not None:
    # Resize the ROI
    resized_roi = cv2.resize(roi, (200, 100))  # Replace with the desired constant size

    # Convert the resized ROI to grayscale
    gray_image = cv2.cvtColor(resized_roi, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Display the binary image
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_rgb = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2RGB)

    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.fromarray(img_rgb))

    print("Extracted Text:", text)
else:
    print(f"Error: Unable to extract region of interest")
