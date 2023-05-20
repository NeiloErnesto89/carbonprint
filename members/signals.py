# add signals here to be able to use them

from django.db.models.signals import post_save # signal fired after object is saved, we do this when user is created
from django.contrib.auth.models import User # django user model acts as sender as it sends signal
# we need now a reciever, a function that gets (or recieves) the signal and performs some task
from django.dispatch import receiver # reciever of the signal
from .models import Profile # import Profile model to be able to create a profile for the user

# now we want to offically create a user profile upon user creation

@receiver(post_save, sender=User) # when a user is saved, send this signal (post_save) and recieve it (reciever)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# now we want to save the profile upon user creation
@receiver(post_save, sender=User) # when a user is saved, send this signal (post_save) and recieve it (reciever)
def save_profile(sender, instance, **kwargs):
    # now we just want to save
    instance.profile.save() # save the profile of the user instance