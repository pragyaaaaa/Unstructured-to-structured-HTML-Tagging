from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os

# Load the HTML file
filename = "feature_extraction\samplepdf8.html"
with open(filename, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Remove irrelevant tags
for tag in soup(["style", "script"]):
    tag.decompose()

# Extract the text
text = " ".join(tag.string for tag in soup.strings)

# Initialize a TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the text data
features = vectorizer.fit_transform([text])

# Convert the features to a Pandas DataFrame
features_df = pd.DataFrame(features.toarray(), columns=vectorizer.get_feature_names())

# Store the features in a CSV file with the same name as the uploaded HTML file
csv_filename = os.path.splitext(filename)[0] + ".csv"
features_df.to_csv(csv_filename, index=False)