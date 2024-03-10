import requests

urls = ["https://patents.google.com/xhr/query?url=q%3D(l'intelligence%2Bartificial%2Bdans%2Bl'education)%26oq%3Dl'intelligence%2Bartificial%2Bdans%2Bl'education&exp=&download=true",'https://patents.google.com/xhr/query?url=q%3D(artificial%2Bintelligence%2Beducation)%26page%3D1&exp=&download=true']

# urls = ['https://patents.google.com/xhr/query?url=q%3D(artificial%2Bintelligence%2Beducation)%26page%3D1&exp=&download=true']
def download():
    # URL of the CSV file
    for url in urls:
        i=0
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content of the response (the CSV data)
            csv_data = response.content

            # Save the CSV data to a file
            with open(f'downloaded_file{i}.csv', 'wb') as f:
                f.write(csv_data)
            i+=1

            print("CSV file downloaded successfully!")
        else:
            print("Failed to download CSV file. Status code:", response.status_code)
            print(response.text)

download()