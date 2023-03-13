from django.urls import path
from app.views import *
app_name='somthing'
urlpatterns=[
    path('sample/',sample,name='sample'),
]