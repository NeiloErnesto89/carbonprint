from django.db import models
from django.contrib.auth.models import User # django user model as we are extending it

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with User model (aka the current, logged in user)
    bio = models.TextField(max_length=300, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
