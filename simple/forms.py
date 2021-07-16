from django import forms
from .models import Items


class ListItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        exclude = ("updated",)
        