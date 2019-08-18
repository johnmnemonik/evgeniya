from django.urls import path


from api.views import (
	api_enterprises, api_enterprises_detail, api_product_detail, 
	api_enterprises_list, api_product_search)



urlpatterns = [
	path('api/product/<int:pk>/', api_product_detail),
	path('api/enterprises/<int:pk>/', api_enterprises_detail),
	path('api/organizations/<int:pk>/', api_enterprises_list),
	path('api/product/search/<str:query>/', api_product_search),

]