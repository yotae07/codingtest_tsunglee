from django.urls               import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views                    import(
    ProductView,
    OrderView
)

search_register = ProductView.as_view({
    'get': 'register_search'
})

search_name = ProductView.as_view({
    'get': 'name_search'
})

search_order = OrderView.as_view({
    'get': 'order_search'
})

urlpatterns = format_suffix_patterns([
    path('/search-name', search_register),
    path('/search/<str:name>', search_name),
    path('/search-order', search_order),
])
