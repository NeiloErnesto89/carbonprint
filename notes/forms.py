from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        # ordering = ['-id']
        fields = ('title', 'content')