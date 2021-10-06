from django.urls import url
from nco import views

urlpatterns = [
    url(r'^api/nco$', views.nco),
]