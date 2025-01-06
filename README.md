#Dynamic Route Optimization and Emission Reduction System

Introduction

This project is developed to address a critical challenge in logistics and transportation—optimizing vehicle routes to ensure timely deliveries while minimizing environmental impact. The system leverages real-time traffic, weather, and vehicle data to recommend the most efficient routes and estimate vehicle emissions for each route to help reduce the company's carbon footprint.

Objectives

Develop a Python-based dynamic routing system using real-time data from various applicable APIs.

Optimize vehicle routes considering traffic, weather, and vehicle-specific details.

Estimate and minimize vehicle emissions for each route.

Ensure the system is user-friendly and accessible.

Features
Real-time traffic data integration using TomTom API.

Route generation using Google Maps and OSRM APIs.

Meteorological data integration using AQICN API.

Emission estimation for each route to reduce carbon footprint.

User-friendly interface for inputting vehicle details and destinations.

Requirements
Python 3.8+

Flask

Requests

TomTom API Key

Google Maps API Key

AQICN API Key

OSRM Server

Installation
Clone the repository:

bash
git clone https://github.com/soumyaatanna/Dynamic-route-Optimization.git
cd route-optimization
Create a virtual environment and activate it:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
pip install -r requirements.txt
Set up your API keys: Create a .env file in the root directory and add your API keys:

plaintext
TOMTOM_API_KEY=your_tomtom_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
AQICN_API_KEY=your_aqicn_api_key
Usage
Run the Flask application:

bash
flask run
Open your web browser and navigate to http://127.0.0.1:5000.

Enter the vehicle details and destination information in the provided form.

The system will calculate the optimal route, considering real-time traffic and weather data, and estimate the emissions for the chosen route.

APIs Used
TomTom API: For real-time traffic data.

Google Maps API: For route generation.

AQICN API: For meteorological data.

OSRM: For route generation and optimization.
Contributors
This project was developed by the following team members:

Soumya Tanna

Veera Varshini Vakada

Prapul Krishna Shaik

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

I hope this helps! If you need any more adjustments or have further questions, feel free to ask. 😊
