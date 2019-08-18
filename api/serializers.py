from rest_framework import serializers
from ts.models import Region, Category, NetEnterprises, Product, Enterprises


class RegionSerialiser(serializers.ModelSerializer):
	""""""
	class Meta:
		model = Region
		fields = ('id', 'name',)



class CategorySerializer(serializers.ModelSerializer):
	""""""
	class Meta:
		model = Category
		fields = ('id', 'name',)



class NetEnterprisesSerializer(serializers.ModelSerializer):
	""""""
	class Meta:
		model = NetEnterprises
		fields = ('id', 'name',)



class ProductSerializer(serializers.ModelSerializer):
	""""""
	class Meta:
		model = Product
		fields = ('id', 'name', 'price')



class EnterprisesSerializer(serializers.ModelSerializer):
	""""""
	class Meta:
		model = Enterprises
		fields = ('id', 'name', 'description')