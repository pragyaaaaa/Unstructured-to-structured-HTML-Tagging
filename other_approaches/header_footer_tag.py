import csv
import os
from bs4 import BeautifulSoup

html_dir = "html_db"
csv_dir = "csv_db"
output_dir = "results/html_db"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each CSV file
for csv_file in os.listdir(csv_dir):
    csv_path = os.path.join(csv_dir, csv_file)
    with open(csv_path, "r") as f_csv:
        csv_reader = csv.DictReader(f_csv)
        for row in csv_reader:
            # Extract text, is_header, and is_footer from the CSV row
            text = row["Text"]
            is_header = row["is_header"].lower() == "true"
            is_footer = row["is_footer"].lower() == "true"

            # Loop through each HTML file
            for html_file in os.listdir(html_dir):
                html_path = os.path.join(html_dir, html_file)
                with open(html_path, "r", encoding="utf-8") as f_html:
                    # Parse HTML using BeautifulSoup
                    soup = BeautifulSoup(f_html, "html.parser")

                    # Find all div elements containing the text
                    divs = soup.find_all("div", text=text)

                    # Loop through each matching div
                    for div in divs:
                        # Add "header" or "footer" class to div
                        if is_header:
                            div["class"] = div.get("class", []) + ["header"]
                        if is_footer:
                            div["class"] = div.get("class", []) + ["footer"]

                    # Write modified HTML to output file
                    output_file = os.path.splitext(html_file)[0] + "_output.html"
                    output_path = os.path.join(output_dir, output_file)
                    with open(output_path, "w", encoding="utf-8") as f_output:
                        f_output.write(str(soup))
