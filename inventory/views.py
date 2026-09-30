from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'], url_path='low_stock')
    def low_stock(self, request):
        """Return all products where quantity <= low_stock_threshold."""
        qs = [p for p in self.get_queryset() if p.is_low_stock]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class DashboardView(APIView):
    def get(self, request):
        total_products = Product.objects.count()
        total_categories = Category.objects.count()

        low_stock_products = [p for p in Product.objects.all() if p.is_low_stock]
        low_stock_count = len(low_stock_products)
        low_stock_items = [
            {'name': p.name, 'quantity': p.quantity}
            for p in low_stock_products
        ]

        return Response({
            'total_products': total_products,
            'total_categories': total_categories,
            'low_stock_count': low_stock_count,
            'low_stock_items': low_stock_items,
        })
