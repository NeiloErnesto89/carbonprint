from django.urls import path

from . import views # import members/views.py

# same pattern as url routing 
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'), # reference name in nav bar
    path('register_user', views.register_user, name='register'), 
    path('profile', views.profile, name='profile'),
    path('/<int:pk>/delete_user', views.delete_user, name='delete_user'), # delete user
]