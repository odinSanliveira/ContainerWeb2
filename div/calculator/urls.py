
from django.urls import path
from . import views

urlpatterns=[
    path('div/', views.division.as_view(), name='division'),
]