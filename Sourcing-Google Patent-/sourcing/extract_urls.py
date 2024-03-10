import pandas as pd


def return_urls():
    df = pd.read_csv('csv_files/test.csv')
    url_list = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        url = row['result link']
        url_list.append(url)

    # return url_list


    return  ['https://patents.google.com/patent/CN111666898B/en', 'https://patents.google.com/patent/KR20200014046A/en', 'https://patents.google.com/patent/CN112051433A/en', 'https://patents.google.com/patent/JP2014002482A/en', 'https://patents.google.com/patent/US20200296498A1/en', 'https://patents.google.com/patent/CN108857600A/en', 'https://patents.google.com/patent/CN111404808A/en', 'https://patents.google.com/patent/US20220198486A1/en', 'https://patents.google.com/patent/JP7083269B2/en', 'https://patents.google.com/patent/CN113920123B/en', 'https://patents.google.com/patent/CN111553327A/en']
# print(return_urls())


