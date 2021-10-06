from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^api/cft$', views.Maneuver_Fire),
    url(r'^api/cft$', views.Movement_Contact),
    url(r'^api/cft$', views.Ammo_Lift),
]
