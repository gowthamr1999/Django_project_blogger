from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index,name="index"),
    path('', views.login,name="login"),
    path('post/<str:pk>', views.post,name="post"),
    path('logout', views.logout,name="logout"),
    path('register', views.register,name="register"),

]
