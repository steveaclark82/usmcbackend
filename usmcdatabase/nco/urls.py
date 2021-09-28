from django.urls import path
from nco import views

urlpatterns = [
    path('all', views.get_all_nco),
    path('<int:id>/', views.get_nco),
]