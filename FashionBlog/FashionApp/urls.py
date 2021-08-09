from django.urls import path 
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct


urlpatterns = [
    path('categories',ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='category'),
    path('products',ListProduct.as_view(), name='products'),
    path('product/<int:pk>/',DetailProduct.as_view(), name='product' )
]