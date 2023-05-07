from django.contrib import admin

from . import models # import Notes model from models.py/ '. ' -> current directory

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    # fields we want to display in admin panel
    list_display = ('title', 'content', 'created_at')
    #pass # we don't want any further configuration 

# register that this model should be visible in admin panel (attahced to admin panel)

admin.site.register(models.Notes, NotesAdmin) # register Notes model with NotesAdmin class