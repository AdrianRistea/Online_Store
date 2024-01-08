import django_filters
from store.models import Product, Category


class ProductFilters(django_filters.FilterSet):
    list_of_products = [((product.name, product.name.upper())) for product in Product.objects.filter(active=True)]
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name of product')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max price')

    class Meta:
        model = Product
        fields = ['name', 'min_price', 'max_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the name of product'})
        self.filters['min_price'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Min price'})
        self.filters['max_price'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Max price'})




