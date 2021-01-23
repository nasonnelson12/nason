from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
	path('profile/', views.profile, name='profile'),
	path('update/', views.update, name='update'),
	path('password/', views.password, name='password'),
	path('orders/', views.user_orders, name='orders'),
	path('orderproduct/', views.orderproduct, name='orderproduct'),
	path('orderdetail/<int:id>', views.user_orderdetail, name='orderdetail'),
	path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
	path('comment/', views.user_comment, name='user_comment'),
	path('faq/', views.faq, name='faq')

]