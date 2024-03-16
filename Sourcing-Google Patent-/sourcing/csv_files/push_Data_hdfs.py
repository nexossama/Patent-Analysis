from hdfs import InsecureClient

hdfs_host = 'localhost'
hdfs_port = 50070

# Create an HDFS client
client = InsecureClient(f'http://{hdfs_host}:{hdfs_port}')

def push_data(input_file):
    client.upload('/raw-data-stage-0', input_file)

    print(f"File {input_file} uploaded to HDFS")

csv_files = ['downloaded_file1.csv','downloaded_file0.csv']
for file in csv_files :
    push_data(file)