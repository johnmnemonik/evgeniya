import django_filters
from django_filters import ModelChoiceFilter, ChoiceFilter, RangeFilter

from ts.models import Product, Category, Enterprises, NetEnterprises


class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = Product
		fields = {'price': ['lt', 'gt']}


class CategoryFilter(django_filters.FilterSet):
	name = ModelChoiceFilter(queryset=Category.objects.all())

	class Meta:
		model = Category
		fields = {
			'name': ['exact'],
		}

