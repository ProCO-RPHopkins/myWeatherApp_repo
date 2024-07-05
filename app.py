''' jsonify is built into the flask package and converts python dictionary
to JSON (JavaScript Object Notation) responses (i.e., strings) '''
from flask import Flask, request, jsonify
# had to install the requests library to make the API call
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error':'city is required'}), 400
    
    # I could not get the commented out url and key to work, so I used another url and key and it worked
    # api_key = 'ca4d61c6ac7a4f45901204402240307'
    # base_url = 'http://weather.com/v1/current.json'
    api_key = 'f64fb8bed0a2d10ac4e3d0139af0b45f'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units':'imperial' # imperial for Fahrenheit, metric for Celsius
    }

    # make the request
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve weather data'}), 500
    
    # get the data from the response
    data = response.json()
    weather_info = {
    'city': data['name'],
    'temperature': data['main']['temp'],
    'weather_condition': data['weather'][0]['description'],
    'humidity': data['main']['humidity'],
    'wind_speed': data['wind']['speed']
    }  

    return jsonify(weather_info), 200


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
