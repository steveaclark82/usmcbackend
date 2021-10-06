from django.conf.urls import url 
from . import views


urlpatterns = [
    url('maneuver_fire/', views.Maneuver_Fire),
    url('movement_contact/', views.Movement_Contact),
    url('ammo_lift/', views.Ammo_Lift),
]
