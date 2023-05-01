from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# view is 'request-handler' function -> takes a request a returns a response

def say_hello(request):
    # return render(request, 'home.html')
    # return instance of HttpResponse class
    return HttpResponse("Hello, Django!")    


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

