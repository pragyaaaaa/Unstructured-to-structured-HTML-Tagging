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
"html_db\samplepdf1.html",
"html_db\samplepdf100.html",
"html_db\samplepdf101.html",
"html_db\samplepdf102.html",
"html_db\samplepdf103.html",
"html_db\samplepdf104.html",
"html_db\samplepdf105.html",
"html_db\samplepdf106.html",
"html_db\samplepdf107.html",
"html_db\samplepdf108.html",
"html_db\samplepdf14.html",
"html_db\samplepdf15.html",
"html_db\samplepdf17.html",
"html_db\samplepdf19.html",
"html_db\samplepdf2.html",
"html_db\samplepdf21.html",
"html_db\samplepdf22.html",
"html_db\samplepdf23.html",
"html_db\samplepdf24.html",
"html_db\samplepdf25.html",
"html_db\samplepdf26.html",
"html_db\samplepdf27.html",
"html_db\samplepdf29.html",
"html_db\samplepdf30.html",
"html_db\samplepdf31.html",
"html_db\samplepdf32.html",
"html_db\samplepdf33.html",
"html_db\samplepdf34.html",
"html_db\samplepdf35.html",
"html_db\samplepdf36.html",
"html_db\samplepdf37.html",
"html_db\samplepdf38.html",
"html_db\samplepdf39.html",
"html_db\samplepdf40.html",
"html_db\samplepdf41.html",
"html_db\samplepdf42.html",
"html_db\samplepdf44.html",
"html_db\samplepdf45.html",
"html_db\samplepdf46.html",
"html_db\samplepdf47.html",
"html_db\samplepdf48.html",
"html_db\samplepdf50.html",
"html_db\samplepdf51.html",
"html_db\samplepdf52.html",
"html_db\samplepdf53.html",
"html_db\samplepdf55.html",
"html_db\samplepdf56.html",
"html_db\samplepdf57.html",
"html_db\samplepdf59.html",
"html_db\samplepdf60.html",
"html_db\samplepdf8.html",

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
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        # Set configuration parameters for Tesseract OCR
        config = r"--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        font_text = pytesseract.image_to_string(img, config=config)

        # Check if font style is bold
        is_bold = "bold" in font_text.lower()

        x, y, w, h = cv2.boundingRect(img)
        if w == img.shape[1]:
            is_alone = True

        # Append the data to the list
        data.append([text, is_all_caps, is_alone, is_bold])

        print(file,"is converted")

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Text", "Is Caps", "Is Alone", "Is Bold"])

    # Store the data in a CSV file with the same name as the uploaded HTML file
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    df.to_csv(csv_filename, index=False)
