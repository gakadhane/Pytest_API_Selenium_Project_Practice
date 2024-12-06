import requests

# Define the token (usually you fetch it through a different endpoint first)
token = "your_bearer_token_here"
# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

# Define the endpoint you want to access
endpoint = f"{BASE_URL}/booking"

# Make the request using the Bearer token
headers = {
    "Authorization": f"Bearer {token}"  # Bearer Token in the Authorization header
}

response = requests.get(endpoint, headers=
import requests
from requests.auth import HTTPBasicAuth

# Define API credentials (example)
username = "ravi707@mailinator.com"  # Your username
password = "Rr@778998445665"  # Your password
# Base URL for the API
BASE_URL = "https://www.mystoriesmatter.com/user?redirectUrl=%2Fsettings"
# Authentication header (using HTTPBasicAuth)
auth = HTTPBasicAuth(username, password)
# Define the endpoint for fetching token (if applicable)
token_endpoint = f"{BASE_URL}/auth"
# Make the request to the auth endpoint
response = requests.get(token_endpoint, auth=auth)
# Check if the request was successful and extract the token
if response.status_code == 200:
    token_data = response.json()
token = token_data.get('token')  # Assuming the token is in 'token' field
print(f"Fetched Token: {token}")
else:
print(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")
headers)

# Check if the request was successful
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}, Response: {response.text}")

    -----
    BASE_URL = "https://www.mystoriesmatter.com/user"

auth = HTTPBasicAuth(username, password)

token_endpoint = f"{BASE_URL}?redirectUrl=%2Fsettings"


