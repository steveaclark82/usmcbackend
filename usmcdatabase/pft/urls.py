from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.get_Three_Mile),
    path('<int:id>/', views.get_Crunches),
    path('<int:id>/', views.get_Plank),
    path('<int:id>/', views.get_Row),
    path('<int:id>/', views.get_Pullups),
    path('<int:id>/', views.get_Pushups),
 
]
