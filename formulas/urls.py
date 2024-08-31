from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('links', views.links, name='links'),
    path('square/', views.square_calculate, name='square'),
    path('triangle/', views.triangle_calculate, name='triangle'),
    path('circle/', views.calculate_circle, name='circle'),
]
