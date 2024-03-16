from hdfs import InsecureClient
from get_data_hdfs import get_data


hdfs_host = 'localhost'
hdfs_port = 50070

# Create an HDFS client
client = InsecureClient(f'http://{hdfs_host}:{hdfs_port}')

def save(name):
    with client.write(f'/raw-data-stage-1/{name}', overwrite=True) as writer:
        get_data().to_csv(writer, index=False)
    print("the merged data is uploaded to HDFS")


save('merged_data.csv')