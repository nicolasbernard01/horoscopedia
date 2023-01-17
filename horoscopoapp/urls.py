from django.urls import path
from .views import *


urlpatterns = [
    
    path('', horoscopo , name='index'),
    
]