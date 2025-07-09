import requests

url = "https://datalemur.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print(response.text)  # This prints the raw HTML content
else:
    print("Failed to retrieve the page")
