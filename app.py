from flask import Flask, request, jsonify, render_template
from utils import get_traffic_data, get_route_data, get_weather_data, calculate_emissions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html') 

@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    data = request.json
    vehicle_details = data['vehicle_details']
    origin = data['origin']
    destination = data['destination']
    
    traffic_data = get_traffic_data('tomtom_api_key', origin, destination)
    route_data = get_route_data('google_map_api_key', origin, destination)
    weather_data = get_weather_data('api_key', origin)
    
    distance = route_data['routes'][0]['legs'][0]['distance']['value'] / 1000  # Convert to km
    emissions = calculate_emissions(distance, vehicle_details['fuel_efficiency'])
    
    return jsonify({
        'route': route_data,
        'traffic': traffic_data,
        'weather': weather_data,
        'emissions': emissions
    })

if __name__ == '__main__':
    app.run(debug=True)

  
