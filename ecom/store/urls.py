
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('product/<int:pk>', views.product, name='product'),
    # Existing CBD collection URLs
    path('cbd-collections/', views.cbd_collections, name='cbd_collections'),
    path('cbd-collections/<slug:slug>/', views.cbd_collections_product_list, name='cbd_collections_product_list'),

    # New Sticker collection URLs
    path('sticker-collections/', views.sticker_collections, name='sticker_collections'),
    path('sticker-collections/<slug:slug>/', views.sticker_collections_product_list, name='sticker_collections_product_list'),
    path('collections/<slug:slug>/sub-collections/', views.sticker_sub_collections_list, name='sticker_sub_collections_list'),
    path('collections/pre-made-sticker-shop/sub-collections/<slug:slug>/', views.sticker_sub_collections_product_list, name='sticker_sub_collections_product_list'),
    path('sub-collections/<slug:slug>/', views.sticker_sub_collections_product_list, name='sticker_sub_collections_product_list'),

]
