import requests
import time

class GraphQL_Fetch:
    # constructor
    def __init__(self, url):
        self.url = url  #store the url passed in the main fle
        self.retries = 3  #set the rety number if failed to fetch

    def fetch_countries(self):
        # query for fetching the data from graphql api.
        query = """
        query {
          countries {
            name
            capital
            currency
          }
        }
        """
        # loop is used to rety 3 times if firat attempt of fetching data is failed
        for _ in range(self.retries):
            try:
                # POST is used because GraphQL queries are sent in the request body, not as URL parameters.
                response = requests.post(self.url, json={"query": query})
                response.raise_for_status()  # check for error
                data = response.json()  # convert response data from graphql in python dict.
                return data.get("data", {}).get("countries", [])
            except requests.exceptions.RequestException as e:
                print(f"Error fetching countries: {e}") # print the error if any occured.
                #Set a 2-second delay before retrying in case of failure network glitches, temporary server unavailability, or high traffic etc.
                time.sleep(2) 
        return []  #after 3 try if it failed to fetch data then return empty list.
