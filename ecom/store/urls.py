
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('collections/', views.collections, name='collections'),
    path('collections/<slug:slug>', views.collections, name='collections'),
 
]
