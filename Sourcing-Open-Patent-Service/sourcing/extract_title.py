import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('csv_files/test.csv')

def extract_title(code):
    code_title_dict = {}

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the code from the link
        code1 = row['result link'].split('/')[-2]
        # Map the code to the title in the dictionary
        code_title_dict[code1] = row['title']

    return code_title_dict[code]

