from django.urls import path
from .views import index
app_name = 'simple'

urlpatterns = [
    path('', index, name='home-page'),
]


