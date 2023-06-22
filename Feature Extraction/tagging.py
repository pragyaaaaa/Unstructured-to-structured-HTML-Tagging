import pandas as pd
from bs4 import BeautifulSoup
import os

# Define the word pools
fig_pool=["Figure","figure","fig","FIGURE","FIG","Fig","Figure.","figure.","fig.","FIGURE.","FIG.","Fig."]
tab_pool=["Table","table","tab","TABLE","TAB","Tab","Table","table","tab","TABLE.","TAB.","Tab."]
sh_pool=["Introduction","Abstract", "Overview", "Conclusion","References","Summary"]

# Define the function to check if a text is a heading
def is_heading(text):
    return any(word in text for word in sh_pool)

csv_dir = "results/csv_db"
html_dir = "html_db"

# Check if the results directory exists, if not create it
results_folder = "results\html_db"
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

html_file = os.listdir(html_dir)
csv_file = os.listdir(csv_dir)

for h_file, c_file in zip(html_file, csv_file):
    # Load the CSV file
    csv_filename = os.path.join(csv_dir, c_file)
    df = pd.read_csv(csv_filename)

    # Load the HTML file
    html_filename = os.path.join(html_dir, h_file)
    with open(html_filename, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all div elements with the specified class
    div_class = ["h6","h7","ha","hb","hc","hd","h8","h9","h10","h11","h12","h13","hc","he","h5"]
    divs = soup.find_all("div", {"class": div_class})

    # Loop through each div and add the s_heading, figure_heading or table_heading class if necessary
    for i, div in enumerate(divs):
        # Check if the is_heading section is true in the corresponding row of the CSV file
        if df.loc[i, "is_heading"]:
            # Add the s_heading class to the div's class attribute
            div["class"] = div["class"] + ["s_heading"]
        # Check if the is_figure_heading section is true in the corresponding row of the CSV file
        elif df.loc[i, "is_figure_heading"] and any(word in df.loc[i, "Text"].split()[:3] for word in fig_pool):
            # Add the figure_heading class to the div's class attribute
            div["class"] = div["class"] + ["figure_heading"]
        # Check if the is_table_heading section is true in the corresponding row of the CSV file
        elif df.loc[i, "is_table_heading"] and any(word in df.loc[i, "Text"].split()[:3] for word in tab_pool):
            # Add the table_heading class to the div's class attribute
            div["class"] = div["class"] + ["table_heading"]

    # Save the modified HTML to a new file in the results folder
    html_output_filename = os.path.splitext(h_file)[0] + "_output.html"
    html_output_path = os.path.join(results_folder, html_output_filename)
    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(h_file, "is tagged and saved")