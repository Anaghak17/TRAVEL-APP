from django.urls import path
from .import views
urlpatterns = [
      path('index1/',views.index1,name="index1"),
      path('cart/',views.cart,name="cart"),

]