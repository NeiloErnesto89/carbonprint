from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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