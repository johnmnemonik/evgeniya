from django.shortcuts import render

from ts.filters import ProductFilter, CategoryFilter
from ts.models import Product, Category, Enterprises



def product_view(request):
	product = Product.objects.all()
	filter = ProductFilter(request.GET, queryset=product)
	return render(request, "ts/product_filter.html", {'filter': filter})



def category_view(request):
	enterprises = request.GET.get('name')
	product = Product.objects.filter(category=enterprises)
	filter = CategoryFilter(queryset=product)
	return render(request, "ts/category_filter.html", {'filter': filter})
