from django.shortcuts import render
from django.http import HttpResponse 
import requests 
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required # decorator to restrict access to view

# Create your views here.
# view is 'request-handler' function -> takes a request a returns a response

def index(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home.html', {'today': datetime.today()}) # return request, template

@login_required(login_url='/admin') # decorator to restrict access to view and redirect to admin login page  
def restricted(request):
    return render(request, 'restricted.html', {'today': datetime.today()})
 
def say_hello(request):
    # return render(request, 'home.html')
    # return instance of HttpResponse class
    return HttpResponse("Hello, Django!")  

# function returns geolocation data via users ip address availble to index.html
def geolocation(request):
    user_ip_address = requests.get('https://api.ipify.org?format=json') # returns current user ip address
    ip_data = json.loads(user_ip_address.text)
    # print(json.loads(user_ip_address.text))
    res = requests.get('http://ip-api.com/json/' + ip_data["ip"]) # get request to api via concatenation
    location_data_one = res.text # get text from response
    location_data = json.loads(location_data_one) # loads from json format to python dict
    return render(request, 'index.html', {'data': location_data})


# real world scenario == pull data from db
# def user_name(request, name):
#     return HttpResponse(f"Hello {name}") 

# dummy test for debugging
def calculate():
    x = 1
    y = 2   
    return x + y

# test function using render to render a template
def template_test(request):
    x = calculate()
    
    # 3 parm -> request, template name, context. 
    # Context allows us to pass data to template via map object e.g dict 
    return render(request, 'index.html', {'name': 'Neil'}) # return request, template

