from django.contrib import admin

from ts.models import Region, Category, NetEnterprises, Product, Enterprises


class AdminRegion(admin.ModelAdmin):
	pass


class AdminCategory(admin.ModelAdmin):
	pass


class AdminNetEnterprises(admin.ModelAdmin):
	pass


class AdminProduct(admin.ModelAdmin):
	pass


class AdminEnterprises(admin.ModelAdmin):
	exclude = ('-product',)



admin.site.register(Region, AdminRegion)
admin.site.register(Category, AdminCategory)
admin.site.register(NetEnterprises, AdminNetEnterprises)
admin.site.register(Product, AdminProduct)
admin.site.register(Enterprises, AdminEnterprises)