from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("update_todo/<int:pk>/", views.update_todo, name="update_todo"),
    path("delete_todo/<int:pk>/", views.delete_todo, name="delete_todo"),
]
