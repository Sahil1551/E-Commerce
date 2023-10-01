from django.contrib import admin
from django.urls import path
from Clothingstore import views
urlpatterns = [
    path("",views.index,name="Home"),
    path("home",views.index,name="home"),
    path("product/home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("product/about",views.about,name="about"),
    path("shop", views.shop, name="shop"),
    path("product/shop",views.shop,name="shop"),
    path("blog_details",views.blog_details,name="blog_details"),
    path("product/blog_details",views.blog_details,name="blog_details"),
    path("blog", views.blog, name="blog"),
    path("product/blog",views.blog,name="blog"),
    path("contact", views.contacts, name="contact"),
    path("product/contact",views.contacts,name="contact"),
    path("shop_details", views.shop_details, name="shop_details"),
    path("product/shop_details",views.shop_details,name="shop_details"),
    path("shopping_cart", views.shopping_cart, name="shopping_cart"),
    path("product/shopping_cart",views.shopping_cart,name="shopping_cart"),
    path("checkout/<int:id>", views.checkouts, name="checkout"),
    path("product/cart/checkout/<int:id>",views.checkouts,name="checkout"),
    path("main",views.login,name="main"),
    path("product/main",views.login,name="main"),
    path("signup",views.signup,name="signup"),
    path("product/signup",views.signup,name="signup"),
    path("signout",views.signout,name="signout"),
    path("product/signout",views.signout,name="signout"),
    path("product/<int:id>", views.products, name="product"),
    path("product/cart/<int:id>",views.carts,name="cart")
]
