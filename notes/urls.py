from django.urls import path

from . import views # import notes/views.py

# same pattern as url routing 
urlpatterns = [
    path("notes/", views.notes_list),
    path("notes/<int:pk>", views.notes_detail), # we want to pass in the primary key of the note we want to view e.g. notes/1
]