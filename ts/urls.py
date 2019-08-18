from django.urls import path

from ts.views import product_view, category_view 


urlpatterns = [
	path('search/', product_view, name='search'),
	path('category/', category_view, name='category'),

]