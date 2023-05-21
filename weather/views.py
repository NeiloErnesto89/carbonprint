from django.shortcuts import render
import requests
import datetime
import os
from django.http import Http404 # for fetch weather test
from django.contrib import messages
from requests.exceptions import HTTPError # checking for bad request - 404

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
        
        # 17/05/2023 -> need to updates this None for other logic gates  
        if weather1 == None:
            messages.error(request, 'This city does not exist in our database. Please try again ---')
            return render(request, 'weather/weather.html')
        
        else:   
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
    # this section is important as it's the first time we render the page
    else: # we assume it's a get request
        messages.error(request, 'This city does not exist in our database. Please try again.')
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

# outsource functionality of weather api request to a function - not an endpoint
def fetch_weather(city, api_key, current_weather_url):

    # response check via - https://realpython.com/python-requests/ e.g. if response.status_code == 200: is same as -> if repsonse_check:
    response_check = requests.get(current_weather_url.format(city, api_key))
    # if response_check.status_code == 404:
    #     # raise Http404("Response was a mess, please try another!!!")
    #     return redirect('emissions')
    if response_check: # if response ok
    
        response= requests.get(current_weather_url.format(city, api_key)).json() # get as json object to treat as a dict in python
        # if not response['message'] == 'city not found':
        weather_data = {
            'city': city,
            'temperature': round(response['main']['temp'] - 273.15, 2), # round to 2 decimal places, also subtract as it's in kelvin
            # 'country': response['sys']['country'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        
        return weather_data
    
    else:
        # if the response isn't successful, we return None
        return None
    
    # else:
    #     no_city = "no city found"
    #     print(no_city)
    #     raise Http404("Response was a mess, please try another!!!")

    # else: # if response not ok
    #     print(response['message'])
    #     no_city = response['message']
    #     return no_city
        # raise Http404("Response was a mess, please try another!!!")
        # return redirect('emissions')

# WORKING VERSION OF THE FUNCTION for emissions
def _emissions(request):
     
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
        'c02': round(reemission_response['co2e'], 2), # python round() function rounds to 2 decimal places
        'c02_unit' : reemission_response['co2e_unit'],
        'emiss_factor': reemission_response['emission_factor']['name'], 
    }
    print(emiss_data['c02'])
    
    return emiss_data

# emissions tester with query and region
# query is powerful as it's free text search
# - A free-text query that will match ids, names, descriptions, etc. of emission factors. This uses fuzzy matching, so your query does not need to be precise.
# via https://www.climatiq.io/docs/api-reference/search

def emissions(request):
     
    if request.method == 'POST':
        region = request.POST['region'] # required
        passengers = request.POST.get('passengers', None)
        distance = request.POST.get('distance', None)
        query = request.POST.get('query', None) # now added to test query search

        # emissions_data1 = emissions_search(region, passengers, distance)
        
        if query:
            emissions_data1 = emissions_search(region, passengers, distance)
            emissions_data2 = emissions_query(query, region)
            # context = {
            #     'emissions1': emissions_data1,
            #     'emissions2': emissions_data2,
            # }
        else:
            emissions_data1 = emissions_search(region, passengers, distance)
            emissions_data2 = None
        
        context = {
                'emissions1': emissions_data1,
                'emissions2': emissions_data2,
            }
        
        return render(request, 'weather/emissions.html', context)
    
    else:
        
        return render(request, 'weather/emissions.html')


# emssions regional queries 21/0/2023

def emissions_query(query, region):
    MY_API_KEY = str(os.environ.get('API_KEY'))
    
    url = "https://beta4.api.climatiq.io/search"
    query = query # assign query arg to a variable
    query_params = {
    # Free text query can be writen under the query string
    "query": query,
    # You can also filter on region, year, source and more
    "region": region,
    # The string below means "major version 1 compatible", which means we stay on major version 1 of the data
    "data_version": "^1",
}
    authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

    search_response = requests.get(url, params=query_params, headers=authorization_headers).json()
    
    # print(search_response.keys()) # find keys in large data set

    # # The most relevant is probably the results - here are the first 
    # print(search_response["results"][0:1])
    # print(type(search_response["results"][0:1])) # list with nested dict
    
    search_response_list = search_response["results"][0:1]

    description = search_response_list[0]['description']

    # Access the CO2 value
    co2_value = search_response_list[0]['constituent_gases']['co2']

    # print(f"Description: {description}")
    # print(f"CO2 value: {co2_value}")
    
    query_data = {
        'c02': search_response_list[0]['constituent_gases']['co2'],
        'description': search_response_list[0]['description'], 
        'category' : search_response_list[0]['category'],
        'source_data' : search_response_list[0]['source_dataset'],
        'unit' : search_response_list[0]['unit']
    }
    
    return query_data


# flight tracker method 

def flight_tracker(request):
    
    flight_class = ['economy', 'unknown', 'business', 'first']
    
    # try except to handle errors
    try:
        if request.method == 'POST':
            travel = request.POST['travel'] # required
            leg_from = request.POST.get('leg_from', None)
            leg_to = request.POST.get('leg_to', None)
            passengers = request.POST.get('passengers', None) 
            travel_class = request.POST.get('travel_class', None)
            # freight flight - involved weight by kg
            # freight = request.POST.get('freight', None)     
            
            flight_tracker_data = flight_tracker_calculation(travel, leg_from, leg_to, passengers, travel_class)
        
            context = {
                'flight_tracker': flight_tracker_data, # access to co2e, co2 unit, activity unit
                'flight_class': flight_class,
            }
            return render(request, 'weather/travel.html', context)
        
        else:
            context = {
                'flight_class': flight_class,
            }
            
            return render(request, 'weather/travel.html', context)
        
    except KeyError as http_err:
        error_message = str(http_err)
        messages.error(request, 'Please enter a valid airport code with the IATA code')
        # print(error_message)
        
        context = {
                'flight_class': flight_class,
                'error_message': error_message,
            }
        
        return render(request, 'weather/travel.html', context)
        
    # else:
    #     context = {
    #         'flight_class': flight_class,
    #     }
        
    #     return render(request, 'weather/travel.html', context)
    
def flight_tracker_calculation(travel, leg_from, leg_to, passengers, travel_class):
    
        MY_API_KEY = str(os.environ.get('API_KEY'))
        
        if travel == 'flights':
            url = "https://beta4.api.climatiq.io/travel/flights"
            
        else:
            url = "https://beta4.api.climatiq.io/travel/flights"
            
        parameters = {
        "legs": [
            {
                "from": leg_from,
                "to": leg_to,
                "passengers": int(passengers),
                "class": travel_class
            },
            # {
            #     "from": "AMS",
            #     "to": "JFK",
            #     "passengers": 2,
            #     "class": "economy"
            # }
        ]
        }
        
        authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

        response = requests.post("https://beta4.api.climatiq.io/travel/flights", json=parameters, headers=authorization_headers)

        # pprint.pprint(response.json())

        repo_json = response.json()
        # print(repo_json['co2e']) # entire journey
        # print(repo_json['legs'][0]['activity_data']['activity_unit'])
        
        flight_data = {
            'c02': round(repo_json['co2e'],2), # round down co2e to 2 decimal places
            'unit': repo_json['co2e_unit'],
            'activity_unit': repo_json['legs'][0]['activity_data']['activity_unit'],
            'activity_value': round(repo_json['legs'][0]['activity_data']['activity_value'], 2),
        }
        
        return flight_data