from download_csv import  download
from header_removal import remove


download()

input_file = 'downloaded_file.csv'
remove(input_file)

print('done')