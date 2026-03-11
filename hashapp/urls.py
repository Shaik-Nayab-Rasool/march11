from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('register/',views.register),
    path('login/',views.login),
    path('update/',views.update),
    path('set_cookie/',views.set_cookie),
    path('logout/',views.log_out),
]
