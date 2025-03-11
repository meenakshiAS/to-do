from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        """This is Task Form"""

        model = Task
        fields = ["title", "description", "due_date", "completed"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
