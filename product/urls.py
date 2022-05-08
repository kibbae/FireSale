from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="product"),
    path('<int:id>', views.get_product_by_id, name="product-details"),
    path('create_product', views.create_product, name="create-product"), # video 9
    path('delete_item/<int:id>', views.delete_product, name='delete-item'),
    # path('update_item/<int:id>', views.update_product, name='update-item'),
    # path('sort_item', views.sort_product, name="sort-item"),
    # path('make_offer/<int:id>', views.make_offer, name="make-offer")

]