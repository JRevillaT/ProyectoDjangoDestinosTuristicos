from django.urls import path
from . import views,models

urlpatterns=[
    path('register',views.register,name='register'),
    ]