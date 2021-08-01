from django.urls import path
from .views import productPage, productDetail, CartView, Json_Response

app_name = "ProductPage"

urlpatterns = [
    path('', productPage, name="product_page"),
    path('detail/', productDetail, name="product_detail"),
    path('cart/', CartView, name="shopping_cart"),
    path('json/', Json_Response),
]

    