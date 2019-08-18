from django.db import models



class Region(models.Model):
	name = models.CharField("Регион", max_length=200)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Регион города'
		verbose_name_plural = 'Регионы города'



class Category(models.Model):
	name = models.CharField("Категория", max_length=200)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'



class NetEnterprises(models.Model):
	name = models.CharField("Сеть предприятий", max_length=200)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Сеть предприятий'
		verbose_name_plural = 'Сети предприятий'




class Product(models.Model):
	name = models.CharField("название", max_length=200)
	category = models.ForeignKey(Category, verbose_name="категория", on_delete=models.CASCADE)
	sell = models.ManyToManyField(NetEnterprises, verbose_name='сеть предприятий')
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')



	def __str__(self):
		return "{}\t{}".format(self.name, self.price)


	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
	



class Enterprises(models.Model):
	netenter = models.ForeignKey(NetEnterprises, on_delete=models.CASCADE, verbose_name='сеть предприятий')
	name = models.CharField("Предприятие", max_length=200)
	description = models.TextField("Описание")
	region = models.ManyToManyField(Region, verbose_name='Районы')
	
	product = models.ManyToManyField(Product, verbose_name='продукты')


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Предприятие'
		verbose_name_plural = 'Предприятия'
	




