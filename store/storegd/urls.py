from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('login/', views.login.as_view(), name="login"),
    path('log/', views.loginuser.as_view(), name="log"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('allpro/', views.allproduct, name="allpro"),
    path('viewpro/', views.viewpro, name="viewpro"),

]