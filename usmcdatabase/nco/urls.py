from django.urls import path
from nco import views

urlpatterns = [
    path('nco/', views.nco),
]