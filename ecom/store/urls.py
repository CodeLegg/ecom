
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('product/<int:pk>', views.product, name='product'),
    path('collections/', views.collections, name='collections'),
    path('collections/<slug:slug>/', views.collection_detail, name='collection_detail'),  # Collection detail URL
 
]
