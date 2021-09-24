from django.urls import path
from . import views
urlpatterns = [
    path('/', views.get_pft_score),
    path('/', views.get_age_range),
    path('three_mile/', views.get_pft_run),
    path('row/', views.get_pft_row),
    path('pullups/', views.get_pft_pullups),
    path('pushups/', views.get_pft_pushups),
    path('crunches/', views.get_pft_crunches),
    path('plank/', views.get_pft_plank),
    
    
]
