from django.urls import path
from . import views
from order import views as OrderViews
from User import views as UserViews

app_name = 'shop' 

urlpatterns = [
	path('', views.homeview, name='home'),
	path('category/<int:id>/<slug:slug>', views.category_product, name='category_product'),
	path('product/<int:id>/<slug:slug>', views.product_slider, name='product_slider'),
	path('search/', views.search, name='search'),
	path('contact/', views.contact.as_view(), name='contact'),
	path('shopdetails/<slug>/<int:id>', views.ItemDetailView, name='shopdetails'),
	path('addcomment/<int:id>/', views.addcomment, name='addcomment'),
	path('shopingcart/', OrderViews.shoping_cart, name='shopingcart'),
	#path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
	#path('paymentcash/<payment_option>/', views.PaymentCash.as_view(), name='paymentcash'),
	path('signup/', UserViews.signup, name = 'signup'),
    path('login/', UserViews.loginPage, name = "login"),
    path('logout/', UserViews.logoutUser, name = 'logout'),
	 
]  