from django.urls import path

from . import views # import notes/views.py

# same pattern as url routing 
urlpatterns = [
    path("notes/", views.notes_list, name="notes_list"), # name can be used to refer to this url in templates via <a href="{% url 'notes_list' %}">Notes</a>
    path("notes/<int:pk>", views.notes_detail, name="notes_detail"), # we want to pass in the primary key of the note we want to view e.g. notes/1
    path("notes/create/", views.notes_create, name="notes_create"),
    path("notes/<int:pk>/delete/", views.delete_note, name="delete_note")
    # path("notes/create", views.NotesCreateView.as_view(), name="notes_create"), # create note with class-base views to test
]