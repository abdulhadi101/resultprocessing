from django.urls import path
from .views import (userLogin, userRegistration)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('register/', userRegistration, name='register'),
    path ('login/', userLogin, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),

]