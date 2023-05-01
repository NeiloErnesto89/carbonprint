# map urls to view functions        
from django.urls import path # import path function
from . import views # import views module from current directory

#special var -> array of urlpattern objects
# views we dont pass function, give just a reference 
# URLCOnf module -> URL Configuration and we want to import this into the main url configuration
urlpatterns = [ path('hello/', views.say_hello), 
               path('temp/', views.template_test),] # path function takes 3 args: route, view, name 
               
  