from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="products"),
    path('<int:id>', views.get_product_by_id, name="product-details"),
    path('create_product', views.create_product, name="create-product"), # video 9
    path('update_product/<int:id>', views.update_product, name='update-product'),
    path('delete_product/<int:id>', views.delete_product, name='delete-product'),
    path('make_offer/<int:id>', views.get_product_by_id, name="make-offer"),
    path('myoffers', views.myoffers, name="offers"),
   # path('acceptOffer', views.AcceptOffer, name="accept")
]