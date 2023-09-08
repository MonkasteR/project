from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductCreate, \
    ProductUpdate, ProductDelete, subscriptions, ProductsList, ProductDetail

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>/', cache_page(60)(ProductDetail.as_view()), name='product_detail'),
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
