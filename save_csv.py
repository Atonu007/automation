import csv

class Csv_Save:
    def __init__(self, filename):
        self.filename = filename # from main file 

    def save_to_csv(self, countries):
        try:
            # Open the CSV file in append mode to add new data without overwriting existing data
            with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)  # writer object to write to the file
                file_empty = file.tell() == 0  # Check if the file is empty 
                if file_empty:
                    writer.writerow(["Country Name", "Capital", "Currency"])  # Write the header row if the file is empty
                # Loop through the list of countries and write each country's details to the CSV
                for country in countries:
                    writer.writerow([country.get("name"), country.get("capital"), country.get("currency")])
            print(f"Data saved to {self.filename}") 
        except Exception as e:
            print(f"Error saving to CSV: {e}")  # Print error message if an exception occurs
