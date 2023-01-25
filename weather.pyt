import requests
import json

# Define the API endpoint and API key
endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "9226ed0b9dd0791ba0039533eae0c888"

# Define the city you want to get the weather for
city = "New York"

# Make the API request
response = requests.get(endpoint, params={'q': city, 'appid': api_key})

# Parse the JSON data
data = json.loads(response.text)

# Extract the temperature and weather description
temperature = data['main']['temp']
description = data['weather'][0]['description']

# Print the temperature and weather description
print("The temperature in {} is {:.2f} degrees Celsius.".format(city, temperature - 273.15))
print("The weather is currently: {}".format(description))
