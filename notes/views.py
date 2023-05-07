from django.shortcuts import render

from .models import Notes

# we want all the notes info (objects) coming from the database to be avaialble to the template
def notes_list(request):
    all_notes = Notes.objects.all() # get all notes from db
    return render(request, 'notes/notes_list.html', {'notes': all_notes}) # return request, template, context

# test to display admin note content in template - extra arg 'pk' for primary key to id note object
def notes_detail(request, pk):
    current_note = Notes.objects.get(pk=pk) # get note object from db, supply pk to get specific note
    return render(request, 'notes/notes_detail.html', {'note': current_note}) # return request, template, context