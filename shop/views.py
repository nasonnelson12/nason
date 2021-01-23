from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from stripe.api_resources import review
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View, TemplateView

from shop.models import Category, Product, Images, Comment, CommentForm, ContactUs
from .forms import ContactForm



# Create your views here.

def homeview(request):
	category = Category.objects.all()
	product = Product.objects.filter(status='True')
	product_slider = Product.objects.filter(slider='True').order_by('-id')[:5]
	latest_product = Product.objects.filter(slider='True').order_by('-id')[:5]
	paginator = Paginator(product, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {  'category':category,
				 'product':product,
				 'page_obj':page_obj,
				 'product_slider':product_slider,
				 'latest_product':latest_product
			}
	return render (request, "index.html", context )
	

def product_slider(request, id, slug):
	category = Category.objects.all()
	product = Product.objects.filter(category_id=id )
	product_slider = Product.objects.filter(slider='True').order_by('-id')[:3]
	context = {  'category':category,
				 'product':product,
				 'product_slider':product_slider,
				 }
	return render (request, "slider.html", context )

def category_product(request, id, slug):
	category = Category.objects.all()
	product = Product.objects.filter(category_id=id, status='True')
	context = {  'category':category,
				 'product':product,
				 'product_slider':product_slider}
	return render (request, "shop.html", context )


class contact(View):
	def get(self, *args, **kwargs):
		category = Category.objects.all()
		form = ContactForm()
		context = {
			'category':category,
			'form': form
		}
		return render(self.request, "contact.html", context)

	def post(self, *args, **kwargs):
		form = ContactForm(self.request.POST)
		if form.is_valid():
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			email = form.cleaned_data.get('email')
			phone = form.cleaned_data.get('phone')
			massage = form.cleaned_data.get('massage')

			try:
				conta = ContactUs()
				conta.first_name = first_name 
				conta.last_name = last_name 
				conta.email = email
				conta.phone = phone 
				conta.massage = massage
				conta.save()

				messages.info(self.request, "Thank you to contact us we shall contact you very soon on your email")
				return redirect("/")

			except ObjectDoesNotExist:
				messages.info(self.request, "something went wrong")
				return redirect("/contact")


def search(request):
	try:
		q = request.GET.get('keyword')
	except:
		q = None
	if q:
		products = Product.objects.filter(title__contains=q, status='True')
		category = Category.objects.all()
		context = {'query':q, 'products':products, 'category':category}
		template = 'search.html'
	else:
		template = 'index.html'
		context = {}
	return render(request, template, context)
		


def ItemDetailView(request, slug, id):
	if request.user.is_authenticated:
		query = request.GET.get('q')
		category = Category.objects.all()
		product = Product.objects.get(id=id)
		images = Images.objects.filter(product__id=product.id)
		comments = Comment.objects.filter(product__id=product.id, status='True')
	
		context = {'category':category, 'product':product,
	           'images':images, 'comments':comments
	           }
		return render(request, 'product.html', context)
	else:
		return redirect('/login/')
	

def addcomment(request, id):
	url = request.META.get('HTTP_REFERER')
	current_user = request.user
	#return HttpResponse(url)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			data = Comment()
			data.product_id = id
			data.user_id = current_user.id
			data.subject = form.cleaned_data['subject']
			data.comment = form.cleaned_data['comment']
			data.ip = request.META.get('REMOTE_ADDR')
			data.save()
		messages.success(request, "Your review has been sent. Thank you for your intered")
		return HttpResponseRedirect(url)

	return HttpResponseRedirect(url)

