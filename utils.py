import requests
def get_traffic_data(api_key, start_location, end_location):
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={api_key}&point={start_location}&point={end_location}"
    response = requests.get(url)
    print("Traffic Data Response:", response.json())  # Debugging
    return response.json()

def get_route_data(api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)
    print("Route Data Response:", response.json())  # Debugging
    return response.json()

def get_weather_data(api_key, location):
    url = f"https://api.waqi.info/feed/{location}/?token={api_key}"
    response = requests.get(url)
    print("Weather Data Response:", response.json())  # Debugging
    return response.json()
def calculate_emissions(distance_km, fuel_efficiency_mpg):
    distance_miles = distance_km * 0.621371  # Convert kilometers to miles
    gallons_used = distance_miles / fuel_efficiency_mpg
    emissions_per_gallon = 19.6  # CO2 emissions in pounds per gallon of gasoline
    return gallons_used * emissions_per_gallon
