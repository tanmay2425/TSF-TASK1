# Importing necessary modules
import cv2
import pytesseract as ptr

# Path of tesseract on my PC
ptr.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# Input image path
test_img = cv2.imread('test3.png')

# pyteseeract accepts RGB Value, openCV does it in BGR
# Converting test image from BGR to RGB
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

height_img, width_img, _ = test_img.shape
data = ptr.image_to_data(test_img)

for x, c in enumerate(data.splitlines()):
    if x != 0:
        c = c.split()
        if len(c) == 12:
            # Initializing 4 variables for x-coordinate, y- coordinate, width, height
            x, y, w, h = int(c[6]), int(c[7]), int(c[8]), int(c[9])

            # Creating boxes around the characters
            cv2.rectangle(test_img, (x, y), (w + x, h + y), (0, 0, 255), 2)

            # Adding labels around the characters
            cv2.putText(test_img, c[11], (x, y),

                        cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

# Displaying the image & giving it a window name
cv2.imshow('Result', test_img)

# Displaying the image until closed
cv2.waitKey(0)
