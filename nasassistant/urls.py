from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("day", views.day, name="day"),
    path("mars", views.mars, name="mars"),
    path("form1", views.form1, name="form1"),
    path("exoplanets", views.exoplanets, name="exoplanets"),
    path("exoplanets_comparison", views.exoplanets_comparison,
         name="exoplanets_comparison"),
]
