import requests

url = "https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend=5101087&offset=0"
headers = {'Origin': 'https://sscasn.bkn.go.id'}

# Make the API request
response = requests.get(url, headers=headers)

# Print the response status code
print(response.status_code)

# Print the response content
print(response.json())
