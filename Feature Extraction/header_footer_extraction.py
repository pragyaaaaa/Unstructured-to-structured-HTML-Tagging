import os
import zipfile
from bs4 import BeautifulSoup
import csv

def extract_header_footer(docx_file):
    with zipfile.ZipFile(docx_file) as myzip:
        header_text = ""
        footer_text = ""

        if 'word/header1.xml' in myzip.namelist():
            with myzip.open('word/header1.xml') as myfile:
                soup = BeautifulSoup(myfile.read(), features="xml")
                header = soup.find_all('w:t')
                header_text = ' '.join([t.text for t in header])
                
        if 'word/footer1.xml' in myzip.namelist():
            with myzip.open('word/footer1.xml') as myfile:
                soup = BeautifulSoup(myfile.read(), features="xml")
                footer = soup.find_all('w:t')
                footer_text = ' '.join([t.text for t in footer])

        return header_text, footer_text

def is_empty(string):
    return string is None or string.strip() == ""

input_dir = 'Dataset'
output_dir = 'Res'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(input_dir):
    if file_name.endswith('.docx'):
        file_path = os.path.join(input_dir, file_name)
        header_text, footer_text = extract_header_footer(file_path)

        output_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".csv")
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Text', 'is_header', 'is_footer'])

            if not is_empty(header_text):
                writer.writerow([header_text, True, False])

            if not is_empty(footer_text):
                writer.writerow([footer_text, False, True])

            if is_empty(header_text) and is_empty(footer_text):
                writer.writerow(["", False, False])
