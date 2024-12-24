import random
from graphql_fetch import GraphQL_Fetch
from rest_post import Rest_Post
from save_csv import Csv_Save

def main():
    # Initialize the classes with their URLs and filenames
    graphql = GraphQL_Fetch(url="https://countries.trevorblades.com/")
    rest_api = Rest_Post(url="https://jsonplaceholder.typicode.com/posts")
    save_csv = Csv_Save(filename="countries.csv")

    # storing the fetched country 
    countries = graphql.fetch_countries()
    if not countries:
        print("No countries fetched. Exiting.")
        return

    # used random() just for showing, every time before posting the the url is fetching and selecting a random country.
    # it can be implemented by desire selection nedd.
    country = random.choice(countries)

    # Post country details
    rest_api.post_country_details(country)

    # Save country data to CSV
    save_csv.save_to_csv(countries)

if __name__ == "__main__":
    main()
