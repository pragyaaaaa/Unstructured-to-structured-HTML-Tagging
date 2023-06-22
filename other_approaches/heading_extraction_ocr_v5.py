from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import cv2

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

filenames=[
"html_db\samplepdf15.html",
"html_db\samplepdf1.html"

]

for file in filenames:
    # Load the HTML file
    filename = file
    with open(filename, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Create an empty list to store the data
    data = []

    # Extract information from each div with attributes h5, h6, hc, he, h7, h8, h9, h10, h13
    for heading in soup.find_all("div", {"class": ["h5", "h6", "hc", "he", "h7", "h8", "h9", "h10", "h13"]}):
        # Extract the text
        text = heading.text.strip()

        # Check if the text is in all caps
        is_all_caps = text.isupper()

        # Check if the extracted text is the only text on that particular line
        is_alone = False

        # Extract font style using Tesseract OCR
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.putText(img, text, (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imwrite('temp.png', img)

        img = cv2.imread("temp.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Calculate the mean intensity of the text region and the surrounding region
        x, y, w, h = cv2.boundingRect(thresh)
        if w == 0 or h == 0:
            text_region_mean = 0
            surrounding_region_mean = 0
        else:
            text_region_mean = np.mean(thresh[y:y+h, x:x+w])
            surrounding_region_mean = (np.mean(thresh[y-10:y, x:x+w]) + np.mean(thresh[y+h:y+h+10, x:x+w]))/2

        # Check if the text is darker than the surrounding text
        is_bold = False
        if text_region_mean < surrounding_region_mean:
            is_bold = True

        if w == img.shape[1]:
            is_alone = True

        # Append the data to the list
        data.append([text, is_all_caps, is_alone, is_bold])

    print (file, "is converted")

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Text", "Is Caps", "Is Alone", "Is Bold"])

    # Store the data in a CSV file with the same name as the uploaded HTML file
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    df.to_csv(csv_filename, index=False)