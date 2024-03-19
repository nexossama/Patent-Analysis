import pandas as pd
import os
def remove(input_file):

    # Input and output file paths
    output_file = 'test.csv'

    if os.path.exists(output_file):
        # Read input CSV file skipping the first row
        df = pd.read_csv(input_file, skiprows=2)

        # Write data to output file
        df.to_csv(output_file, index=False,mode='a')

    else:
        # Read input CSV file skipping the first row
        df = pd.read_csv(input_file, skiprows=1)

        # Write data to output file
        df.to_csv(output_file, index=False)

    print("First line removed and data written to", output_file)


