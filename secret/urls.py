from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("mod", views.mod, name="mod"),
    path("init", views.init, name="init"),
    path("account", views.account, name="account"),
    path("new", views.new, name="new"),
    path("mortal", views.mortal, name="mortal"),
]
