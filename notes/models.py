from django.db import models

class Notes(models.Model):
    #attributes we want in our admin note
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True -> auto set date and time when note is created  
    
    # override __str__ method to return title of note in admin panel
    # def __str__(self):
    #     return self.title 
    
    