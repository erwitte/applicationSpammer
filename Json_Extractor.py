import requests
import Token


def fetch_job_json():
    token = Token.get_token()
    # Endpoint URL to fetch job listings
    job_search_url = 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs'

    # Example GET request with token as header parameter
    headers = {
        'OAuthAccessToken': token  # Use 'X-API-Key' if specified as an alternative
    }

    # Example query parameters
    params = {
        "was": "Backend",
        'angebotsart': '1',  # Job offer type (1 = ARBEIT)
        'wo': 'Hannover',  # Location (Berlin in this case)
        'umkreis': '50',  # Radius around location in kilometers
        'page': '1',  # Page number of results
        'size': '100',  # Number of results per page
        'pav': 'false'  # Include jobs from private employment agencies (false means not included)
    }

    # Make the GET request
    response = requests.get(job_search_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        job_data = response.json()
        print("Successfully fetched job json")
        return job_data
    else:
        print(f"Failed to fetch job data. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        exit(1)


def extract_relevant_data(json_entry):
    titel_arbeitgeber_refnr = json_entry['titel'], json_entry['arbeitgeber'], json_entry['refnr']
    return titel_arbeitgeber_refnr


def get_relevant_data():
    job_data = fetch_job_json()
    relevant_data = []
    for index in range(len(job_data["stellenangebote"])):
        relevant_data.append(extract_relevant_data(job_data["stellenangebote"][index]))
    return relevant_data
