from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [path('', views.index,name='index'),path('checkout',views.checkout,name='checkout'),path('signup',views.signup,name='signup'),path('webcam', views.webcam,name='webcam')]
