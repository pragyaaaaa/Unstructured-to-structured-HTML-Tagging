import re
from bs4 import BeautifulSoup
import pandas as pd
import os


# Define the word pool
pool = ["Introduction", "Abstract", "Overview", "Conclusion", "References", "Summary"]

# Define the function to check if a text is a heading
def is_heading(text):
    return any(word in text for word in pool)

# Create the results/csv_db directory if it doesn't exist
csv_dir = "results/csv_db"
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

# Get a list of all the HTML files in the html_db directory
html_dir = "html_db"
filenames = os.listdir(html_dir)
html_files = [filename for filename in filenames if filename.endswith(".html")]

for file in html_files:
    # Create the HTML file path
    html_path = os.path.join(html_dir, file)

    # Load the HTML file
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Create an empty list to store the data
    data = []

    # Define regular expressions to match the specified patterns
    pattern_roman_numeral = "^(IX|IV|V?I{0,3})\."
    pattern_number = "^\d+\. "

    for heading in soup.find_all("div", {"class":["h6","h7","ha","hb","hc","hd","h8","h9","h10","h11","h12","h13","hc","he","h5"]}):
        text = heading.text
        is_all_caps = text.isupper()

        # Check if the text is preceded by the specified patterns
        is_roman_numeral = bool(re.match(pattern_roman_numeral, text))
        is_number = bool(re.match(pattern_number, text))

        # Check if the text is a heading
        is_heading_text = is_roman_numeral or is_all_caps or is_number or is_heading(text)

        data.append([text, is_all_caps, is_roman_numeral, is_number, is_heading_text])

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Text","Is Capitalized", "Is Roman Numeral", "Is Number", "is_heading"])

    # Store the data in a CSV file with the same name as the uploaded HTML file
    csv_filename = os.path.splitext(os.path.basename(file))[0] + ".csv"
    csv_path = os.path.join(csv_dir, csv_filename)
    df.to_csv(csv_path, index=False)

    print(file, "is converted into csv format")
