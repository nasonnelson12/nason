from django.urls import path
from . import views

app_name = 'order' 

urlpatterns = [
	path('', views.homeview, name='home'),
	path('addtoshopcart/<int:id>/', views.addtoshopcart, name='addtoshopcart'),
	path('deletefromcart/<int:id>/', views.delete_cart, name='deletefromcart'),
	#path('payment/', views.Payment.as_view(), name='payment'),
    path('orderproduct/', views.orderproductviews, name='orderproduct'),
    #path('paymentcash/', views.PaymentCash.as_view(), name='paymentcash')

	
] 