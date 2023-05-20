from django.contrib import admin
from .models import Profile # import Profile model to via on admin page

admin.site.register(Profile) # register Profile model on admin page
