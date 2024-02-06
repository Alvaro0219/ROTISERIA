from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Product, Category

#Filtrado de categorias y productos
class ProductFilter(filters.FilterSet):

    #Filtrado por categoria
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')
    #Filtrado por nombre
    name = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')

    #Funcion para que me devuelva productos tanto por el nombre como por la descripcion
    def filter_by_search(self, queryset, value):
        return queryset.filter(name__icontains=value) | queryset.filter(description__icontains=value)

    class Meta: 
        model = Product
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
        }

#Serializador de productos
class ProductSerializer(serializers.ModelSerializer):
    #Traer el nombre de la categoria para poder mostrarlo en VUE
    category_name = serializers.ReadOnlyField(source='category.name')
    #Traer el tipo de precio por su nombre y obtener la segunda parte del choice
    price_type_description = serializers.ReadOnlyField(source='get_price_type_display')

    class Meta:
        model = Product
        #campos a serializar
        fields = ('id', 'name', 'image', 'description', 'category', 'category_name', 'price', 'price_type', 'price_type_description')
        #fields = '__all__'      Obtengo todos los campos de la tabla 
        filterset_class = ProductFilter

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'