"""
URL configuration for carbonsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include # add url

# from home.views import index

urlpatterns = [
    path('', include('home.urls')), # renders url directly (not need for '/home/)
    path('admin/', admin.site.urls),
    # path(r'^$', index, name='index'), # rendering base page
    # path('home/', include('home.urls')), # any urls that begin with 'home' should be routed to our home app
    path('__debug__/', include('debug_toolbar.urls')), 
]
