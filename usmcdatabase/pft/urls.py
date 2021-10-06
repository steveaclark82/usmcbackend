from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^api/pft$', views.Three_Mile),
    url(r'^api/pft$', views.Crunches),
    url(r'^api/pft$', views.Plank),
    url(r'^api/pft$', views.Row),
    url(r'^api/pft$', views.Pullups),
    url(r'^api/pft$', views.Pushups),
 
]
