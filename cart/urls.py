from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart"),
    path('payment', views.payment, name="payment"),
    path('shipping', views.shipping, name="shipping"),
    path('orderreview', views.orderreviw, name="orderreview")
]