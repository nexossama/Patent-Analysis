import pandas as pd


def return_urls():
    df = pd.read_csv('csv_files/test.csv')
    url_list = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        url = row['result link']
        url_list.append(url)

    return url_list

    # return  ['https://patents.google.com/patent/US11468582B2/en', 'https://patents.google.com/patent/JP7017198B2/en', 'https://patents.google.com/patent/US11651768B2/en', 'https://patents.google.com/patent/US10430707B2/en', 'https://patents.google.com/patent/US11594024B2/en', 'https://patents.google.com/patent/JP6764547B1/en', 'https://patents.google.com/patent/US20210397501A1/en', 'https://patents.google.com/patent/US11106598B2/en', 'https://patents.google.com/patent/US20210328969A1/en', 'https://patents.google.com/patent/US10990815B2/en', 'https://patents.google.com/patent/US11748411B2/en', 'https://patents.google.com/patent/US11752030B2/en', 'https://patents.google.com/patent/US11494930B2/en', 'https://patents.google.com/patent/KR102324776B1/en', 'https://patents.google.com/patent/US11887352B2/en', 'https://patents.google.com/patent/US20200387797A1/en', 'https://patents.google.com/patent/CN109416873B/en', 'https://patents.google.com/patent/US11036215B2/en', 'https://patents.google.com/patent/US11888689B2/en', 'https://patents.google.com/patent/US20200312042A1/en', 'https://patents.google.com/patent/US20210319894A1/en', 'https://patents.google.com/patent/EP3615282B1/en', 'https://patents.google.com/patent/US11893355B2/en', 'https://patents.google.com/patent/KR102264498B1/en', 'https://patents.google.com/patent/US11195183B2/en', 'https://patents.google.com/patent/US11631039B2/en', 'https://patents.google.com/patent/US20230289666A1/en', 'https://patents.google.com/patent/US11573239B2/en', 'https://patents.google.com/patent/US11023745B2/en', 'https://patents.google.com/patent/CN110084365B/en', 'https://patents.google.com/patent/CN107342962B/en', 'https://patents.google.com/patent/US20190193273A1/en', 'https://patents.google.com/patent/US11210851B1/en', 'https://patents.google.com/patent/CN111368319B/en', 'https://patents.google.com/patent/US20220188918A1/en', 'https://patents.google.com/patent/KR102139740B1/en', 'https://patents.google.com/patent/CN105137967B/en', 'https://patents.google.com/patent/CN111524602B/en', 'https://patents.google.com/patent/US11462090B2/en', 'https://patents.google.com/patent/US20210005085A1/en', 'https://patents.google.com/patent/CA3055148C/en', 'https://patents.google.com/patent/US10268974B2/en', 'https://patents.google.com/patent/TWI622953B/en', 'https://patents.google.com/patent/US11878682B2/en', 'https://patents.google.com/patent/US20190115097A1/en', 'https://patents.google.com/patent/US20190236416A1/en', 'https://patents.google.com/patent/WO2022000188A1/en', 'https://patents.google.com/patent/US10601456B2/en', 'https://patents.google.com/patent/CN111600851B/en', 'https://patents.google.com/patent/US11816561B2/en', 'https://patents.google.com/patent/US11508361B2/en', 'https://patents.google.com/patent/US9349103B2/en', 'https://patents.google.com/patent/US10930386B2/en', 'https://patents.google.com/patent/US10922464B2/en', 'https://patents.google.com/patent/US8566143B2/en', 'https://patents.google.com/patent/US20210391089A1/en', 'https://patents.google.com/patent/US11473407B2/en', 'https://patents.google.com/patent/CN112711937B/en', 'https://patents.google.com/patent/CN111367445B/en', 'https://patents.google.com/patent/US11783658B2/en', 'https://patents.google.com/patent/CN106214123B/en', 'https://patents.google.com/patent/EP3534283A1/en', 'https://patents.google.com/patent/US11734885B2/en', 'https://patents.google.com/patent/US11694418B2/en', 'https://patents.google.com/patent/CN108784655B/en', 'https://patents.google.com/patent/KR102390313B1/en', 'https://patents.google.com/patent/CN111052332B/en', 'https://patents.google.com/patent/US11756042B2/en', 'https://patents.google.com/patent/US11580090B2/en', 'https://patents.google.com/patent/CN111279328B/en']

print(len(return_urls()))




