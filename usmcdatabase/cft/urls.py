from django.urls import path
from . import views
urlpatterns = [
    path('/', views.get_cft_score),
    path('maneuver_fire/', views.get_cft_muf),
    path('ammo_lift/', views.get_cft_ammo),
    path('movement_contact/', views.get_cft_mtc),
]
