from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

#Creamos vistas 
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    def get_queryset(self):

        queryset = super().get_queryset()

        #Filtrado por categorias
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        #Fitlrado por nombre de producto o descripcion
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(description__icontains=search)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer

