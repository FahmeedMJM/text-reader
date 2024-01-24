#cordinate
import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en']) 

# Constants for resizing and cropping
resize_dimensions = (1270, 689)
crop_coordinates = (529, 420, 820, 500)

img = cv2.imread('F:\\FAHMEED ANTLER\\letter detection photo\\H9410065158.jpg')  

# Resize the image to a constant size
resized_img = cv2.resize(img, resize_dimensions)

# Extract the region of interest based on the given cropping coordinates
x1, y1, x2, y2 = crop_coordinates
roi = resized_img[y1:y2, x1:x2]

if roi is not None:
    # Convert the ROI to grayscale
    gray_image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Display the binary image
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Perform OCR on the binary image
    result = reader.readtext(binary_image)

    print("Extracted Text:", result)
else:
    print("Error: Unable to extract region of interest")
