from django.shortcuts import render, redirect, get_object_or_404, reverse # redirect to redirect to another url
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm # django register form for users
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm # import forms.py
from django.contrib.auth.decorators import login_required # decorator to restrict access to certain pages to logged in users only
from django.contrib.auth.models import User # import User model


def login_user(request):
    # if user fills form and submits
    if request.method == "POST":
        # https://docs.djangoproject.com/en/4.2/topics/auth/default/#auth-web-requests
        # here we are using the authenticate() method to verify that the given username 
        # and password match against a user account   
        # username = request.POST["username"]
        # password = request.POST["password"]
        username = request.POST.get('username')
        password = request.POST.get('password')
        # use authenticate() to verify that the given username & password are correct
        user = authenticate(request, username=username, password=password)
        # then if user is not None, the password verified for the user, and the user is active
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home_page') # redirect to home page
        else:
            # pass error message to user (unsuccessful login)
            messages.error(request, 'Invalid username or password') 
            return redirect('login') # redirect to login page
    else:
        return render(request, 'authenticate/login.html', {}) # empty conetxt dict


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home_page') # redirect to home page


# function to register new users

def register_user(request):
    if request.method == "POST":
        # formerly UserCreationForm(request.POST) - now RegisterUserForm(request.POST)
        form = RegisterUserForm(request.POST) # if user fills form and submits - we pass that data to the UserCreationForm
        # now we validate the form
        if form.is_valid():
            form.save() # save the form to the database i.e user
            # username = form.cleaned_data.get('username') # get the username from the form 'cleaned' data
            # password = form.cleaned_data.get('password1') # get the 1st password from the form 'cleaned' data
            username = form.cleaned_data['username'] # get the username from the form 'cleaned' data
            password = form.cleaned_data['password1']
            # now we authenticate the user & sign them in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!!')
            return redirect('home_page') # redirect to home page with success message
        # else:
        #     # if form is invalid, we want to hide the help text
        #     for field in form:
        #         field.help_text = ''
    # else - potential user wants to fill out form so we redirect 
    else: 
        form = RegisterUserForm() # create a new form former UserCreationForm()
    
    # within if-else, we have a form context dict which we need to make available to the template                
    return render(request, 'authenticate/register_user.html', { 'form': form}) # form context dict 

@login_required(login_url='login') # decorator to restrict access to certain pages to logged in users only
def profile(request):
    if request.method == "POST": # post conditional, what is run when we submit the form
    # we populate the fields of forms my passing in the instance of the user   
        user_form = UserUpdateForm(request.POST, instance=request.user) # pass in the instance of the user + post data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # pass in the instance of the user profile + plus data plus files for img
        
        # now we validate the forms so we need  'and'condition  to check both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() # saving both forms
            print('saved')
            # pass success message to user
            messages.success(request, 'Your profile has been updated successfully') 
            return redirect('profile') # redirect to profile page and avoids extra post request (refreshing page)
        
    else:
        user_form = UserUpdateForm(instance=request.user) # pass in the instance of the user
        profile_form = ProfileUpdateForm(instance=request.user.profile) # pass in the instance of the user profile
    # pass into template:
    context = { 
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'authenticate/profile.html', context) # empty conetxt dict


@login_required
def delete_user(request, pk):

    user = get_object_or_404(User, pk=pk)
    # return HttpResponseRedirect

    if request.user.is_authenticated and request.user == user:
        user.delete()
        messages.success(request, 'This User has been deleted')
        return redirect(reverse("login"))

    elif request.user.is_authenticated and request.user.is_superuser:
        user.delete()
        messages.success(request, 'The admin has deleted this user')
        return redirect(reverse("home_page"))

    elif request.user.is_authenticated and request.user.is_superuser and user.pk == 1:
        messages.error(request, 'Admin cannot delete the Admin profile')
        return redirect('profile', user.pk)
    else:
        messages.error(request, 'you are not allowed to deleted this user')
        return redirect('profile', user.pk)