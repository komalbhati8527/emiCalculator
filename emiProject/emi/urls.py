from django.urls import path
from .views import *
urlpatterns = [
    path('', emicalculator),
    path('emiResult', emiResult)
]