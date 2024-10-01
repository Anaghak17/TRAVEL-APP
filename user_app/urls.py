from django.urls import path
from .import views
urlpatterns = [
      path('index1/',views.index1,name="index1"),
      path('cart/',views.cart,name="cart"),
      path('shop/',views.shop,name="shop"),
      path('shop1/',views.shop1,name="shop1"),

]