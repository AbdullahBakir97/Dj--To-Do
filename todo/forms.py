from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']
        labels = {
            'title': 'Title',
            'completed': 'Completed'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        error_messages = {
            
            'title': {
                'required': 'Title is required.',
                'min_length': 'Title must be at least 3 characters long.'
            }
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_completed(self):
        completed = self.cleaned_data.get('completed')
        if completed:
            # Add any additional validation here if needed
            pass
        return completed