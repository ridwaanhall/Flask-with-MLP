import requests
import json
from Config import BASE_URL

# Define the URL
url = BASE_URL + '/predict'

# Define the data to be sent in JSON format
data = {'features': [1, 0]}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, data=json_data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response data
    print(response.json())
    # print prettier
    # print(json.dumps(response.json(), indent=4))
else:
    print('Error:', response.status_code)
