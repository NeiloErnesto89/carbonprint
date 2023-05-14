from django.contrib.auth.forms import UserCreationForm # django register form for users
from django.contrib.auth.models import User # django user model
from django import forms # django forms

# create an updated user registeration form that incorporates first, last name, email
# via the User object in Django

# RegisterUserForm is child class of UserCreationForm - inherits all the fields from UserCreationForm
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField() # add email field to form
    first_name = forms.CharField(max_length=30) # add first name field to form
    second_name = forms.CharField(max_length=30) # add second name field to form
    
    # Meta class to provide info about the form - Django looks for this class
    # here we define the model we want to interact with (User model)
    class Meta:
        model = User # model we want to interact with
        # now we define all the fields we want to display in the form
        fields = ('username', 'first_name', 'second_name', 'email', 'password1', 'password2') # tuple of fields we want to display in the form  
        
    
    
     