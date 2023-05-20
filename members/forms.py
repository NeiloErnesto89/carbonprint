from django.contrib.auth.forms import UserCreationForm # django register form for users
from django.contrib.auth.models import User # django user model
from django import forms # django forms
from .models import Profile # import Profile model to be able to create a profile for the user  

# create an updated user registeration form that incorporates first, last name, email
# via the User object in Django - we are udpdating the pre built UserCreationForm in the Django framework
# using polymorphism - we are creating a child class of UserCreationForm and updating it

# RegisterUserForm is child class of UserCreationForm - inherits all the fields from UserCreationForm
class RegisterUserForm(UserCreationForm):
    # widget is a html element that we can add to the form and we add form-control class to it
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})) # add email field to form
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'})) # add first name field to form
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'})) # add second name field to form
    
    # Meta class to provide info about the form - Django looks for this class
    # here we define the model we want to interact with (User model)
    class Meta:
        model = User # model we want to interact with
        # now we define all the fields we want to display in the form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') # tuple of fields we want to display in the form  
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        # now we add placeholders to the form fields
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Second Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
        # # now we add labels to the form fields
        # self.fields['username'].label = False
        # self.fields['first_name'].label = False
        # self.fields['second_name'].label = False
        # self.fields['email'].label = False
        # self.fields['password1'].label = False
        # self.fields['password2'].label = False
        
        # now we add classes to the form fields
        self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['second_name'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
    
# create a user update form that incorporates first, last name, email

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})) # add email field to form
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'})) # add first name field to form
    last_name = forms.CharField(max_length=30) # add second name field to form
    
    # Meta class to provide info about the form - Django looks for this class
    # here we define the model we want to interact with (User model)
    class Meta:
        model = User # model we want to interact with
        # now we define all the fields we want to display in the form
        fields = ('username', 'first_name', 'last_name', 'email') # tuple of fields we want to display in the form 
        
        # error with second name not updating- maybe resolved by cleaning
        # def clean_second_name(self):
        #     second_name = self.cleaned_data['second_name']
        #     # Add any additional validation or cleaning logic for the second_name field if needed
        #     return second_name
        
# now we also want to work with profile model - we want to create a form that allows us to update the profile model
class ProfileUpdateForm(forms.ModelForm):
    # no addtional fields
    # Meta class to provide info about the form - Django looks for this class
    class Meta:
        model = Profile # model we want to interact with
        fields = ('image', 'bio', 'location') # tuple of fields we want to display & update in the form
        
    # updating __init__ constructor to try resolve second name not correctly mapping
    
    # def __init__(self, *args, **kwargs):
    #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)
    #     # Update the instance argument to retrieve the profile associated with the current user
    #     self.instance = self.instance.user.profile