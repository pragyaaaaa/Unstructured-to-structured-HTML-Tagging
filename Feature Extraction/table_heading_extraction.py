import pandas as pd
import os

# Define the word pool
pool = ["Table", "table", "tab", "TABLE", "TAB", "Tab", "Table.", "table.", "tab.", "TABLE.", "TAB.", "Tab."]

# Load the CSV files
csv_dir = "results/csv_db"
filenames = os.listdir(csv_dir)
for filename in filenames:
    csv_path = os.path.join(csv_dir, filename)
    df = pd.read_csv(csv_path)

    # Add a new column "is_table_heading"
    df["is_table_heading"] = False

    # Loop through each row in the DataFrame
    for i, row in df.iterrows():
        text = row["Text"]
        words = text.split()

        # Check if any of the first 3 words contain a word from the pool
        if any(word in words[:3] for word in pool):
            df.at[i, "is_table_heading"] = True

            # Check if the text is already marked as a heading
            if row["is_heading"]:
                df.at[i, "is_heading"] = False

            # Check if the text is already marked as a figure heading
            if row["is_figure_heading"]:
                df.at[i, "is_figure_heading"] = False

    # Save the updated DataFrame to the same CSV file
    df.to_csv(csv_path, index=False)

    print(filename, "is updated with table headings")