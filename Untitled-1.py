
#import easyocr
#reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
#result = reader.readtext(r'F:\\FAHMEED ANTLER\\letter detection photo\\images (2).png')
#print(result)
import cv2
img = cv2.imread('F:\\FAHMEED ANTLER\\letter detection photo\\H9410065158.jpg')

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

coordinates = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        print(f"Clicked at pixel coordinates: ({x}, {y})")

# Create a window and set the callback function
cv2.namedWindow('Original Image')
cv2.setMouseCallback('Original Image', mouse_callback)

# Keep the window open until 'q' is pressed
while True:
    cv2.imshow('Original Image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

# Print the final list of coordinates
print("Selected Coordinates:", coordinates)

# Example coordinates (replace with your own)
x1, y1 = coordinates[0]
x2, y2 = coordinates[1]

# Extract the ROI
roi = img[y1:y2, x1:x2]

# Display the ROI
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


