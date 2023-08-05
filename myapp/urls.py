from django.urls import path
from .views import *

urlpatterns = [


    path('home/',home),
    path('date/',date1),
    path('index/',index),
    path('vegitable/',vegitable)
]