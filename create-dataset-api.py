import csv
import requests

# Set the API endpoint and token
api_endpoint = "https://api.waqi.info/feed/here/"
api_token = "3f22aa832ccc530e82d0b9dd8eacd43c70016bee"
city = 'beijing'

# Send a GET request to the API endpoint
response = requests.get(api_endpoint, params={"token": api_token, "city": city})

# Convert the API response to a dictionary
data = response.json()['data']['forecast']

# Extract the daily data from the API response
daily_data = data["daily"]
# List of days
days = [d["day"] for d in daily_data["o3"]]

# List of columns to be included in the csv
columns = ["day", "o3_avg", "o3_max", "o3_min", "pm10_avg", "pm10_max", "pm10_min",'pm25_max', 'pm25_avg', 'pm25_min']

# Create the csv file and write the header
with open("data.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    
    # Iterate through the days and write the data for each day
    for day in days:
        row = {"day": day}
        for key, value in daily_data.items():
            for d in value:
                if d["day"] == day:
                    row[f"{key}_avg"] = d["avg"]
                    row[f"{key}_max"] = d["max"]
                    row[f"{key}_min"] = d["min"]
        writer.writerow(row)
