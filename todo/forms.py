from django import forms
from .models import Todo, Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body')