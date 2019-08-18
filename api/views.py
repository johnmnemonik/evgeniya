from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view


from ts.models import Region, Category, NetEnterprises, Product, Enterprises
from api.serializers import (
	RegionSerialiser, CategorySerializer, NetEnterprises, ProductSerializer, EnterprisesSerializer
	)



@api_view(['GET'])
def api_enterprises(request):
	""" список предприятий """
	if request.method == 'GET':
		enterprises = Enterprises.objects.all()
		serializer = EnterprisesSerializer(enterprises, many=True)
		return Response(serializer.data)



@api_view(['GET'])
def api_enterprises_detail(request, pk):
	""" детальная информация по предпреятием """
	if request.method == 'GET':
		enterprises =get_object_or_404(Enterprises, pk=pk)
		serializer = EnterprisesSerializer(enterprises)
		return Response(serializer.data)



@api_view(['GET'])
def api_product_detail(request, pk):
	""" Детальная информация по товару """
	if request.method == 'GET':
		product = get_object_or_404(Product, pk=pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)



@api_view(['GET'])
def api_product_search(request, query):
	""" поиск по названию товара"""
	if request.method == 'GET':
		product = Product.objects.filter(name__istartswith=query)
		serializer = ProductSerializer(product, many=True)
		return Response(serializer.data)



@api_view(['GET'])
def api_enterprises_list(request, pk):
	""" вывод списка предпреятий с учетом района """
	if request.method == 'GET':
		region = get_object_or_404(Region, pk=pk)
		enterprises = Enterprises.objects.filter(region=region)
		serializer = RegionSerialiser(enterprises, many=True)
		return Response(serializer.data)
