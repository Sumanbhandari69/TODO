from django.urls import path
from app.views import home, login_view, signup_view

urlpatterns = [
    path("", home, name='home'),
    path("login/", login_view, name='login'),
    path("signup/", signup_view),
]
