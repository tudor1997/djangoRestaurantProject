from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('about-us', views.about, name='about'),
]