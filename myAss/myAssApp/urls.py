from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('registerroute/add/',views.add,name='add'),
    path('login/',views.login,name='login'),
    # path('login/',LoginView.as_view(),name = 'login'),
    path('registerroute/',views.registerroute,name='registerroute'),
    path('login/loginInfo/',views.loginInfo,name = 'loginInfo'),
    path('logout/',views.logout_request,name='logout'),
    path('registerroute/add/backTohomePageroute/',views.backTohomePageroute,name='backTohomePageroute')
]