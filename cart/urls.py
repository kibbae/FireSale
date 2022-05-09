from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart"),
    path('shipping', views.shipping, name="shipping")
]