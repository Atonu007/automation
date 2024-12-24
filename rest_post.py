import requests
import time

class Rest_Post:
    # Constructor
    def __init__(self, url):
        self.url = url  # Store the URL passed in the main file
        self.retries = 3  # Set the retry number if failed to post data

    def post_country_details(self, country):
        # Prepare the payload with country details to be posted
        payload = {
            "title": f"Country: {country['name']}", 
            "body": f"Capital: {country['capital']}, Currency: {country['currency']}",  
            "userId": 1  
        }

        # Loop to retry 3 times if the first attempt to post data fails
        for _ in range(self.retries):
            try:
                # Send the POST request with the payload in JSON format
                response = requests.post(self.url, json=payload)
                response.raise_for_status()  # Check for any errors in the response
                print(f"Posted country details: {response.json()}")  # Print the response if successful
                return  # Exit after successfully posting
            except requests.exceptions.RequestException as e:
                print(f"Error posting country details: {e}")  # Print the error message if any error occurs
                #Set a 2-second delay before retrying in case of failure network glitches, temporary server unavailability, or high traffic etc.
                time.sleep(2)   
