from django.urls import path

from . import views # import members/views.py

# same pattern as url routing 
urlpatterns = [
    path('login_user', views.login_user, name='login'),
]