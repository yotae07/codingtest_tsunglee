from django.db.models          import Count
from rest_framework.response   import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework            import(
    viewsets,
    status
)

from .models                   import(
    Image,
    Product,
    Order
)
from .serializers              import(
    ImageSerializer,
    ProductSerializer,
    OrderSerializer
)

class DefaultPagination(PageNumberPagination):
    page_size        = 20
    page_query_param = 'page_size'
    max_page_size    = 100

class ProductView(viewset.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False)
    def name_search(self, request, name=None):
        qs = self.queryset.filter(name=name)
        serializer = self.get_serializer(qs, many=True)
        pagination_class = DefaultPagination
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def register_search(self, request):
        qs               = self.queryset.values('created_at').order_by('created_at')
        serializer       = self.get_serializer(qs, many=True)
        pagination_class = DefaultPagination
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderView(viewset.ModelViewSet):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False)
    def order_search(self, request):
        qs               = self.queryset.values('product').anntate(count=Count('product')).order_by('-count')
        serializer       = self.get_serializer(qs, many=True)
        pagination_class = DefaultPagination
        return Response(serializer.data, status=status.HTTP_200_OK)
