from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.get_Movement_Contact),
    path('<int:id>/', views.get_Maneuver_Fire),
    path('<int:id>/', views.get_Ammo_lift),
]
