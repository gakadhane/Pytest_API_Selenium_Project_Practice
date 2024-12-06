import requests


# Define login credentials
username = "your_username"
password = "your_password"

# Authentication endpoint to get the JWT token
login_url = "https://api.example.com/login"

# Prepare data (e.g., credentials)
data = {
    "username": username,
    "password": password
}

# Make a POST request to get the JWT token
response = requests.post(login_url, json=data)

# If successful, extract the JWT token
if response.status_code == 200:
    token_data = response.json()
    jwt_token = token_data.get('token')
    print(f"JWT Token: {jwt_token}")
else:
    print(f"Failed to fetch JWT token. Status Code: {response.status_code}, Response: {response.text}")
