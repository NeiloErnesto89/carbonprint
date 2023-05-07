from django.shortcuts import render, redirect, get_object_or_404, reverse # redirect to redirect to another url
from django.http import Http404 # return correct error msg

# class base views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required # decorator to restrict access to view

from .models import Notes
from .forms import NotesForm    


# we want all the notes info (objects) coming from the database to be avaialble to the template
def notes_list(request):
    all_notes = Notes.objects.all() # get all notes from db
    return render(request, 'notes/notes_list.html', {'notes': all_notes}) # return request, template, context

# test to display admin note content in template - extra arg 'pk' for primary key to id note object
def notes_detail(request, pk):
    # wrap query in try except block to catch error if note doesn't exist
    try:
        current_note = Notes.objects.get(pk=pk) # get note object from db, supply pk to get specific note
    except Notes.DoesNotExist: # object doesn't exist
        raise Http404("Note does not exist, please try another") 
    return render(request, 'notes/notes_detail.html', {'note': current_note}) # return request, template, context


# class NotesCreateView(CreateView):
#     model = Notes # model we want to create
#     template_name = 'notes/create_note.html' # template we want to render
#     fields = ['title', 'content'] # fields we want to display in form
#     success_url = 'internal/notes' # url we want to redirect to after form submission

# @login_required
def notes_create(request, pk=None):
    post = get_object_or_404(Notes, pk=pk) if pk else None
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False) # creates object but commit-> false to prevent saving to db
            note.save()
            return redirect(notes_detail, pk=note.pk) # invokes method and we pass primary key of note we want to view         
    else:
        form = NotesForm(instance=post)
        return render(request, 'notes/notes_form.html', {'form': form})
    # return render(request, 'notes/create_note.html')
    
