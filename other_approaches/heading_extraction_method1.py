from bs4 import BeautifulSoup
import pandas as pd
import os

# filenames=["html_db\samplepdf1.html",
# "html_db\samplepdf100.html"]
filenames=["html_db\samplepdf1.html",
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

    # Remove irrelevant tags
    # for tag in soup(["style", "script"]):
    #     tag.decompose()

    # Create an empty list to store the data
    data = []

    
    for heading in soup.find_all("div", {"class":["h6","h7","ha","hb","hc","hd","h8","h9","h10","h11","h12","h13","hc","he","h5"]}):
        text=heading.text
        is_all_caps = text.isupper()
        data.append([text,is_all_caps])

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Text","Is Capitalized"])

    # Store the data in a CSV file with the same name as the uploaded HTML file
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    df.to_csv(csv_filename, index=False)

    print (file,"is converted")
