from django.shortcuts import render
from .forms import ListItemsForm
from .models import Items


def index(request):
    items = ListItemsForm(Items.objects.all()).data
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
