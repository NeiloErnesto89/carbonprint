from django.shortcuts import render
import requests
import datetime
import os

# emissions
import json

# request is param we pass into the endpoint
def index(request):
    # API_KEY = SECRET_KEY = str(os.getenv('SECRET_KEY'))
    API_KEY = str(os.environ.get('SECRET_KEY'))
    # API = open(".env", "r").read()
    print(API_KEY)
    # define url endpoint with {} as placeholders for city name and api key queries
    current_weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}" # 2 params to format
    # define url endpoint for coordinates
    # forecast_url = "http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    # forecast_url = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    
   
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}"
   
    # next we check if it's a post request or a get request
    # if post request - we need to get some data
    if request.method == 'POST':
        city1 = request.POST['city1'] # required
        city2 = request.POST.get('city2', None) # None as it's optional
        # use function to get info in endpoint + we will fetch the weather data
        
        # returns just weather data to compare
        weather1 = fetch_weather(city1, API_KEY, current_weather_url)
        if city2:
            weather2 = fetch_weather(city2, API_KEY, current_weather_url)
        else:
            weather2 = None
            
        context = {
            'weather_data1': weather1,
            'weather_data2': weather2,
        }
        
        # UNCOMMENT IF WE WANT TO USE FORECAST TEST NOW API RESPONSE IS WORKING
        # weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)
        # if city2:
        #     weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_url)
        # else:
        #     weather_data2, daily_forecasts2 = None, None # exists but no data (optional)
        
        # # now we pass the data to the template via context dict
        # context = { 
        #     'weather_data1': weather_data1,
        #     'daily_forecasts1': daily_forecasts1,   
        #     'weather_data2': weather_data2,
        #     'daily_forecasts2': daily_forecasts2, 
        # }
        return render(request, 'weather/weather.html', context) # pass context to template
    else: # we assume it's a get request

        return render(request, 'weather/weather.html')

# CURRENTLY NOT INVOKED AS WE ARE NOT USING THE FORECAST DUE TO API LIMITATIONS - MUST PAY FOR IT
# outsource functionality of weather api request to a function - not an endpoint
def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    # send a get request expecting response with certain fields + format in 
    # we use to render the template
    response= requests.get(current_weather_url.format(city, api_key)).json() # get as json object to treat as a dict in python
    # now extract (get) fields from json object - cord lat and lon
    lat, lon = response['coord']['lat'], response['coord']['lon']
    # with the 2 values above we can send another request to get the forecast
    # forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
    
    # now we take the json object and format so it can be passed into the template
    # dictionary context/object we can pass to render on the html
    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2), # round to 2 decimal places, also subtract as it's in kelvin
        # 'country': response['sys']['country'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    
    daily_forecasts = [] 
    
    # for daily_data in forecast_response['daily'][:5]: # 5 days of forecast, daily kv pair
    #     # append to list dictionaries with forecast info
    #     daily_forecasts.append({ 
            
    #         'day' : datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'), # convert unix timestamp to day of the week
    #         'min_temp' : round(daily_data['temp']['min'] - 273.15, 2), # convert to celsius
    #         'max_temp' : round(daily_data['temp']['max'] - 273.15, 2), # convert to celsius 
    #         'description' : daily_data['weather'][0]['description'],
    #         'icon' : daily_data['weather'][0]['icon'],
            
    #         })
        
    # test loop
    for daily_data in daily_forecasts[4]:
        daily_forecasts.append({ 
            'dt_txt' : daily_data['dt_txt'],
            'min_temp' : round(daily_data['temp']['min'] - 273.15, 2), # convert to celsius
            'max_temp' : round(daily_data['temp']['max'] - 273.15, 2), # convert to celsius 
            'description' : daily_data['weather'][0]['description'],
            'icon' : daily_data['weather'][0]['icon'],
         })
        # print(data)
    # result is to retiurn 2 objects - weather_data and daily_forecasts
    return weather_data, daily_forecasts


def fetch_weather(city, api_key, current_weather_url):

    response= requests.get(current_weather_url.format(city, api_key)).json() # get as json object to treat as a dict in python

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2), # round to 2 decimal places, also subtract as it's in kelvin
        # 'country': response['sys']['country'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    
    return weather_data


def emissions(request):
     
    if request.method == 'POST':
        region = request.POST['region'] # required
        passengers = request.POST.get('passengers', None)
        distance = request.POST.get('distance', None)

        emissions_data1 = emissions_search(region, passengers, distance)
        
        context = {
                'emissions1': emissions_data1,
            }
        
        return render(request, 'weather/emissions.html', context)
    
    else:
        
        return render(request, 'weather/emissions.html')

# this function will be called by the emissions view
# it will take the user input and make a request to the api
# returns a json object based on input parms
def emissions_search(region, passengers, distance):
    
    MY_API_KEY = str(os.environ.get('API_KEY'))
    
    activity_id = "passenger_train-route_type_na-fuel_source_electricity"
    # regional = region
    parameters =  {
        "passengers": int(passengers),
        "distance": int(distance),
        "distance_unit": "km"
        }

    json_body = {
        "emission_factor": {
            "id": activity_id,
            "region": region,
            # More filters are possible here. See the full documentation for more options
        },
        # Specify how much energy we're estimating for
        "parameters": parameters
    }

    # You must always specify your AUTH token in the "Authorization" header like this.
    authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

    # We send a POST request to the estimate endpoint with a json body and the correct authorization headers
    emission_response = requests.post("https://beta3.api.climatiq.io/estimate", json=json_body, headers=authorization_headers)
    
    reemission_response = emission_response.json() # get as json object to treat as a dict in python {'key' : 'value'}
    # print(reemission_response['co2e'])
    # print(reemission_response['emission_factor']['name'])
    
    emiss_data = {
        'c02': reemission_response['co2e'],
        'emiss_factor': reemission_response['emission_factor']['name'], 
    }
    print(emiss_data['c02'])
    
    return emiss_data