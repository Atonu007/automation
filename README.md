

## Solution Architecture

In this solution, I wanted to demonstrate my understanding and comfort with Object-Oriented Programming (OOP). To do that, I organized the solution into separate classes, each handling a specific task.

### Class GraphQL_Fetch:
Is responsible for fetching data from the GraphQL API. To show how the data is being fetched, I randomly select a country from the response.
### Class Rest_Post:
Takes the randomly selected country and posts its details to a REST API.
### Class Csv_Save:
Saves the fetched data to a CSV file. I didn’t check for data duplication, as my main goal was to show that the data is being saved every time new data is fetched.

I chose to select the country randomly to show how the data can be fetched and posted, but this can be customized based on the specific needs of the project. Overall, the focus was on demonstrating the OOP approach, and the solution can be adjusted as required.



## Running the Application

To run the application, follow these steps:

1. Clone the repository or download the source code.
2. Create a virtual environment and activate.
(macos) 
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   if windows then 
  ```bash
   python -m venv venv
   venv\Scripts\activate 
   ```
4. Install the required Python packages using pip:
  ```bash
  pip install -r requirements.txt
 
   ```
3. Run the `main.py` file:
   ```bash
   python main.py
   ```
   
