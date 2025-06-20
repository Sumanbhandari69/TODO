from django.urls import path
from app.views import home, login_view, signup_view, add_todo, signout, delete_todo, change_status

urlpatterns = [
    path("", home, name='home'),
    path("login/", login_view, name='login'),
    path("signup/", signup_view),
    path("add-todo/", add_todo),
    path("logout/", signout),
    path("delete-todo/<int:id>", delete_todo),
    path("change-status/<int:id>/<str:status>", change_status),
]
