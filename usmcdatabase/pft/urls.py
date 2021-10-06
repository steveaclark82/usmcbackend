from django.conf.urls import url 
from . import views


urlpatterns = [
    url('three_mile/', views.Three_Mile),
    url('crunches/', views.Crunches),
    url('plank/', views.Plank),
    url('row/', views.Row),
    url('pullups/', views.Pullups),
    url('pushups/', views.Pushups),
]
