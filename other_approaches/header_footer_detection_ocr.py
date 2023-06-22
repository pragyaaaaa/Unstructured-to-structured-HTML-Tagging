import fitz
import cv2
import numpy as np
import pytesseract
import os
import shutil

# Load the PDF into the code
pdf_file = 'TestPdf\samplepdf1.pdf'
pdf_doc = fitz.open(pdf_file)

# Convert the pages of the PDF into temporary images
for page_num in range(pdf_doc.page_count):
    page = pdf_doc[page_num]
    pix = page.get_pixmap(alpha=False)
    output_path = f'temp_image_{page_num}.png'
    pix.save(output_path)

# Create a copy of the images
for i in range(pdf_doc.page_count):
    shutil.copy(f'temp_image_{i}.png', f'image_{i}.png')

# Convert the first copy of the image into black and white pixels using Otsu's method
for i in range(pdf_doc.page_count):
    img = cv2.imread(f'image_{i}.png', cv2.IMREAD_GRAYSCALE)
    ret, thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(f'thresh_image_{i}.png', thresh_img)

# Traverse the pixels from bottom up and create a frame that includes the black pixels
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for i in range(pdf_doc.page_count):
    img = cv2.imread(f'image_{i}.png', cv2.IMREAD_GRAYSCALE)
    thresh_img = cv2.imread(f'thresh_image_{i}.png', cv2.IMREAD_GRAYSCALE)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    bottom_pixels = thresh_img[y + h - 1, x:x + w]
    if np.all(bottom_pixels == 255):
        top_pixels = thresh_img[y - 1, x:x + w]
        if np.all(top_pixels == 0):
            frame = img[y:y + h, x:x + w]
            cv2.imwrite(f'frame_{i}.png', frame)

# Extract the text from the frame using OCR tools
for i in range(pdf_doc.page_count):
    frame = cv2.imread(f'frame_{i}.png', cv2.IMREAD_GRAYSCALE)
    text = pytesseract.image_to_string(frame)
    with open(f'page_{i}.csv', 'w', encoding='utf-8') as f:
        f.write(text)

# Delete the temporary images and threshold images
for i in range(pdf_doc.page_count):
    os.remove(f'temp_image_{i}.png')
    os.remove(f'image_{i}.png')
    os.remove(f'thresh_image_{i}.png')
