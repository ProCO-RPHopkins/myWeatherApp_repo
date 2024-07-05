myAPI_WeatherApp - W8D1

-Functionality
   1. App route uses weather function to 'GET' requests from '/weather' endpoint.
   2. City parameter is used to make a GET request from API OpenWeatherMap request using query 
      (e.g., ?city=Miami).
   3. If city request not made, 400 (JSON) status code is returned.
   4. If city request unsuccessful, 500 (JSON) status code is returned.
   5. If city request is successful, 200 (JSON) status code is returned.
   6. In case of 200 status code, response data is converted from JSON to the Python weather_info 
      dictionary (using jsonify method), which includes city, temperature, humidity, weather_condition, and wind_speed.
   7. Retrieved OpenWeatherMap data is displayed on the server: http://127.0.0.1:5000 with endpoint /weather and query parameter.

-Troubleshooting
   1. The GET request would not work with the API Key from https://weather.com
         - A 500 status code was returned
         - I do not know why the city query would not work with the API from weather.com, but I immediately recognized the problem.
   2. I got an API key from https://openweathermap.com and the weather app ran fine.

      
-Testing
   1. Run -- python app.py -- 
   2. Start server http://127.0.0.1:5000
         - A 404 status code was returned, which means page not found because the HTTP is missing the /weather endpoint
         - Error Message: "Not Found
           The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
   3. The /weather endpoint was added to the HTTP: http://127.0.0.1:5000/weather
         - A 400 status code was returned, which means 'bad request' because no city query was added to the /weather endpoint
         - Error Message:  {
                              "error": "city is required"
                           }  
   4. The city query -- ?city=PuppyTown -- was added to the /weather endpoint: http://127.0.0.1:5000/weather?city=PuppyTown
         - A 500 status code was returned, which is a catch all 'internal server error' prompted by a city query that was not found
         - Error Message:  {
                              "error": "Failed to retrieve weather data"
                           }
   5. The city query -- ?city=Miami -- was added to the /weather endpoint: http://127.0.0.1:5000/weather?city=Miami
         - A 200 status code was returned, which means "successful HTTP request"
         - Successful query display:
                           {
                              "city": "Miami",
                              "humidity": 75,
                              "temperature": 86.83,
                              "weather_condition": "broken clouds",
                              "wind_speed": 12.66
                           }

-Terminal Output of HTTP Status Codes
   ![alt text](<Screenshot (224).png>)

