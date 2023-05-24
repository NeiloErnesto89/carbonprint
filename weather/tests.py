from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse # reverse url lookup
# from unittest.mock import patch, mock # mocking the request - patch as decorator or context manager whereby we can mock an object in the context of a test
import unittest
from unittest import mock
from django.test import Client
import requests
from .views import flight_tracker_calculation, flight_tracker
import os

# import requests_mock
from django.test import RequestFactory

class FlightTrackerTestCase(TestCase):
    
    # unitest for the flight_tracker function
    def test_flight_tracker(self):
        
        # Prepare test data to be mocked
        travel = 'flights'
        leg_from = 'DUB'
        leg_to = 'JFK'
        passengers = '2'
        travel_class = 'economy'

        # Here we are mocking the requests.post method which is just 
        with mock.patch('requests.post') as mock_post:
            
            # now using mock response JSON to imitate the API response and assign it to a variable
            mock_response = { 
                'co2e': 100.0,
                'co2e_unit': 'kg',
                'legs': [
                    {
                        'activity_data': {
                            'activity_unit': 'km',
                            'activity_value': 500.0
                        }
                    }
                ]
            }
            
            # mock response == return value of  mock post method
            mock_post.return_value.json.return_value = mock_response
            
            # Call the flight_tracker_calc function for test
            result = flight_tracker_calculation(travel, leg_from, leg_to, passengers, travel_class)

            # Assert the expected result == actual result
            expected_result = {
                'c02': 100.0, # c02 
                'unit': 'kg',
                'activity_unit': 'km',
                'activity_value': 500.0
            }
            
            # print(result)
            # print(expected_result)
            
            assert result == expected_result
    
#     def setUp(self):
#         self.factory = RequestFactory()
        
    # def test_flight_tracker_calculation(self, travel, leg_from, leg_to, passengers, travel_class):
    #     # Make an actual API call to test the API
    #     MY_API_KEY = str(os.environ.get('API_KEY'))
    #     url = "https://beta4.api.climatiq.io/travel/flights"
    #     parameters = {
    #         "legs": [
    #             {
    #                 "from": leg_from,
    #                 "to": leg_to,
    #                 "passengers": int(passengers),
    #                 "class": travel_class
    #             }
    #         ]
    #     }
    #     authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}
    #     response = requests.post(url, json=parameters, headers=authorization_headers)
    #     data = response.json()
    #     # Process the API response and return the required data
    #     flight_data = {
    #         'co2': data['co2e'],
    #         'unit': data['co2e_unit'],
    #         'activity_unit': data['legs'][0]['activity_data']['activity_unit'],
    #         'activity_value': data['legs'][0]['activity_data']['activity_value']
    #     }
    #     return flight_data




# class FlightTrackerTest(TestCase):

#       def test_get_info_from_website(self):
#         # Mock the API response
#         mock_response = {
#             'co2': 123,
#             'description': ' Description',
#             'category': 'Category',
#             'source_data': 'Mocked Source Data',
#             'unit': 'kg'
#         }
        

#         # Replace the actual API call with a mock
#         with mock.patch('emissions_query', return_value=mock_response):
#             # Call the method that uses the API
#             result = emissions_query()

#             # Perform assertions on the result
#             self.assertEqual(result, 'mocked data')
    
    # def test_flight_tracker(self):
    #     with patch('requests.get') as mocked_get: # mock the request.get method 
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'
            
    #         response = self.client.get(reverse('flight_tracker'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, 'flight_tracker/flight_tracker.html')
    #         self.assertContains(response, 'Success')

# from django.test import TestCase, RequestFactory
# from .views import index

# class IndexTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_index_get_request(self):
#         request = self.factory.get('/weather/')
#         response = index(request)

#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'This city does not exist in our database. Please try again.')

#     def test_index_post_request(self):
#         request = self.factory.post('/weather/', {'city1': 'London'})
#         response = index(request)

#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'weather/weather.html')

# auth test example - https://www.youtube.com/watch?v=FLVB_HruIjk

# class BaseTest(TestCase):
#     def setUp(self):
#         self.register_url = reverse('register') # here we are using the name of the url in the urls.py file
#         self.login_url = reverse('login')
        
#         return super().setUp()

# class TestViews(TestCase):
    
#     def test_get_home_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'weather/weather.html')

# import unittest
# from django.test import Client


# class SimpleTest(unittest.TestCase):
#     def setUp(self):
#         # Every test needs a client.
#         self.client = Client()

#     def test_details(self):
        
#         fake_json = {{'python' : 'rocks'}}
        
#         response = self.client.get("/weather/weather/")

#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)

#         # Check that the rendered context contains 5 customers.
#         self.assertEqual(len(response.context["customers"]), 5)
