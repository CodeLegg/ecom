
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('product/<int:pk>', views.product, name='product'),
 path('cdb_collections/', views.cbd_collections, name='cbd_collections'),
    path('cdb_collections/<slug:slug>/', views.cbd_collections_product_list, name='cbd_collections_product_list'),
]
