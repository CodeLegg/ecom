from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("wholesale/", views.wholesale, name="wholesale"),
    path("cbd-section/", views.cbd_section, name="cbd_section"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("product/<slug:slug>", views.product, name="product"),
    re_path(r"^product/(?P<slug>[\w-]+)/.*$", views.product, name="product_extra"),
    # Existing CBD collection URLs
    path("cbd-collections/", views.cbd_collections, name="cbd_collections"),
    path(
        "cbd-collections/<slug:slug>/",
        views.cbd_collections_product_list,
        name="cbd_collections_product_list",
    ),
    re_path(
        r"^cbd-collections/(?P<slug>[\w-]+)/.*$",
        views.cbd_collections_product_list,
        name="cbd_collections_extra",
    ),
    # New Sticker collection URLs
    path("sticker-collections/", views.sticker_collections, name="sticker_collections"),
    path(
        "sticker-collections/<slug:slug>/",
        views.sticker_collections_product_list,
        name="sticker_collections_product_list",
    ),
    re_path(
        r"^sticker-collections/(?P<slug>[\w-]+)/.*$",
        views.sticker_collections_product_list,
        name="sticker_collections_extra",
    ),
    path(
        "pre-made-sticker-shop/<slug:slug>/",
        views.sticker_sub_collections_list,
        name="sticker_sub_collections_list",
    ),
    re_path(
        r"^pre-made-sticker-shop/(?P<slug>[\w-]+)/.*$",
        views.sticker_sub_collections_list,
        name="sticker_sub_collections_extra",
    ),
    path(
        "pre-made-sticker-shop/<slug:slug>/",
        views.sticker_sub_collections_product_list,
        name="sticker_sub_collections_product_list",
    ),
    re_path(
        r"^pre-made-sticker-shop/(?P<slug>[\w-]+)/.*$",
        views.sticker_sub_collections_product_list,
        name="sticker_sub_collections_extra",
    ),
    path("confirm-age/", views.confirm_age, name="confirm_age"),
]
