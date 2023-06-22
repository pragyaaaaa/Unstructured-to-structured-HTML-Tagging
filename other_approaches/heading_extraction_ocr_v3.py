from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import cv2
import re

filenames=[
"html_db\samplepdf1.html",
]

for file in filenames:
    # Load the HTML file
    filename = file
    with open(filename, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the maximum heading level used in the div tags
    valid_tags = soup.find_all("div", {"class": ["h5", "h6", "hc", "he", "h7", "h8", "h9", "h10", "h13"]})
    max_heading_level = 0
    for tag in valid_tags:
        level = int(re.search(r"h(\d+)", tag['class'][0]).group(1))
        if level > max_heading_level:
            max_heading_level = level

    # Create an empty list to store the data
    data = []

    # Extract information from each heading with the maximum level
    for heading in soup.find_all("div", {"class": "h{}".format(max_heading_level)}):
        # Extract the text
        text = heading.text.strip()

        # Check if the text is in all caps
        is_all_caps = text.isupper()

        # Check if the extracted text is the only text on that particular line
        is_alone = False
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(text, font, 1, 2)[0]
        img = np.zeros((textsize[1], textsize[0], 3), dtype=np.uint8)
        cv2.putText(img, text, (0, textsize[1]-5), font, 1, (255, 255, 255), 2)
        cv2.imwrite('temp.png', img)

        img = cv2.imread("temp.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        x, y, w, h = cv2.boundingRect(img)
        if w == img.shape[1]:
            is_alone = True

        # Append the data to the list
        data.append([text,is_all_caps, is_alone])

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Text", "Is Caps ", "Is Alone"])

    # Store the data in a CSV file with the same name as the uploaded HTML file
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    df.to_csv(csv_filename, index=False)

    print(file,"is extracted")
