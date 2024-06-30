import requests


def get_token():
    # Replace with your client credentials
    client_id = 'c003a37f-024f-462a-b36d-b001be4cd24a'
    client_secret = '32a39620-32b3-4307-9aa1-511e3d7f48a8'

    # Endpoint URL to request the token
    token_url = 'https://rest.arbeitsagentur.de/oauth/gettoken_cc'

    # Data to be sent in the POST request body
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    # Send the POST request to get the token
    response = requests.post(token_url, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the token from the JSON response
        token = response.json().get('access_token')
        print(f"Successfully obtained token")
        return token
    else:
        print(f"Failed to obtain token. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        exit(1)
