from django.urls import url
from users import views

urlpatterns = [
    url(r'^api/users$', views.user),
]