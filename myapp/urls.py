from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('home/', views.HomePage, name='HomePage'),
    path('about/', views.AboutPage, name='AboutPage'),
    path('contact/', views.ContactPage, name='ContactPage'),
    path('parcel/', views.ParcelPage, name='ParcelPage'),
    path('loading/', views.LoadingPage, name='LoadingPage'),
    path('form', views.myform, name='myform'),
    path('process', views.myformprocess, name='myformprocess'),

]