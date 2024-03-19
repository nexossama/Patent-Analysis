import pandas as pd
from hdfs import InsecureClient

hdfs_host = 'localhost'
hdfs_port = 50070

# Create an HDFS client
client = InsecureClient(f'http://{hdfs_host}:{hdfs_port}')


def get_data():
    # Step 1: List all CSV files in the 'raw-data' directory
    file_list = client.list('/raw-data-stage-0')

    # Step 2: Read each CSV file into a pandas DataFrame and perform processing
    dfs = []
    for file_name in file_list:
        if file_name.endswith('.csv'):
            with client.read(f'/raw-data-stage-0/{file_name}') as reader:
                df = pd.read_csv(reader,skiprows=1)

                dfs.append(df)

    # Step 3: Concatenate all DataFrames into one
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df



