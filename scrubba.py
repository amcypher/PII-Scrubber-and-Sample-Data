#headers = {"Content-Type": "application/json", "X-Auth-Key": key, "X-Auth-Email": email}
# Necessary Imports
import requests
import json
from pprint import pprint

# URL to fetch the data
url = "https://raw.githubusercontent.com/amcypher/PII-Scrubber-and-Sample-Data/main/pii-json.json"
# If you need to auth
# headers = {"Content-Type": "application/json", "X-Auth-Key": key, "X-Auth-Email": email}

# Method to pull data from the API
def pull_data(url):
    # Set our headers for the HTTP Request
    headers = {"Content-Type": "application/json"}
    # Try catch to handle failed HTTP Requests
    try:
        response = requests.get(url, headers=headers)
        # Return the response if HTTP 200
        if response.status_code == 200:
            return response.json()
        # Non 200 Response
        else:
            print(f'Status Code: {response.status_code}')
            return False
    except Exception as e:
        # Exception occurred
        print(f"API Fetch Failed: {e}")
        return False

def scrubba(data):
    # Removing the PII that we know exists in these Key Value Pairs
    # Object references passed to this function
    try:
        data['pii_instances']['ssn'] = "xxx-xx-xxxx"
        data['pii_instances']['date_of_birth'] = 'xxxx/xx/xx'
    except KeyError as e:
        print(f"KeyError: {e}")

# Main
def main():
    # Get the data
    my_results = pull_data(url)
    # Check the outcome
    if my_results:
        # Scrub the data
        scrubba(my_results)
        # Print the keys
        pprint(my_results.keys())
        # Print the scrubbed version
        pprint(my_results)
    else:
        # Something went wrong
        print("Exiting Program")
        exit()

if __name__ == "__main__":
    main()
